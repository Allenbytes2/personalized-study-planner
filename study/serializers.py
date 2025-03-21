from rest_framework import serializers
from .models import *

# Endpoint 1: /tasks
class StudyTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyTask
        fields = ['id', 'task', 'status', 'goal_date', 'created_at']

# Endpoint 2: /subjects-lessons
class SubjectLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectLesson
        fields = ['id', 'subject', 'lesson', 'created_at']

# Endpoint 3: /subjects-diary
class SubjectDiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectDiary
        fields = ['id', 'subject', 'note', 'created_at']

# Endpoint 4: /study-schedule
class StudyScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudySchedule
        fields = ['id', 'study_date', 'study_hours', 'subjects', 'created_at']

# Endpoint 5: /study-resources
class StudyResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyResource
        fields = ['id', 'title', 'url', 'subject', 'resource_type', 'created_at']

# Endpoint 6: /study-break
class StudyBreakTimerSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyBreakTimer
        fields = ['id', 'study_duration', 'break_duration', 'created_at']

# Endpoint 7: /study-progress
class StudyProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyProgress
        fields = ['id', 'study_session_date', 'subject', 'completed', 'study_hours', 'created_at']

# Endpoint 8: /study-challenges
class StudyChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyChallenge
        fields = ['id', 'challenge_description', 'start_date', 'end_date', 'created_at']

# Endpoint 9: /study/quiz
class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ['id', 'subject', 'quiz_content', 'created_at']

# Endpoint 10: /study-prompt
class StudyPromptSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyPrompt
        fields = ['id', 'subject', 'prompt', 'created_at']

# Endpoint 11: /resources/quiz (standalone - no serializer needed)
# [Placeholder: This endpoint fetches external data and requires no serializer]

# Endpoint 12: /study-reflection
class StudyReflectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyReflection
        fields = ['id', 'reflection_date', 'strengths', 'areas_for_improvement', 'created_at']

# Endpoint 13: /course/grades
class CourseGradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseGrade
        fields = ['id', 'course_name', 'grade', 'created_at']

# Endpoint 14: /notes
class StudyNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyNote
        fields = ['id', 'subject', 'note_content', 'created_at']

# Endpoints 15-20 are STANDALONE and require NO serializers:
# 15. /send-study-notes → Integrates with Gmail API
# 16. /motivation → Fetches from external quote API
# 17. /study-resources/recommendations → External resource API
# 18. /add-exam-to-calendar → Google Calendar integration
# 19. /generate-study-statistics → Aggregates data from StudyProgress/CourseGrade
# 20. /generate-study-schedule → Uses StudySchedule + StudyBreakTimer data