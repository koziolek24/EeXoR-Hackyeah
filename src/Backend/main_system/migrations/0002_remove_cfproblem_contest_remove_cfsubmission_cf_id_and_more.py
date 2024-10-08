# Generated by Django 5.1.1 on 2024-09-28 19:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_system', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cfproblem',
            name='contest',
        ),
        migrations.RemoveField(
            model_name='cfsubmission',
            name='cf_id',
        ),
        migrations.RemoveField(
            model_name='cfsubmission',
            name='contest',
        ),
        migrations.RemoveField(
            model_name='cfsubmission',
            name='creation_time',
        ),
        migrations.AddField(
            model_name='cfsubmission',
            name='accept_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cfsubmission',
            name='submit_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 28, 19, 59, 35, 756595, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cfproblem',
            name='points',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='cfproblem',
            name='rating',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='cfsubmission',
            name='verdict',
            field=models.BooleanField(default=False),
        ),
    ]
