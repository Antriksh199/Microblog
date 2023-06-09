# Generated by Django 4.1.3 on 2023-04-04 08:06

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('User', '0011_remove_userprofile_followers'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='followers',
            field=models.ManyToManyField(blank=True, null=True, related_name='followed_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
