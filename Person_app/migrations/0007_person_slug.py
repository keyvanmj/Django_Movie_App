# Generated by Django 3.2.7 on 2021-12-26 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Person_app', '0006_delete_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='slug',
            field=models.SlugField(blank=True, max_length=140, null=True),
        ),
    ]