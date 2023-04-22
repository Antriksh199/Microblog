# Generated by Django 4.1.3 on 2023-04-04 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0012_userprofile_followers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='followers',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='follows',
            field=models.ManyToManyField(blank=True, null=True, related_name='followed_by', to='User.userprofile'),
        ),
    ]