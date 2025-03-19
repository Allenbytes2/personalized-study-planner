from rest_framework import serializers
from django.contrib.auth.models import User
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

class UserField(serializers.PrimaryKeyRelatedField):
    def __init__(self, **kwargs):
        # Set the queryset to all User objects
        kwargs['queryset'] = User.objects.all()
        super().__init__(**kwargs)

    def to_internal_value(self, data):
        # Allow string input (username) and convert it to a User object
        if isinstance(data, str):
            try:
                user = User.objects.get(username=data)
                return user
            except User.DoesNotExist:
                raise serializers.ValidationError({"user": "User  with this username does not exist."})
        return super().to_internal_value(data)
class StudyScheduleSerializer(serializers.ModelSerializer):
    user = UserField()
    class Meta:
        model = StudySchedule
        fields = '__all__'

class StudyResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyResource
        fields = '__all__'

class StudyBreakTimerSerializer(serializers.ModelSerializer):
    user = UserField()
    class Meta:
        model = StudyBreakTimer
        fields = '__all__'

class StudyProgressSerializer(serializers.ModelSerializer):
    user = UserField()
    class Meta:
        model = StudyProgress
        fields = '__all__'

class ExamAlertSerializer(serializers.ModelSerializer):
    user = UserField()
    class Meta:
        model = ExamAlert
        fields = '__all__'

class StudyTipSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyTip
        fields = '__all__'

class StudyTaskPrioritySerializer(serializers.ModelSerializer):
    user = UserField()
    class Meta:
        model = StudyTaskPriority
        fields = '__all__'

class SubjectSuggestionSerializer(serializers.ModelSerializer):
    user = UserField()
    class Meta:
        model = SubjectSuggestion
        fields = '__all__'

class StudyTrackerSerializer(serializers.ModelSerializer):
    user = UserField()
    class Meta:
        model = StudyTracker
        fields = '__all__'

class StudyNoteSerializer(serializers.ModelSerializer):
    user = UserField()
    class Meta:
        model = StudyNote
        fields = '__all__'

class StudyChallengeSerializer(serializers.ModelSerializer):
    user = UserField()
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
    user = UserField()
    class Meta:
        model = StudyReflection
        fields = '__all__'

class StudyFeedbackSerializer(serializers.ModelSerializer):
    user = UserField()
    class Meta:
        model = StudyFeedback
        fields = '__all__'

class MotivationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motivation
        fields = '__all__'

class StudyStatisticSerializer(serializers.ModelSerializer):
    user = UserField()
    class Meta:
        model = StudyStatistic
        fields = '__all__'

class CourseGradeSerializer(serializers.ModelSerializer):
    user = UserField()
    class Meta:
        model = CourseGrade
        fields = '__all__'

class StudyPlanAdjustmentSerializer(serializers.ModelSerializer):
    user = UserField()
    class Meta:
        model = StudyPlanAdjustment
        fields = '__all__'

class StudyReminderSerializer(serializers.ModelSerializer):
    user = UserField()
    class Meta:
        model = StudyReminder
        fields = '__all__'