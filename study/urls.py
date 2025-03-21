from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import *

router = DefaultRouter()
router.register(r'tasks', StudyTaskViewSet)
router.register(r'subjects-lessons', SubjectLessonViewSet)
router.register(r'subjects-diary', SubjectDiaryViewSet)
router.register(r'study-schedule', StudyScheduleViewSet)
router.register(r'study-resources', StudyResourceViewSet)
router.register(r'study-break', StudyBreakTimerViewSet)
router.register(r'study-progress', StudyProgressViewSet)
router.register(r'notes', StudyNoteViewSet)
router.register(r'study-challenges', StudyChallengeViewSet)
router.register(r'study/quiz', QuizViewSet)
router.register(r'study-prompt', StudyPromptViewSet)
router.register(r'study-reflection', StudyReflectionViewSet)
router.register(r'course-grades', CourseGradeViewSet)

urlpatterns = [
    # JWT Authentication
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Custom Advanced Functionality Routes
    path('generate-study-schedule/<int:study_schedule_id>/<int:timer_id>/', generate_study_schedule_view, name='generate_study_schedule'),
    path('study-resources-recommendations/<str:resource_type>/', recommend_study_resources_view, name='recommend_study_resources'),
    path('generate-study-statistics/', generate_study_statistics_view, name='generate_study_statistics'),
    path('add-exam-to-calendar/', AddExamToCalendarView.as_view(), name='add_exam_to_calendar'),
    path('send-study-notes/', SendStudyNotesView.as_view(), name='send_study_notes'),
    path('motivation/', MotivationView.as_view(), name='motivation'),
    path('resources/quiz/', fetch_quiz_questions_view, name='resources_quiz'),

    # OAuth Flow
    path('oauth/redirect/', oauth_redirect, name='oauth_redirect'),
    path('oauth/callback/', oauth_callback, name='oauth_callback'),

    # Default API routes
    path('', include(router.urls)),
]