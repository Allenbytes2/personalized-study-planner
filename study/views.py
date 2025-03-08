from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import random
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


def get_motivation():
    quotes = [
        "The harder you work for something, the greater you'll feel when you achieve it.",
        "Don't watch the clock; do what it does. Keep going.",
        "Success is the sum of small efforts, repeated day in and day out.",
        "The future depends on what you do today.",
        "Believe you can and you're halfway there.",
        "What you get by achieving your goals is not as important as what you become by achieving your goals.",
        "Education is the most powerful weapon which you can use to change the world.",
        "Don’t stop when you’re tired, stop when you’re done.",
        "Success is the result of preparation, hard work, and learning from failure.",
        "The key to success is to focus on goals, not obstacles.",
        "You are capable of more than you know.",
        "The difference between who you are and who you want to be is what you do.",
        "Dream big. Start small. Act now.",
        "It's not about perfect. It's about effort.",
        "The road to success and the road to failure are almost exactly the same.",
        "Push yourself, because no one else is going to do it for you.",
        "Work hard in silence, let your success be your noise.",
        "Success doesn’t come from what you do occasionally, it comes from what you do consistently.",
        "You don’t have to be great to start, but you have to start to be great.",
        "The best way to predict the future is to create it."
    ]

    return random.choice(quotes)

@api_view(['GET'])
def motivation_view(request):
    quote = get_motivation()

    return Response({
        "message": "Your motivational quote",
        "quote": quote
    }, status=status.HTTP_200_OK)
class StudyScheduleViewSet(viewsets.ModelViewSet):
    queryset = StudySchedule.objects.all()
    serializer_class = StudyScheduleSerializer

# Study Resource ViewSet
class StudyResourceViewSet(viewsets.ModelViewSet):
    queryset = StudyResource.objects.all()
    serializer_class = StudyResourceSerializer

# Study Break Timer ViewSet
class StudyBreakTimerViewSet(viewsets.ModelViewSet):
    queryset = StudyBreakTimer.objects.all()
    serializer_class = StudyBreakTimerSerializer

# Study Progress ViewSet
class StudyProgressViewSet(viewsets.ModelViewSet):
    queryset = StudyProgress.objects.all()
    serializer_class = StudyProgressSerializer

# Exam Alert ViewSet
class ExamAlertViewSet(viewsets.ModelViewSet):
    queryset = ExamAlert.objects.all()
    serializer_class = ExamAlertSerializer

# Study Tip ViewSet
class StudyTipViewSet(viewsets.ModelViewSet):
    queryset = StudyTip.objects.all()
    serializer_class = StudyTipSerializer

# Study Task Priority ViewSet
class StudyTaskPriorityViewSet(viewsets.ModelViewSet):
    queryset = StudyTaskPriority.objects.all()
    serializer_class = StudyTaskPrioritySerializer

# Subject Suggestion ViewSet
class SubjectSuggestionViewSet(viewsets.ModelViewSet):
    queryset = SubjectSuggestion.objects.all()
    serializer_class = SubjectSuggestionSerializer

# Study Tracker ViewSet
class StudyTrackerViewSet(viewsets.ModelViewSet):
    queryset = StudyTracker.objects.all()
    serializer_class = StudyTrackerSerializer

# Study Note ViewSet
class StudyNoteViewSet(viewsets.ModelViewSet):
    queryset = StudyNote.objects.all()
    serializer_class = StudyNoteSerializer

# Study Challenge ViewSet
class StudyChallengeViewSet(viewsets.ModelViewSet):
    queryset = StudyChallenge.objects.all()
    serializer_class = StudyChallengeSerializer

# Study Prompt ViewSet
class StudyPromptViewSet(viewsets.ModelViewSet):
    queryset = StudyPrompt.objects.all()
    serializer_class = StudyPromptSerializer

# Quiz ViewSet
class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

# Study Reflection ViewSet
class StudyReflectionViewSet(viewsets.ModelViewSet):
    queryset = StudyReflection.objects.all()
    serializer_class = StudyReflectionSerializer

# Study Feedback ViewSet
class StudyFeedbackViewSet(viewsets.ModelViewSet):
    queryset = StudyFeedback.objects.all()
    serializer_class = StudyFeedbackSerializer

# Motivation ViewSet
class MotivationViewSet(viewsets.ModelViewSet):
    queryset = Motivation.objects.all()
    serializer_class = MotivationSerializer

# Study Statistic ViewSet
class StudyStatisticViewSet(viewsets.ModelViewSet):
    queryset = StudyStatistic.objects.all()
    serializer_class = StudyStatisticSerializer

# Course Grade ViewSet
class CourseGradeViewSet(viewsets.ModelViewSet):
    queryset = CourseGrade.objects.all()
    serializer_class = CourseGradeSerializer

# Study Plan Adjustment ViewSet
class StudyPlanAdjustmentViewSet(viewsets.ModelViewSet):
    queryset = StudyPlanAdjustment.objects.all()
    serializer_class = StudyPlanAdjustmentSerializer

# Study Reminder ViewSet
class StudyReminderViewSet(viewsets.ModelViewSet):
    queryset = StudyReminder.objects.all()
    serializer_class = StudyReminderSerializer