# Generated by Django 4.1.2 on 2022-11-07 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0002_remove_profession_slug_remove_vacancies_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='unemployed',
            name='vc',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='vacancies.vacancies', verbose_name='Вакансії'),
        ),
    ]