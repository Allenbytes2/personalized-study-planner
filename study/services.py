from datetime import timedelta
from django.db.models import Q
from django.utils import timezone
from .models import (
    StudySchedule,
    StudyResource,
    StudyBreakTimer,
    StudyProgress,
    ExamAlert,
    StudyTip,
    StudyTaskPriority,
    SubjectSuggestion,
    StudyTracker,
    StudyNote,
    StudyChallenge,
    StudyPrompt,
    Quiz,
    StudyReflection,
    StudyFeedback,
    Motivation,
    StudyStatistic,
    CourseGrade,
    StudyPlanAdjustment,
    StudyReminder,
)

# Service for creating personalized study schedule
def generate_study_schedule(user, available_hours, exam_dates, assignment_due_dates):
    # Generate a personalized study schedule based on user inputs (exam dates, assignment dates, and available study hours)
    study_schedule = []
    for date in exam_dates:
        schedule = StudySchedule.objects.create(
            user=user,
            study_date=date,
            study_hours=available_hours,
            subjects="Math, Science",  # Example, you can calculate subjects based on context
        )
        study_schedule.append(schedule)
    return study_schedule

# Service to recommend study resources based on subject
def recommend_study_resources(subject):
    return StudyResource.objects.filter(subject=subject)

# Service for Pomodoro timer configuration
def configure_study_timer(user, study_duration, break_duration):
    timer = StudyBreakTimer.objects.create(
        user=user,
        study_duration=study_duration,
        break_duration=break_duration,
    )
    return timer

# Service to track progress
def track_study_progress(user, subject, duration, completed=False):
    progress = StudyProgress.objects.create(
        user=user,
        subject=subject,
        study_session_date=timezone.now().date(),
        duration=duration,
        completed=completed
    )
    return progress

# Service for sending exam reminders
def set_exam_reminder(user, exam_date, reminder_time, subject):
    reminder = ExamAlert.objects.create(
        user=user,
        exam_date=exam_date,
        reminder_time=reminder_time,
        subject=subject
    )
    return reminder

# Service for providing study tips based on subject
def get_study_tips(subject):
    return StudyTip.objects.filter(subject=subject)

# Service to prioritize study tasks based on urgency and difficulty
def prioritize_study_tasks(user):
    tasks = StudyTaskPriority.objects.filter(user=user)
    prioritized_tasks = sorted(tasks, key=lambda x: (x.urgency, x.difficulty), reverse=True)
    return prioritized_tasks

# Service to suggest subjects based on user's performance
def suggest_subject_based_on_performance(user):
    grades = CourseGrade.objects.filter(user=user)
    # Example logic: Suggest subjects where the user has low grades
    low_performance_subjects = grades.filter(grade__in=["D", "E", "F"])
    suggestions = []
    for grade in low_performance_subjects:
        suggestions.append(
            SubjectSuggestion.objects.create(
                user=user,
                suggested_subject=grade.course_name,
                reason="Low grade performance"
            )
        )
    return suggestions

# Service to track total study time
def track_total_study_time(user):
    study_sessions = StudyTracker.objects.filter(user=user)
    total_study_time = sum(session.duration for session in study_sessions)
    return total_study_time

# Service for sharing study notes
def share_study_notes(user, subject, note_content):
    note = StudyNote.objects.create(
        user=user,
        subject=subject,
        note_content=note_content
    )
    return note

# Service to create study challenges
def create_study_challenge(user, description, start_date, end_date):
    challenge = StudyChallenge.objects.create(
        user=user,
        challenge_description=description,
        start_date=start_date,
        end_date=end_date
    )
    return challenge

# Service to generate random study prompts
def generate_study_prompt(subject):
    return StudyPrompt.objects.filter(subject=subject).order_by('?').first()

# Service to recommend quizzes for self-assessment
def recommend_quiz_for_subject(subject):
    return Quiz.objects.filter(subject=subject)

# Service for study reflection
def study_reflection(user, strengths, areas_for_improvement):
    reflection = StudyReflection.objects.create(
        user=user,
        reflection_date=timezone.now().date(),
        strengths=strengths,
        areas_for_improvement=areas_for_improvement
    )
    return reflection

# Service to collect study feedback
def collect_study_feedback(user, feedback_text):
    feedback = StudyFeedback.objects.create(
        user=user,
        feedback_date=timezone.now().date(),
        feedback_text=feedback_text
    )
    return feedback

# Service to get motivational quotes
def get_motivation():
    return Motivation.objects.all().order_by('?').first()

# Service to generate study statistics
def get_study_statistics(user):
    statistics = StudyStatistic.objects.filter(user=user).first()
    if not statistics:
        statistics = StudyStatistic.objects.create(user=user, total_study_hours=0, most_studied_subject="None")
    return statistics

# Service to track grades for a course
def track_course_grades(user):
    return CourseGrade.objects.filter(user=user)

# Service to adjust study plans based on changes
def adjust_study_plan(user, reason, adjusted_date):
    adjustment = StudyPlanAdjustment.objects.create(
        user=user,
        adjustment_reason=reason,
        adjusted_date=adjusted_date
    )
    return adjustment

# Service to set study reminder notifications
def set_study_reminder(user, reminder_date, reminder_time, message):
    reminder = StudyReminder.objects.create(
        user=user,
        reminder_date=reminder_date,
        reminder_time=reminder_time,
        message=message
    )
    return reminder

# Helper function to apply filtering for study resources
def filter_study_resources_by_type(resource_type):
    return StudyResource.objects.filter(resource_type=resource_type)

# Helper function to calculate study schedule adjustments based on new input
def adjust_schedule_for_new_deadlines(user, new_exam_dates, new_assignment_due_dates):
    # Example logic: Update existing schedules for new deadlines
    for schedule in StudySchedule.objects.filter(user=user):
        if schedule.study_date in new_exam_dates or schedule.study_date in new_assignment_due_dates:
            schedule.study_hours += 2  # Add 2 more hours for rescheduling
            schedule.save()
    return "Study schedule updated for new deadlines"
