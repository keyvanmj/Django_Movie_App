# Generated by Django 3.2.7 on 2021-12-28 07:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Vote_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rate',
            name='ip_address',
        ),
    ]
