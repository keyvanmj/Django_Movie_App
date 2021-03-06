# Generated by Django 3.2.7 on 2021-12-25 13:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('User_IP', '__first__'),
        ('Series_app', '__first__'),
        ('Movie_app', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Favourite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
                ('ip_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='User_IP.ipaddress')),
                ('movies', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Movie_app.movie')),
                ('series', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Series_app.series')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
