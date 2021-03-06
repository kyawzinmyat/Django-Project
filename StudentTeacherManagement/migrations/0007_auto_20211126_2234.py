# Generated by Django 3.2.5 on 2021-11-26 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0002_auto_20211126_2234'),
        ('StudentTeacherManagement', '0006_student_num_of_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='courses',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Courses.course'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='courses',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='Courses.course'),
        ),
    ]
