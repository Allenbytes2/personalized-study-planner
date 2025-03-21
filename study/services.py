from datetime import date, timedelta, datetime
from django.db.models import Q
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from email.mime.text import MIMEText
import base64
from django.conf import settings
from .models import StudyResource, CourseGrade, StudyProgress, StudyNote
from collections import defaultdict
import requests
import random

# 1. Generate a Personalized Study Schedule

def generate_detailed_study_schedule(study_date, study_hours, subjects, study_duration, break_duration):
    """
    Generates a detailed study schedule with multiple cycles of study and break timers.
    Skips 12 PM to 1 PM for lunch and 7 PM to 8 PM for dinner.
    """
    # Validate study_hours
    if not isinstance(study_hours, (int, float)) or study_hours <= 0:
        return {
            "message": "Invalid study hours provided.",
            "schedule": []
        }
    # Validate subjects
    if not isinstance(subjects, str) or not subjects.strip():
        return {
            "message": "No subjects available for scheduling.",
            "schedule": []
        }
    # Initialize variables
    schedule = []
    current_time = datetime.combine(study_date, datetime.min.time()).replace(hour=8, minute=0)  # Start at 8:00 AM
    remaining_hours = study_hours
    # Split subjects into a list (comma-separated string)
    subject_list = [subject.strip() for subject in subjects.split(",") if subject.strip()]
    # Define lunch and dinner break times
    lunch_start = current_time.replace(hour=12, minute=0)
    lunch_end = current_time.replace(hour=13, minute=0)
    dinner_start = current_time.replace(hour=19, minute=0)
    dinner_end = current_time.replace(hour=20, minute=0)
    # Allocate time for each subject in cycles of study and break
    for subject in subject_list:
        while remaining_hours > 0:
            # Check if current time falls within lunch or dinner break
            if lunch_start <= current_time < lunch_end:
                schedule.append({
                    "subject": "Lunch Break",
                    "type": "lunch",
                    "start_time": lunch_start.strftime("%H:%M"),
                    "end_time": lunch_end.strftime("%H:%M"),
                    "duration_minutes": 60,  # Already an integer
                    "message": "Lunch break skipped from 12 PM to 1 PM."
                })
                current_time = lunch_end  # Skip to the end of lunch
                continue
            if dinner_start <= current_time < dinner_end:
                schedule.append({
                    "subject": "Dinner Break",
                    "type": "dinner",
                    "start_time": dinner_start.strftime("%H:%M"),
                    "end_time": dinner_end.strftime("%H:%M"),
                    "duration_minutes": 60,  # Already an integer
                    "message": "Dinner break skipped from 7 PM to 8 PM."
                })
                current_time = dinner_end  # Skip to the end of dinner
                continue
            # Study session
            study_session_hours = min(remaining_hours, study_duration / 60)  # Convert minutes to hours
            end_study_time = current_time + timedelta(hours=study_session_hours)
            # Ensure study session does not overlap with lunch or dinner
            if lunch_start <= end_study_time <= lunch_end:
                end_study_time = lunch_start  # Adjust end time to start of lunch
            if dinner_start <= end_study_time <= dinner_end:
                end_study_time = dinner_start  # Adjust end time to start of dinner
            schedule.append({
                "subject": subject,
                "type": "study",
                "start_time": current_time.strftime("%H:%M"),
                "end_time": end_study_time.strftime("%H:%M"),
                "duration_minutes": int(round((end_study_time - current_time).total_seconds() / 60)),  # Convert to integer
            })
            # Update remaining hours and current time
            remaining_hours -= (end_study_time - current_time).total_seconds() / 3600
            current_time = end_study_time
            # Break session (if there's still time left)
            if remaining_hours > 0:
                break_session_hours = min(remaining_hours, break_duration / 60)  # Convert minutes to hours
                end_break_time = current_time + timedelta(hours=break_session_hours)
                # Ensure break session does not overlap with lunch or dinner
                if lunch_start <= end_break_time <= lunch_end:
                    end_break_time = lunch_start  # Adjust end time to start of lunch
                if dinner_start <= end_break_time <= dinner_end:
                    end_break_time = dinner_start  # Adjust end time to start of dinner
                schedule.append({
                    "subject": subject,
                    "type": "break",
                    "start_time": current_time.strftime("%H:%M"),
                    "end_time": end_break_time.strftime("%H:%M"),
                    "duration_minutes": int(round((end_break_time - current_time).total_seconds() / 60)),  # Convert to integer
                })
                # Update remaining hours and current time
                remaining_hours -= (end_break_time - current_time).total_seconds() / 3600
                current_time = end_break_time
            # Stop if no more time is left
            if remaining_hours <= 0:
                break
    return {
        "message": "Detailed study schedule generated successfully.",
        "schedule": schedule,
    }

# 2. Recommend Study Resources
def recommend_study_resources(subject):
    """
    Suggests study resources like books, articles, and videos tailored to the subject.
    Fetches resources from the database.
    """
    resources = StudyResource.objects.filter(subject=subject).order_by('?')[:5]
    return [{'title': res.title, 'url': res.url, 'type': res.resource_type} for res in resources]


# 4. Send Exam Alerts (Advanced Filtering)

