# Generated by Django 4.1.3 on 2023-04-03 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0008_remove_userprofile_followers_userprofile_followers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='followed_by', to='User.userprofile'),
        ),
    ]
