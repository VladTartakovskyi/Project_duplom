# Generated by Django 4.1.2 on 2022-11-08 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0004_unemployed_us'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unemployed',
            name='us',
        ),
    ]
