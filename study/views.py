from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import random
from datetime import date
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
from .serializers import (
    StudyScheduleSerializer,
    StudyResourceSerializer,
    StudyBreakTimerSerializer,
    StudyProgressSerializer,
    ExamAlertSerializer,
    StudyTipSerializer,
    StudyTaskPrioritySerializer,
    SubjectSuggestionSerializer,
    StudyTrackerSerializer,
    StudyNoteSerializer,
    StudyChallengeSerializer,
    StudyPromptSerializer,
    QuizSerializer,
    StudyReflectionSerializer,
    StudyFeedbackSerializer,
    MotivationSerializer,
    StudyStatisticSerializer,
    CourseGradeSerializer,
    StudyPlanAdjustmentSerializer,
    StudyReminderSerializer,
)
from .services import (
    generate_study_schedule,
    recommend_study_resources,
    analyze_study_progress,
    send_exam_alerts,
    get_study_tips,
    prioritize_study_tasks,
    suggest_subjects,
    track_study_sessions,
    adjust_study_plan,
    generate_reflection_report,
)

def get_motivation():
    """
    Returns a random motivational quote from either the predefined list or the database.
    Each quote includes metadata: the quote text, author, and source ("predefined" or "user").
    """
    # Predefined quotes with authors
    predefined_quotes = [
        {"quote": "The harder you work for something, the greater you'll feel when you achieve it.", "author": "Unknown", "source": "predefined"},
        {"quote": "Don't watch the clock; do what it does. Keep going.", "author": "Unknown", "source": "predefined"},
        {"quote": "Success is the sum of small efforts, repeated day in and day out.", "author": "Robert Collier", "source": "predefined"},
        {"quote": "The future depends on what you do today.", "author": "Mahatma Gandhi", "source": "predefined"},
        {"quote": "Believe you can and you're halfway there.", "author": "Theodore Roosevelt", "source": "predefined"},
        {"quote": "What you get by achieving your goals is not as important as what you become by achieving your goals.", "author": "Zig Ziglar", "source": "predefined"},
        {"quote": "Education is the most powerful weapon which you can use to change the world.", "author": "Nelson Mandela", "source": "predefined"},
        {"quote": "Don’t stop when you’re tired, stop when you’re done.", "author": "Unknown", "source": "predefined"},
        {"quote": "Success is the result of preparation, hard work, and learning from failure.", "author": "Unknown", "source": "predefined"},
        {"quote": "The key to success is to focus on goals, not obstacles.", "author": "Unknown", "source": "predefined"},
        {"quote": "You are capable of more than you know.", "author": "Unknown", "source": "predefined"},
        {"quote": "The difference between who you are and who you want to be is what you do.", "author": "Unknown", "source": "predefined"},
        {"quote": "Dream big. Start small. Act now.", "author": "Unknown", "source": "predefined"},
        {"quote": "It's not about perfect. It's about effort.", "author": "Unknown", "source": "predefined"},
        {"quote": "The road to success and the road to failure are almost exactly the same.", "author": "Unknown", "source": "predefined"},
        {"quote": "Push yourself, because no one else is going to do it for you.", "author": "Unknown", "source": "predefined"},
        {"quote": "Work hard in silence, let your success be your noise.", "author": "Unknown", "source": "predefined"},
        {"quote": "Success doesn’t come from what you do occasionally, it comes from what you do consistently.", "author": "Unknown", "source": "predefined"},
        {"quote": "You don’t have to be great to start, but you have to start to be great.", "author": "Zig Ziglar", "source": "predefined"},
        {"quote": "The best way to predict the future is to create it.", "author": "Peter Drucker", "source": "predefined"},
    ]

    # Fetch all user-added quotes from the database
    db_quotes = Motivation.objects.values('quote', 'author')
    db_quotes_with_source = [{"quote": q['quote'], "author": q['author'], "source": "user"} for q in db_quotes]

    # Combine predefined quotes and database quotes
    all_quotes = predefined_quotes + db_quotes_with_source

    # Select and return a random quote
    return random.choice(all_quotes)


@api_view(['GET'])
def motivation_view(request):
    """
    Returns a random motivational quote with metadata (quote, author, source).
    The quote can come from either the predefined list or user-generated quotes.
    """
    quote_data = get_motivation()
    return Response({
        "message": "Your motivational quote",
        "quote": quote_data['quote'],
        "author": quote_data['author'],
        "source": quote_data['source']
    }, status=status.HTTP_200_OK)


# Custom API Views for Advanced Functionality
@api_view(['POST'])
def generate_study_schedule_view(request):
    """
    Generates a personalized study schedule based on user input.
    """
    user = request.user
    available_hours = request.data.get('available_hours')
    exam_dates = request.data.get('exam_dates', None)

    if not available_hours:
        return Response({"error": "Available hours are required."}, status=status.HTTP_400_BAD_REQUEST)

    schedule = generate_study_schedule(user, available_hours, exam_dates)
    return Response(schedule, status=status.HTTP_200_OK)


@api_view(['GET'])
def recommend_study_resources_view(request):
    """
    Recommends study resources based on the subject.
    """
    subject = request.query_params.get('subject')
    if not subject:
        return Response({"error": "Subject is required."}, status=status.HTTP_400_BAD_REQUEST)

    resources = recommend_study_resources(subject)
    return Response(resources, status=status.HTTP_200_OK)


@api_view(['GET'])
def analyze_study_progress_view(request):
    """
    Analyzes and returns study progress for the authenticated user.
    """
    user = request.user
    progress = analyze_study_progress(user)
    return Response(progress, status=status.HTTP_200_OK)


