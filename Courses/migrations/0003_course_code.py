# Generated by Django 3.2.5 on 2021-11-27 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0002_auto_20211126_2234'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='code',
            field=models.TextField(null=True),
        ),
    ]