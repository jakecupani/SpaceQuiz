# Generated by Django 3.1.3 on 2020-12-09 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0006_quiz_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
