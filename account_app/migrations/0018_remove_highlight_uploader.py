# Generated by Django 4.0.4 on 2022-06-05 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account_app', '0017_remove_user_highlight_highlight'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='highlight',
            name='uploader',
        ),
    ]
