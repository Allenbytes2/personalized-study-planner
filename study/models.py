from django.db import models
from django.contrib.auth.models import User

# Endpoint 1: /tasks
class StudyTask(models.Model):
    task = models.TextField()
    status = models.BooleanField(default=False)
    goal_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Task: {self.task[:50]} (Due: {self.goal_date})"

# Endpoint 2: /subjects-lessons
class SubjectLesson(models.Model):
    subject = models.CharField(max_length=100)
    lesson = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Lesson for {self.subject}: {self.lesson[:50]}"

# Endpoint 3: /subjects-diary
class SubjectDiary(models.Model):
    subject = models.CharField(max_length=100)
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Diary entry for {self.subject}: {self.note[:50]}"

# Endpoint 4: /study-schedule
class StudySchedule(models.Model):
    study_date = models.DateField()
    study_hours = models.FloatField()
    subjects = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Schedule for {self.user.username} on {self.study_date}"

# Endpoint 5: /study-resources
class StudyResource(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()
    subject = models.CharField(max_length=100)
    resource_type = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

# Endpoint 6: /study-break
class StudyBreakTimer(models.Model):
    study_duration = models.IntegerField()
    break_duration = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Timer for {self.user.username}"

# Endpoint 7: /study-progress
class StudyProgress(models.Model):
    study_session_date = models.DateField()
    subject = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    study_hours = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Progress for {self.user.username} on {self.study_session_date}"

# Endpoint 8: /study-challenges
class StudyChallenge(models.Model):
    challenge_description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Challenge for {self.user.username}"

# Endpoint 9: /study/quiz
class Quiz(models.Model):
    subject = models.CharField(max_length=100)
    quiz_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Quiz for {self.subject}"

# Endpoint 10: /study-prompt
class StudyPrompt(models.Model):
    subject = models.CharField(max_length=100)
    prompt = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Prompt for {self.subject}"

# Endpoint 11: /resources/quiz (standalone - no model needed)
# [Placeholder: This endpoint fetches external data and requires no model]

# Endpoint 12: /study-reflection
class StudyReflection(models.Model):
    reflection_date = models.DateField()
    strengths = models.TextField()
    areas_for_improvement = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Reflection for {self.user.username} on {self.reflection_date}"

# Endpoint 13: /course/grades
class CourseGrade(models.Model):
    course_name = models.CharField(max_length=100)
    grade = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Grade for {self.user.username} in {self.course_name}"

# Endpoint 14: /notes
class StudyNote(models.Model):
    subject = models.CharField(max_length=100)
    note_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Note for {self.user.username} on {self.subject}"

# Endpoints 15-20 are STANDALONE and require NO models:
# 15. /send-study-notes → Integrates with Gmail API
# 16. /motivation → Fetches from external quote API
# 17. /study-resources/recommendations → External resource API
# 18. /add-exam-to-calendar → Google Calendar integration
# 19. /generate-study-statistics → Aggregates data from StudyProgress/CourseGrade
# 20. /generate-study-schedule → Uses StudySchedule + StudyBreakTimer data