def add_exam_to_calendar(credentials, exam_datetime, subject):
    """
    Adds an exam alert to Google Calendar.
    :param credentials: OAuth2 credentials for the user.
    :param exam_datetime: A datetime object representing the exam date and time.
    :param subject: The subject of the exam.
    """
    try:
        # Build the Google Calendar service
        service = build('calendar', 'v3', credentials=credentials)

        # Construct the event
        event = {
            'summary': f'Exam: {subject}',
            'description': f'Upcoming exam for {subject}.',
            'start': {
                'dateTime': exam_datetime.isoformat(),
                'timeZone': 'Asia/Manila',  # Adjust to your timezone if needed
            },
            'end': {
                'dateTime': (exam_datetime + timedelta(hours=1)).isoformat(),
                'timeZone': 'Asia/Manila',
            },
        }

        # Insert the event into the user's primary calendar
        event_result = service.events().insert(calendarId='primary', body=event).execute()
        print(f"Event created with ID: {event_result['id']}")
        return {"message": "Exam added to Google Calendar successfully!"}

    except HttpError as e:
        return {"error": f"An error occurred while adding the exam to Google Calendar: {e}"}

# 5. Quiz Fetcher
def fetch_quiz_questions(subject):
    """
    Fetches quiz questions from the Open Trivia Database API based on the subject.
    """
    # Open Trivia Database API endpoint
    base_url = "https://opentdb.com/api.php"

    # Map subject to Open Trivia categories (optional)
    category_map = {
        "science": 17,  # Science & Nature
        "history": 23,  # History
        "geography": 22,  # Geography
        "sports": 21,  # Sports
        "general": 9,  # General Knowledge
    }

    # Get the category ID based on the subject
    category_id = category_map.get(subject.lower(), 9)  # Default to General Knowledge

    # Query parameters
    params = {
        "amount": 5,  # Number of questions
        "category": category_id,
        "type": "multiple",  # Multiple-choice questions
        "difficulty": "medium",  # Difficulty level
    }

    try:
        # Make the GET request to the Open Trivia Database API
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the JSON response
        data = response.json()

        if data["response_code"] == 0:
            return data["results"]
        else:
            raise Exception(f"Error fetching quiz questions: {data['response_code']}")
    except requests.exceptions.RequestException as e:
        raise Exception(f"Failed to fetch quiz questions: {str(e)}")

# 6. Share Notes
def send_study_notes_email(credentials, to_email, study_note):
    """
    Sends study notes via Gmail.
    :param credentials: OAuth2 credentials for the user.
    :param to_email: The recipient's email address.
    :param study_note: An instance of StudyNote.
    """
    try:
        service = build('gmail', 'v1', credentials=credentials)

        message = MIMEText(study_note.note_content)
        message['to'] = to_email
        message['subject'] = study_note.subject
        raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

        sent_message = service.users().messages().send(userId='me', body={'raw': raw_message}).execute()
        print(f"Email sent with ID: {sent_message['id']}")
        return {"message": "Notes sent successfully via Gmail!"}
    except HttpError as e:
        return {"error": f"An error occurred while sending the email: {e}"}
# 9. Generate Study Statistics
def generate_study_statistics():
    """
    Generates insights into study habits, including highest/lowest grades and most/least studied subjects.
    """
    # Fetch course grades
    course_grades = CourseGrade.objects.all()
    grade_data = [
        {"subject": grade.course_name, "grade": float(grade.grade)}  # Convert grade to float for comparison
        for grade in course_grades
    ]

    # Calculate highest and lowest grades
    if grade_data:
        highest_grade = min(grade_data, key=lambda x: x['grade'])  # Lowest numerical value is the best grade
        lowest_grade = max(grade_data, key=lambda x: x['grade'])   # Highest numerical value is the worst grade
    else:
        highest_grade = {"subject": None, "grade": None}
        lowest_grade = {"subject": None, "grade": None}

    # Fetch study progress
    study_progress = StudyProgress.objects.all()
    study_hours_by_subject = defaultdict(float)
    for progress in study_progress:
        study_hours_by_subject[progress.subject] += progress.study_hours # Convert minutes to hours

    # Calculate most and least studied subjects
    if study_hours_by_subject:
        most_studied_subject = max(study_hours_by_subject.items(), key=lambda x: x[1])
        least_studied_subject = min(study_hours_by_subject.items(), key=lambda x: x[1])
    else:
        most_studied_subject = (None, 0)
        least_studied_subject = (None, 0)

    # Return the results
    return {
        "highest_grade": {
            "subject": highest_grade["subject"],
            "grade": highest_grade["grade"],
        },
        "lowest_grade": {
            "subject": lowest_grade["subject"],
            "grade": lowest_grade["grade"],
        },
        "most_studied_subject": {
            "subject": most_studied_subject[0],
            "study_hours": round(most_studied_subject[1], 2),
        },
        "least_studied_subject": {
            "subject": least_studied_subject[0],
            "study_hours": round(least_studied_subject[1], 2),
        },
    }


FALLBACK_QUOTES = [
    {"quote": "The way to get started is to quit talking and begin doing.", "author": "Walt Disney"},
    {"quote": "Believe you can and you're halfway there.", "author": "Theodore Roosevelt"},
    {"quote": "Success is not final, failure is not fatal: It is the courage to continue that counts.",
     "author": "Winston Churchill"},
]


def fetch_motivational_quote():
    """
    Fetches a random motivational quote from ZenQuotes API.
    If the API fails, returns a fallback quote.
    """
    api_url = "https://zenquotes.io/api/random"

    try:
        response = requests.get(api_url, timeout=5)
        response.raise_for_status()

        data = response.json()
        if isinstance(data, list) and len(data) > 0:
            quote = data[0].get("q", "No quote available")
            author = data[0].get("a", "Unknown")
            return {"quote": quote, "author": author}
        else:
            return random.choice(FALLBACK_QUOTES)

    except requests.RequestException:
        return random.choice(FALLBACK_QUOTES)