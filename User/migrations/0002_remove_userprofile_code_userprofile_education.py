# Generated by Django 4.1.3 on 2022-12-22 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='code',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='education',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
