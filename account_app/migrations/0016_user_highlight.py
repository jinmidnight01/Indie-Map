# Generated by Django 4.0.4 on 2022-06-05 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_app', '0015_merge_20220605_2339'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='highlight',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]