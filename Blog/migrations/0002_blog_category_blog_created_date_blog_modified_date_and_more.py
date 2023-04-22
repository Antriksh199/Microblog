# Generated by Django 4.1.3 on 2023-03-14 13:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='blog',
            name='created_date',
            field=models.DateField(blank=True, default=datetime.date(2023, 3, 14)),
        ),
        migrations.AddField(
            model_name='blog',
            name='modified_date',
            field=models.DateField(blank=True, default=datetime.date(2023, 3, 14)),
        ),
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=models.CharField(blank=True, help_text='Maximum 250 characters allowed.', max_length=250),
        ),
    ]