# Generated by Django 3.2.7 on 2021-12-25 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User_IP', '0001_initial'),
        ('Stats_app', '0001_initial'),
        ('Series_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='series_hits',
            field=models.ManyToManyField(blank=True, related_name='series_hits', through='Stats_app.HitModel', to='User_IP.IPAddress'),
        ),
    ]
