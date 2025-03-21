# Generated by Django 5.1.6 on 2025-03-20 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0005_alter_coursegrade_grade_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudyTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.TextField()),
                ('status', models.BooleanField(default=False)),
                ('goal_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubjectDiary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('note', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubjectLesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('lesson', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='ExamAlert',
        ),
        migrations.DeleteModel(
            name='Motivation',
        ),
        migrations.DeleteModel(
            name='StudyFeedback',
        ),
        migrations.DeleteModel(
            name='StudyPlanAdjustment',
        ),
        migrations.DeleteModel(
            name='StudyReminder',
        ),
        migrations.DeleteModel(
            name='StudyStatistic',
        ),
        migrations.DeleteModel(
            name='StudyTaskPriority',
        ),
        migrations.DeleteModel(
            name='StudyTip',
        ),
        migrations.DeleteModel(
            name='StudyTracker',
        ),
        migrations.DeleteModel(
            name='SubjectSuggestion',
        ),
    ]
