# Generated by Django 3.2.13 on 2022-06-07 18:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('fileShareApp', '0002_alter_upload_file_upload_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='upload',
            old_name='download_couont',
            new_name='download_count',
        ),
        migrations.AlterField(
            model_name='upload',
            name='file_upload_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 7, 18, 34, 24, 746147, tzinfo=utc), verbose_name='上传时间'),
        ),
    ]
