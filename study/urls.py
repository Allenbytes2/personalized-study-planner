from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
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
    generate_study_schedule_view,
    recommend_study_resources_view,
    analyze_study_progress_view,
    send_exam_alerts_view,
    get_study_tips_view,
    prioritize_study_tasks_view,
    suggest_subjects_view,
    track_study_sessions_view,
    adjust_study_plan_view,
    generate_reflection_report_view,
    motivation_view,
)

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

urlpatterns = [
    # Default API routes
    path('api/', include(router.urls)),
    path('', include(router.urls)),

    # JWT Authentication
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Custom Advanced Functionality Routes
    path('api/study-schedule/generate/', generate_study_schedule_view, name='generate_study_schedule'),
    path('api/study-resources/recommendations/', recommend_study_resources_view, name='recommend_study_resources'),
    path('api/study-progress/analyze/', analyze_study_progress_view, name='analyze_study_progress'),
    path('api/exam/alerts/upcoming/', send_exam_alerts_view, name='send_exam_alerts'),
    path('api/study-tips/get/', get_study_tips_view, name='get_study_tips'),
    path('api/study-planner/priority/tasks/', prioritize_study_tasks_view, name='prioritize_study_tasks'),
    path('api/subject/suggestions/focus/', suggest_subjects_view, name='suggest_subjects'),
    path('api/study-tracker/summary/', track_study_sessions_view, name='track_study_sessions'),
    path('api/study-plan/adjust/', adjust_study_plan_view, name='adjust_study_plan'),
    path('api/study-reflection/report/', generate_reflection_report_view, name='generate_reflection_report'),

    # Motivation Random Quote Endpoint
    path('api/motivation/random/', motivation_view, name='random_motivational_quote'),
]
