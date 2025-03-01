from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    StudyScheduleViewSet,
    StudyResourceViewSet,
    StudyBreakTimerViewSet,
    StudyProgressViewSet,
    ExamAlertViewSet,
    StudyTipViewSet,
    StudyTaskPriorityViewSet,
    SubjectSuggestionViewSet,
    StudyTrackerViewSet,
    StudyNoteViewSet,
    StudyChallengeViewSet,
    StudyPromptViewSet,
    QuizViewSet,
    StudyReflectionViewSet,
    StudyFeedbackViewSet,
    MotivationViewSet,
    StudyStatisticViewSet,
    CourseGradeViewSet,
    StudyPlanAdjustmentViewSet,
    StudyReminderViewSet,
)

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'study-schedule', StudyScheduleViewSet)
router.register(r'study-resources', StudyResourceViewSet)
router.register(r'study-break', StudyBreakTimerViewSet)
router.register(r'study-progress', StudyProgressViewSet)
router.register(r'exam/alerts', ExamAlertViewSet)
router.register(r'study-tips', StudyTipViewSet)
router.register(r'study-planner/priority', StudyTaskPriorityViewSet)
router.register(r'subject/suggestions', SubjectSuggestionViewSet)
router.register(r'study-tracker', StudyTrackerViewSet)
router.register(r'notes/share', StudyNoteViewSet)
router.register(r'study-challenges', StudyChallengeViewSet)
router.register(r'study-prompt', StudyPromptViewSet)
router.register(r'resources/quiz', QuizViewSet)
router.register(r'study-reflection', StudyReflectionViewSet)
router.register(r'study-feedback', StudyFeedbackViewSet)
router.register(r'motivation', MotivationViewSet)
router.register(r'study-statistics', StudyStatisticViewSet)
router.register(r'course/grades', CourseGradeViewSet)
router.register(r'study-plan/adjust', StudyPlanAdjustmentViewSet)
router.register(r'study-reminder/notifications', StudyReminderViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]