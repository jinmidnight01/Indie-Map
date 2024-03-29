# Generated by Django 4.0.4 on 2022-06-05 08:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account_app', '0011_remove_concert_musician_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback_content', models.CharField(max_length=200)),
                ('feedback_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('feedback_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('feedback_post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
