# Generated by Django 5.1.6 on 2025-03-19 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursegrade',
            name='grade',
            field=models.CharField(max_length=4),
        ),
    ]
