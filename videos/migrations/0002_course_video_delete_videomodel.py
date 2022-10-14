# Generated by Django 4.0.5 on 2022-09-28 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('courseImage', models.ImageField(blank=True, upload_to='courses/')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('videoLink', models.CharField(max_length=500)),
                ('lessonNo', models.FloatField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videos.course')),
            ],
        ),
        migrations.DeleteModel(
            name='VideoModel',
        ),
    ]
