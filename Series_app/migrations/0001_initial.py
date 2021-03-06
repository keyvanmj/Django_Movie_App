# Generated by Django 3.2.7 on 2021-12-25 13:15

import Series_app.models
from django.db import migrations, models
import django.db.models.deletion
import embed_video.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Movie_Category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('description', models.TextField(max_length=10000)),
                ('image', models.ImageField(blank=True, null=True, upload_to='series')),
                ('series_background_image', models.ImageField(blank=True, null=True, upload_to='series/background')),
                ('screen_shot', models.ImageField(blank=True, null=True, upload_to='series/screenshot')),
                ('series_slug', models.SlugField(blank=True, max_length=100)),
                ('series_length', models.CharField(max_length=50)),
                ('release_date', models.CharField(blank=True, max_length=100, null=True)),
                ('trailer', embed_video.fields.EmbedVideoField(blank=True, null=True)),
                ('series_rate', models.CharField(blank=True, max_length=100, null=True)),
                ('imdb_rate', models.CharField(blank=True, max_length=100, null=True)),
                ('language', models.CharField(blank=True, max_length=100, null=True)),
                ('quality', models.CharField(blank=True, max_length=100, null=True)),
                ('size', models.CharField(blank=True, max_length=100, null=True)),
                ('subtitle', models.CharField(blank=True, max_length=100, null=True)),
                ('subscription', models.CharField(blank=True, max_length=700, null=True)),
                ('types', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('seasons', models.CharField(max_length=1000)),
                ('genre', models.ManyToManyField(blank=True, to='Movie_Category.Genre')),
            ],
            options={
                'verbose_name_plural': 'Series',
            },
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('selected_season', models.PositiveIntegerField(blank=True, null=True)),
                ('episode', models.PositiveIntegerField(blank=True, null=True)),
                ('series', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Series_app.series')),
                ('image', models.ImageField(blank=True, null=True, upload_to=Series_app.models.season_directory_path_with_uuid)),
                ('trailer', models.CharField(blank=True, max_length=5000, null=True)),
                ('link1', models.CharField(blank=True, max_length=5000, null=True)),
                ('link2', models.CharField(blank=True, max_length=5000, null=True)),
                ('link3', models.CharField(blank=True, max_length=5000, null=True)),
                ('online_link', models.CharField(blank=True, max_length=5000, null=True)),
                ('id', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
