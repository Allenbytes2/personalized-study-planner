from rest_framework import serializers
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

class StudyScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudySchedule
        fields = '__all__'

class StudyResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyResource
        fields = '__all__'

class StudyBreakTimerSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyBreakTimer
        fields = '__all__'

class StudyProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyProgress
        fields = '__all__'

class ExamAlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamAlert
        fields = '__all__'

class StudyTipSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyTip
        fields = '__all__'

class StudyTaskPrioritySerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyTaskPriority
        fields = '__all__'

class SubjectSuggestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectSuggestion
        fields = '__all__'

class StudyTrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyTracker
        fields = '__all__'

class StudyNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyNote
        fields = '__all__'

class StudyChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyChallenge
        fields = '__all__'

class StudyPromptSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyPrompt
        fields = '__all__'

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'

class StudyReflectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyReflection
        fields = '__all__'

class StudyFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyFeedback
        fields = '__all__'

class MotivationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motivation
        fields = '__all__'

class StudyStatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyStatistic
        fields = '__all__'

class CourseGradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseGrade
        fields = '__all__'

class StudyPlanAdjustmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyPlanAdjustment
        fields = '__all__'

class StudyReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyReminder
        fields = '__all__'