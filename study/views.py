from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import redirect
from django.http import JsonResponse
from django.views import View
from django.conf import settings
from google_auth_oauthlib.flow import Flow
from google.oauth2.credentials import Credentials
from .services import *
from .serializers import *

class AddExamToCalendarView(APIView):
    def post(self, request, *args, **kwargs):
        # Validate required fields
        exam_date = request.data.get('exam_date')
        exam_time = request.data.get('exam_time')
        subject = request.data.get('subject')

        errors = []
        if not exam_date:
            errors.append("The 'exam_date' field is required.")
        if not exam_time:
            errors.append("The 'exam_time' field is required.")
        if not subject:
            errors.append("The 'subject' field is required.")

        if errors:
            return Response({"errors": errors}, status=400)

        # Parse the date and time into a datetime object
        try:
            exam_datetime = datetime.strptime(f"{exam_date} {exam_time}", "%Y-%m-%d %H:%M")
        except ValueError:
            return Response(
                {"error": "Invalid date or time format. Use YYYY-MM-DD for date and HH:MM (24-hour format) for time."},
                status=400
            )

        # Check for Google credentials in the session
        creds_data = request.session.get('google_credentials')
        if not creds_data:
            return Response(
                {"error": "You must authenticate with Google Calendar before using this feature."},
                status=401
            )

        # Validate required scopes
        if 'https://www.googleapis.com/auth/calendar' not in creds_data.get('scopes', []):
            return Response(
                {"error": "Your credentials do not include the required Google Calendar scope."},
                status=403
            )

        # Build OAuth2 credentials
        try:
            credentials = Credentials(
                creds_data['token'],
                refresh_token=creds_data['refresh_token'],
                token_uri=creds_data['token_uri'],
                client_id=creds_data['client_id'],
                client_secret=creds_data['client_secret'],
                scopes=creds_data['scopes']
            )
        except KeyError as e:
            return Response(
                {"error": f"Invalid credentials: Missing key {str(e)}."},
                status=400
            )

        # Add the exam to Google Calendar
        result = add_exam_to_calendar(credentials, exam_datetime, subject)
        return Response(result)

class SendStudyNotesView(APIView):
    def post(self, request, *args, **kwargs):
        # Validate required fields
        to_email = request.data.get('to_email')
        note_id = request.data.get('note_id')

        errors = []
        if not to_email:
            errors.append("The 'to_email' field is required.")
        if not note_id:
            errors.append("The 'note_id' field is required.")

        if errors:
            return Response(
                {"errors": errors},
                status=400
            )

        # Fetch the study note
        try:
            study_note = StudyNote.objects.get(id=note_id)
        except StudyNote.DoesNotExist:
            return Response(
                {"error": f"No study note found with ID {note_id}."},
                status=404
            )

        # Check for Google credentials in the session
        creds_data = request.session.get('google_credentials')
        if not creds_data:
            return Response(
                {"error": "You must authenticate with Gmail before using this feature."},
                status=401
            )

        # Validate required scopes
        if 'https://www.googleapis.com/auth/gmail.send' not in creds_data.get('scopes', []):
            return Response(
                {"error": "Your credentials do not include the required Gmail scope."},
                status=403
            )

        # Build OAuth2 credentials
        try:
            credentials = Credentials(
                creds_data['token'],
                refresh_token=creds_data['refresh_token'],
                token_uri=creds_data['token_uri'],
                client_id=creds_data['client_id'],
                client_secret=creds_data['client_secret'],
                scopes=creds_data['scopes']
            )
        except KeyError as e:
            return Response(
                {"error": f"Invalid credentials: Missing key {str(e)}."},
                status=400
            )

        # Send the study notes via Gmail
        result = send_study_notes_email(credentials, to_email, study_note)
        return Response(result)
class MotivationView(View):
    def get(self, request, *args, **kwargs):
        """
        Fetches a motivational quote using the fetch_motivational_quote service
        and returns it as a JSON response.
        """
        # Step 1: Fetch the motivational quote using the service
        quote_data = fetch_motivational_quote()

        # Step 2: Return the quote as a JSON response
        return JsonResponse(quote_data)

