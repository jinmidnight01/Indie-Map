# Generated by Django 4.0.5 on 2022-06-04 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_app', '0009_concert_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='concert',
            name='musician_name',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='concert',
            name='introduce',
            field=models.TextField(null=True),
        ),
    ]
