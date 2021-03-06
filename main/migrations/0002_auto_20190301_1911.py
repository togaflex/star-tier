# Generated by Django 2.1.7 on 2019-03-01 19:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_closed',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date job will be closed'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='job_status',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
