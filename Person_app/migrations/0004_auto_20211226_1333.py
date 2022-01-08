# Generated by Django 3.2.7 on 2021-12-26 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Person_app', '0003_auto_20211226_1330'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='role',
        ),
        migrations.AddField(
            model_name='person',
            name='role',
            field=models.CharField(choices=[('CAST', 'cast'), ('DIRECTOR', 'director'), ('CREATOR', 'creator')], default='cast', max_length=140),
        ),
    ]
