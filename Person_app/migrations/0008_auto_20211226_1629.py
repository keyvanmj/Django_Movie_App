# Generated by Django 3.2.7 on 2021-12-26 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Person_app', '0007_person_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ('title',)},
        ),
        migrations.RenameField(
            model_name='person',
            old_name='full_name',
            new_name='title',
        ),
    ]
