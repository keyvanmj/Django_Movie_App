# Generated by Django 3.2.7 on 2021-12-30 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Series_app', '0007_series_release_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='imdb_link',
            field=models.URLField(blank=True, max_length=300, null=True),
        ),
    ]
