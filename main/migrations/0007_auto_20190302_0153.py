# Generated by Django 2.1.7 on 2019-03-02 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_job_job_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_minimum_qual',
            field=models.TextField(default='None'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='job_prefered_qual',
            field=models.TextField(default='None'),
            preserve_default=False,
        ),
    ]
