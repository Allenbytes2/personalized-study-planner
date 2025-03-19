from datetime import date, timedelta
from django.db.models import Sum, Avg, Count, Q
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

# 1. Generate a Personalized Study Schedule
def generate_study_schedule(user, available_hours, exam_dates=None):
    """
    Generates a personalized study schedule based on exam dates, assignment due dates, and available hours.
    """
    # Fetch upcoming exams and prioritize subjects accordingly
    upcoming_exams = ExamAlert.objects.filter(user=user, exam_date__gte=date.today()).order_by('exam_date')
    tasks = StudyTaskPriority.objects.filter(user=user).order_by('-urgency', '-difficulty')

    schedule = []
    remaining_hours = available_hours

    for exam in upcoming_exams:
        allocated_hours = min(remaining_hours, exam.exam_date - date.today().days * 2)  # Example logic
        schedule.append({
            'subject': exam.subject,
            'exam_date': exam.exam_date,
            'allocated_hours': allocated_hours,
        })
        remaining_hours -= allocated_hours

    return schedule


# 2. Recommend Study Resources
def recommend_study_resources(subject):
    """
    Suggests study resources like books, articles, and videos tailored to the subject.
    """
    resources = StudyResource.objects.filter(subject=subject).order_by('?')[:5]  # Randomly select 5 resources
    return [{'title': res.title, 'url': res.url, 'type': res.resource_type} for res in resources]


# 3. Analyze Study Progress
def analyze_study_progress(user):
    """
    Tracks progress and completion of study sessions, providing insights into completed tasks.
    """
    progress = StudyProgress.objects.filter(user=user, completed=True)
    total_sessions = progress.count()
    total_duration = progress.aggregate(Sum('duration'))['duration__sum'] or 0

    return {
        'total_completed_sessions': total_sessions,
        'total_study_duration_minutes': total_duration,
    }


# 4. Send Exam Alerts (Advanced Filtering)
def send_exam_alerts(user):
    """
    Sends reminders about upcoming exams or assignment deadlines.
    """
    alerts = ExamAlert.objects.filter(user=user, reminder_time__lte=date.today() + timedelta(days=7))
    return [{'subject': alert.subject, 'exam_date': alert.exam_date} for alert in alerts]


# 5. Provide Study Tips (Advanced Filtering)
def get_study_tips(subject, difficulty_level):
    """
    Provides study tips based on the subject or difficulty level chosen by the user.
    """
    tips = StudyTip.objects.filter(Q(subject=subject) | Q(subject='general')).filter(difficulty_level__lte=difficulty_level)
    return [{'tip': tip.tip} for tip in tips]


# 6. Prioritize Study Tasks
def prioritize_study_tasks(user):
    """
    Helps prioritize study tasks based on urgency and difficulty.
    """
    tasks = StudyTaskPriority.objects.filter(user=user).order_by('-urgency', '-difficulty')
    return [{'task': task.task_description, 'urgency': task.urgency, 'difficulty': task.difficulty} for task in tasks]


# 7. Suggest Subjects to Focus On
def suggest_subjects(user):
    """
    Recommends subjects to focus on based on the user’s recent performance or grades.
    """
    recent_grades = CourseGrade.objects.filter(user=user).order_by('-created_at')[:3]
    weak_subjects = [grade.course_name for grade in recent_grades if grade.grade in ['C', 'D', 'F']]
    return weak_subjects


# 8. Track Study Sessions (Advanced Aggregation)
def track_study_sessions(user):
    """
    Logs completed study sessions and tracks total study time for effective time management.
    """
    total_study_time = StudyTracker.objects.filter(user=user).aggregate(Sum('duration'))['duration__sum'] or 0
    most_studied_subject = StudyTracker.objects.filter(user=user).values('subject').annotate(
        total_duration=Sum('duration')
    ).order_by('-total_duration').first()

    return {
        'total_study_time_minutes': total_study_time,
        'most_studied_subject': most_studied_subject['subject'] if most_studied_subject else None,
    }


# 9. Generate Study Statistics
def generate_study_statistics(user):
    """
    Generates insights into the user's study habits, such as total study hours and most studied topics.
    """
    stats = StudyStatistic.objects.filter(user=user).first()
    return {
        'total_study_hours': stats.total_study_hours if stats else 0,
        'most_studied_subject': stats.most_studied_subject if stats else None,
    }


# 10. Adjust Study Plans Dynamically
def adjust_study_plan(user, reason, new_constraints):
    """
    Automatically adjusts study plans based on changes to deadlines, exam dates, or user inputs.
    """
    StudyPlanAdjustment.objects.create(user=user, adjustment_reason=reason, adjusted_date=date.today())
    schedules = StudySchedule.objects.filter(user=user, study_date__gte=date.today())
    for schedule in schedules:
        schedule.study_hours = new_constraints.get('hours', schedule.study_hours)
        schedule.save()


# 11. Generate Reflection Reports
def generate_reflection_report(user, start_date, end_date):
    """
    Lets users reflect on their study sessions, identifying strengths and areas for improvement.
    """
    reflections = StudyReflection.objects.filter(user=user, reflection_date__range=[start_date, end_date])
    feedback = StudyFeedback.objects.filter(user=user, feedback_date__range=[start_date, end_date])

    strengths = [r.strengths for r in reflections]
    areas_for_improvement = [r.areas_for_improvement for r in reflections]
    feedback_text = [f.feedback_text for f in feedback]

    return {
        'strengths': strengths,
        'areas_for_improvement': areas_for_improvement,
        'feedback': feedback_text,
    }