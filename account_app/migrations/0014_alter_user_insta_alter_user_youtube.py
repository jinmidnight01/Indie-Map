# Generated by Django 4.0.5 on 2022-06-05 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_app', '0013_feedback_feedback_name_feedback_feedback_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='insta',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='youtube',
            field=models.URLField(null=True),
        ),
    ]