@api_view(['GET'])
def send_exam_alerts_view(request):
    """
    Sends reminders about upcoming exams for the authenticated user.
    """
    user = request.user
    alerts = send_exam_alerts(user)
    return Response(alerts, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_study_tips_view(request):
    """
    Provides study tips based on the subject or difficulty level chosen by the user.
    """
    subject = request.query_params.get('subject')
    difficulty_level = request.query_params.get('difficulty_level', None)

    if not subject:
        return Response({"error": "Subject is required."}, status=status.HTTP_400_BAD_REQUEST)

    tips = get_study_tips(subject, difficulty_level)
    return Response(tips, status=status.HTTP_200_OK)


@api_view(['GET'])
def prioritize_study_tasks_view(request):
    """
    Prioritizes study tasks for the authenticated user.
    """
    user = request.user
    tasks = prioritize_study_tasks(user)
    return Response(tasks, status=status.HTTP_200_OK)


@api_view(['GET'])
def suggest_subjects_view(request):
    """
    Suggests subjects to focus on based on recent performance.
    """
    user = request.user
    suggestions = suggest_subjects(user)
    return Response(suggestions, status=status.HTTP_200_OK)


@api_view(['GET'])
def track_study_sessions_view(request):
    """
    Tracks and summarizes study sessions for the authenticated user.
    """
    user = request.user
    summary = track_study_sessions(user)
    return Response(summary, status=status.HTTP_200_OK)


@api_view(['POST'])
def adjust_study_plan_view(request):
    """
    Adjusts the study plan based on new constraints.
    """
    user = request.user
    reason = request.data.get('reason')
    new_constraints = request.data.get('new_constraints')

    if not reason or not new_constraints:
        return Response({"error": "Reason and new constraints are required."}, status=status.HTTP_400_BAD_REQUEST)

    adjust_study_plan(user, reason, new_constraints)
    return Response({"message": "Study plan adjusted successfully."}, status=status.HTTP_200_OK)


@api_view(['GET'])
def generate_reflection_report_view(request):
    """
    Generates a reflection report for the authenticated user.
    """
    user = request.user
    start_date = request.query_params.get('start_date')
    end_date = request.query_params.get('end_date')

    if not start_date or not end_date:
        return Response({"error": "Start date and end date are required."}, status=status.HTTP_400_BAD_REQUEST)

    report = generate_reflection_report(user, start_date, end_date)
    return Response(report, status=status.HTTP_200_OK)


# Default ViewSets (Unchanged)
class StudyScheduleViewSet(viewsets.ModelViewSet):
    queryset = StudySchedule.objects.all()
    serializer_class = StudyScheduleSerializer


class StudyResourceViewSet(viewsets.ModelViewSet):
    queryset = StudyResource.objects.all()
    serializer_class = StudyResourceSerializer


class StudyBreakTimerViewSet(viewsets.ModelViewSet):
    queryset = StudyBreakTimer.objects.all()
    serializer_class = StudyBreakTimerSerializer


class StudyProgressViewSet(viewsets.ModelViewSet):
    queryset = StudyProgress.objects.all()
    serializer_class = StudyProgressSerializer


class ExamAlertViewSet(viewsets.ModelViewSet):
    queryset = ExamAlert.objects.all()
    serializer_class = ExamAlertSerializer


class StudyTipViewSet(viewsets.ModelViewSet):
    queryset = StudyTip.objects.all()
    serializer_class = StudyTipSerializer


class StudyTaskPriorityViewSet(viewsets.ModelViewSet):
    queryset = StudyTaskPriority.objects.all()
    serializer_class = StudyTaskPrioritySerializer


class SubjectSuggestionViewSet(viewsets.ModelViewSet):
    queryset = SubjectSuggestion.objects.all()
    serializer_class = SubjectSuggestionSerializer


class StudyTrackerViewSet(viewsets.ModelViewSet):
    queryset = StudyTracker.objects.all()
    serializer_class = StudyTrackerSerializer


class StudyNoteViewSet(viewsets.ModelViewSet):
    queryset = StudyNote.objects.all()
    serializer_class = StudyNoteSerializer


class StudyChallengeViewSet(viewsets.ModelViewSet):
    queryset = StudyChallenge.objects.all()
    serializer_class = StudyChallengeSerializer


class StudyPromptViewSet(viewsets.ModelViewSet):
    queryset = StudyPrompt.objects.all()
    serializer_class = StudyPromptSerializer


class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


class StudyReflectionViewSet(viewsets.ModelViewSet):
    queryset = StudyReflection.objects.all()
    serializer_class = StudyReflectionSerializer


class StudyFeedbackViewSet(viewsets.ModelViewSet):
    queryset = StudyFeedback.objects.all()
    serializer_class = StudyFeedbackSerializer


class MotivationViewSet(viewsets.ModelViewSet):
    queryset = Motivation.objects.all()
    serializer_class = MotivationSerializer


class StudyStatisticViewSet(viewsets.ModelViewSet):
    queryset = StudyStatistic.objects.all()
    serializer_class = StudyStatisticSerializer


class CourseGradeViewSet(viewsets.ModelViewSet):
    queryset = CourseGrade.objects.all()
    serializer_class = CourseGradeSerializer


class StudyPlanAdjustmentViewSet(viewsets.ModelViewSet):
    queryset = StudyPlanAdjustment.objects.all()
    serializer_class = StudyPlanAdjustmentSerializer


class StudyReminderViewSet(viewsets.ModelViewSet):
    queryset = StudyReminder.objects.all()
    serializer_class = StudyReminderSerializer