@api_view(['GET'])
def generate_study_schedule_view(request, study_schedule_id, timer_id):
    """
    Generates a detailed study schedule based on the specified StudySchedule and StudyBreakTimer.
    """
    try:
        # Fetch the StudySchedule instance
        study_schedule = StudySchedule.objects.get(id=study_schedule_id)
    except StudySchedule.DoesNotExist:
        return Response({"error": "Study schedule not found."}, status=status.HTTP_404_NOT_FOUND)

    try:
        # Fetch the StudyBreakTimer instance
        timer = StudyBreakTimer.objects.get(id=timer_id)
    except StudyBreakTimer.DoesNotExist:
        return Response({"error": "Study break timer not found."}, status=status.HTTP_404_NOT_FOUND)

    # Extract relevant data from the StudySchedule instance
    study_date = study_schedule.study_date
    study_hours = study_schedule.study_hours
    subjects = study_schedule.subjects  # Comma-separated list of subjects

    # Generate the detailed schedule using the timer configuration
    schedule = generate_detailed_study_schedule(
        study_date=study_date,
        study_hours=study_hours,
        subjects=subjects,
        study_duration=timer.study_duration,
        break_duration=timer.break_duration
    )

    return Response(schedule, status=status.HTTP_200_OK)


@api_view(['GET'])
def recommend_study_resources_view(request, resource_type):
    """
    Recommends study resources based on the subject and resource type.
    If resource_type is provided, fetches resources from the CORE API.
    Otherwise, fetches resources from the database.
    """
    subject = request.query_params.get('subject')
    if not subject:
        return Response({"error": "Subject is required."}, status=status.HTTP_400_BAD_REQUEST)

    # Map resource types to CORE API types
    type_mapping = {
        "books": "book",
        "articles": "journal-article",
        "research-papers": "conference-paper",
        "datasets": "dataset",
    }
    core_resource_type = type_mapping.get(resource_type, "journal-article")

    # Fetch resources from CORE API with filters
    params = {
        "q": subject,
        "type": core_resource_type,
        "apiKey": settings.CORE_API_KEY  # Use Django settings for API key
    }
    try:
        response = requests.get(settings.CORE_API_URL, params=params)
        response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)
        core_data = response.json()
        resources = [
            {"title": item.get("title", "No Title"), "url": item.get("downloadUrl", "#"),
             "type": item.get("type", "Unknown")}
            for item in core_data.get("results", [])
        ]
    except requests.RequestException as e:
        return Response({"error": f"Failed to fetch resources: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # Fallback to database if no resources are found in the CORE API
    if not resources:
        resources = recommend_study_resources(subject)

    return Response(resources, status=status.HTTP_200_OK)

@api_view(['GET'])
def generate_study_statistics_view(request):
    """
    Generates and returns study statistics, including highest/lowest grades and most/least studied subjects.
    """
    # Generate study statistics
    stats = generate_study_statistics()

    return Response({
        "message": "Study statistics generated successfully.",
        "statistics": stats,
    }, status=status.HTTP_200_OK)


@api_view(['GET'])
def fetch_quiz_questions_view(request):
    """
    Fetches quiz questions based on the subject query parameter.
    """
    # Get the 'subject' query parameter
    subject = request.query_params.get("subject", "general").lower()

    try:
        # Fetch quiz questions using the service
        questions = fetch_quiz_questions(subject)

        # Format the response
        formatted_questions = []
        for question in questions:
            formatted_questions.append({
                "question": question["question"],
                "correct_answer": question["correct_answer"],
                "incorrect_answers": question["incorrect_answers"],
                "difficulty": question["difficulty"],
            })

        return Response({"questions": formatted_questions})
    except Exception as e:
        return Response({"error": str(e)}, status=500)


def oauth_redirect(request):
    """
    Redirects the user to Google's OAuth consent screen.
    """
    flow = Flow.from_client_secrets_file(
        'credentials/credentials.json',
        scopes=[
            'https://www.googleapis.com/auth/gmail.send',
            'https://www.googleapis.com/auth/calendar'
        ],
        redirect_uri=request.build_absolute_uri('/oauth/callback/')
    )
    authorization_url, state = flow.authorization_url(
        access_type='offline',
        include_granted_scopes='true'
    )
    request.session['oauth_state'] = state
    print("OAuth Redirect: Generated state:", state)
    print("OAuth Redirect: Redirecting to:", authorization_url)
    return redirect(authorization_url)


def oauth_callback(request):
    """
    Handles the OAuth callback from Google.
    Exchanges the authorization code for tokens.
    """
    state = request.session.get('oauth_state')
    received_state = request.GET.get('state')
    print("OAuth Callback: Stored state:", state)
    print("OAuth Callback: Received state:", received_state)
    if not state or state != received_state:
        return JsonResponse({"error": "Invalid state parameter"}, status=400)

    try:
        flow = Flow.from_client_secrets_file(
            'credentials/credentials.json',
            scopes=[
                'https://www.googleapis.com/auth/gmail.send',
                'https://www.googleapis.com/auth/calendar'
            ],
            redirect_uri=request.build_absolute_uri('/oauth/callback/')
        )
        authorization_response = request.build_absolute_uri()
        print("OAuth Callback: Authorization response:", authorization_response)
        flow.fetch_token(authorization_response=authorization_response)

        credentials = flow.credentials
        request.session['google_credentials'] = {
            'token': credentials.token,
            'refresh_token': credentials.refresh_token,
            'token_uri': credentials.token_uri,
            'client_id': credentials.client_id,
            'client_secret': credentials.client_secret,
            'scopes': credentials.scopes
        }
        print("OAuth Callback: Credentials fetched successfully.")
        return JsonResponse({"message": "OAuth flow completed successfully!"})
    except Exception as e:
        print("OAuth Callback: Error occurred:", str(e))
        return JsonResponse({"error": f"An error occurred during OAuth callback: {str(e)}"}, status=500)

# Default ViewSets (Unchanged)
# Endpoint 1: /tasks
class StudyTaskViewSet(viewsets.ModelViewSet):
    queryset = StudyTask.objects.all()
    serializer_class = StudyTaskSerializer

# Endpoint 2: /subjects-lessons
class SubjectLessonViewSet(viewsets.ModelViewSet):
    queryset = SubjectLesson.objects.all()
    serializer_class = SubjectLessonSerializer

# Endpoint 3: /subjects-diary
class SubjectDiaryViewSet(viewsets.ModelViewSet):
    queryset = SubjectDiary.objects.all()
    serializer_class = SubjectDiarySerializer

# Endpoint 4: /study-schedule
class StudyScheduleViewSet(viewsets.ModelViewSet):
    queryset = StudySchedule.objects.all()
    serializer_class = StudyScheduleSerializer

# Endpoint 5: /study-resources
class StudyResourceViewSet(viewsets.ModelViewSet):
    queryset = StudyResource.objects.all()
    serializer_class = StudyResourceSerializer

# Endpoint 6: /study-break
class StudyBreakTimerViewSet(viewsets.ModelViewSet):
    queryset = StudyBreakTimer.objects.all()
    serializer_class = StudyBreakTimerSerializer

# Endpoint 7: /study-progress
class StudyProgressViewSet(viewsets.ModelViewSet):
    queryset = StudyProgress.objects.all()
    serializer_class = StudyProgressSerializer

# Endpoint 8: /study-challenges
class StudyChallengeViewSet(viewsets.ModelViewSet):
    queryset = StudyChallenge.objects.all()
    serializer_class = StudyChallengeSerializer

# Endpoint 9: /study/quiz
class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

# Endpoint 10: /study-prompt
class StudyPromptViewSet(viewsets.ModelViewSet):
    queryset = StudyPrompt.objects.all()
    serializer_class = StudyPromptSerializer

# Endpoint 11: /resources/quiz (standalone - no model needed)
# [Placeholder: This endpoint fetches external data and requires no ModelViewSet]

# Endpoint 12: /study-reflection
class StudyReflectionViewSet(viewsets.ModelViewSet):
    queryset = StudyReflection.objects.all()
    serializer_class = StudyReflectionSerializer

# Endpoint 13: /course/grades
class CourseGradeViewSet(viewsets.ModelViewSet):
    queryset = CourseGrade.objects.all()
    serializer_class = CourseGradeSerializer

# Endpoint 14: /notes
class StudyNoteViewSet(viewsets.ModelViewSet):
    queryset = StudyNote.objects.all()
    serializer_class = StudyNoteSerializer

# Endpoints 15-20 are STANDALONE and require NO ModelViewSet:
# 15. /send-study-notes → Integrates with Gmail API
# 16. /motivation → Fetches from external quote API
# 17. /study-resources/recommendations → External resource API
# 18. /add-exam-to-calendar → Google Calendar integration
# 19. /generate-study-statistics → Aggregates data from StudyProgress/CourseGrade
# 20. /generate-study-schedule → Uses StudySchedule + StudyBreakTimer data