from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
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

# Study Schedule ViewSet
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