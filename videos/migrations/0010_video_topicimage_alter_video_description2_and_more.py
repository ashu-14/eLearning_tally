# Generated by Django 4.0.5 on 2022-09-29 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0009_video_description2'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='topicImage',
            field=models.ImageField(blank=True, upload_to='topics/'),
        ),
        migrations.AlterField(
            model_name='video',
            name='description2',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='videoLink',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]