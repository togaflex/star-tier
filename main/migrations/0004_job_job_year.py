# Generated by Django 2.1.7 on 2019-03-02 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_job_job_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_year',
            field=models.TextField(default='NA'),
            preserve_default=False,
        ),
    ]