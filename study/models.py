from django.db import models
from django.contrib.auth.models import User

class StudySchedule(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    study_date = models.DateField()
    study_hours = models.IntegerField()  # Number of hours planned for study
    subjects = models.TextField()  # Comma-separated list of subjects
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Schedule for {self.user.username} on {self.study_date}"

class StudyResource(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()
    subject = models.CharField(max_length=100)
    resource_type = models.CharField(max_length=50)  # e.g., 'book', 'video', 'article'
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class StudyBreakTimer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    study_duration = models.IntegerField()  # Duration in minutes
    break_duration = models.IntegerField()  # Duration in minutes
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Timer for {self.user.username}"

class StudyProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    study_session_date = models.DateField()
    subject = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    duration = models.IntegerField()  # Duration in minutes
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Progress for {self.user.username} on {self.study_session_date}"

class ExamAlert(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exam_date = models.DateField()
    subject = models.CharField(max_length=100)
    reminder_time = models.DateTimeField()  # When to send the reminder
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Exam alert for {self.user.username} on {self.exam_date}"

class StudyTip(models.Model):
    subject = models.CharField(max_length=100)
    tip = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Tip for {self.subject}"

class StudyTaskPriority(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_description = models.TextField()
    urgency = models.IntegerField()  # Scale of 1-10
    difficulty = models.IntegerField()  # Scale of 1-10
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Task priority for {self.user.username}"

class SubjectSuggestion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    suggested_subject = models.CharField(max_length=100)
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Suggestion for {self.user.username}: {self.suggested_subject}"

class StudyTracker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    study_session_date = models.DateField()
    subject = models.CharField(max_length=100)
    duration = models.IntegerField()  # Duration in minutes
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Tracker for {self.user.username} on {self.study_session_date}"

class StudyNote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    note_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Note for {self.user.username} on {self.subject}"

class StudyChallenge(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    challenge_description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Challenge for {self.user.username}"

class StudyPrompt(models.Model):
    subject = models.CharField(max_length=100)
    prompt = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prompt for {self.subject}"

class Quiz(models.Model):
    subject = models.CharField(max_length=100)
    quiz_content = models.TextField()  # Could be JSON or text format
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Quiz for {self.subject}"

class StudyReflection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reflection_date = models.DateField()
    strengths = models.TextField()
    areas_for_improvement = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reflection for {self.user.username} on {self.reflection_date}"

class StudyFeedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    feedback_date = models.DateField()
    feedback_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.user.username} on {self.feedback_date}"

class Motivation(models.Model):
    quote = models.TextField()
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Motivation quote by {self.author}"

class StudyStatistic(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_study_hours = models.FloatField(default=0.0)
    most_studied_subject = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Statistics for {self.user.username}"

class CourseGrade(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=100)
    grade = models.CharField(max_length=4)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Grade for {self.user.username} in {self.course_name}"

class StudyPlanAdjustment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    adjustment_reason = models.TextField()
    adjusted_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Adjustment for {self.user.username} on {self.adjusted_date}"

class StudyReminder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reminder_date = models.DateField()
    reminder_time = models.TimeField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reminder for {self.user.username} on {self.reminder_date}"