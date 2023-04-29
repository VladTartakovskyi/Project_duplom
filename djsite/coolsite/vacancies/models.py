from django.db import models
from django.urls import reverse



class Vacancies(models.Model):
    posada = models.CharField(max_length=255, verbose_name="Посада")
    firma = models.CharField(max_length=255, verbose_name="Фірма")
    city = models.CharField(max_length=255, null=True, verbose_name="Місто")
    street = models.CharField(max_length=255, null=True, verbose_name="Вулиця")
    salary = models.IntegerField(verbose_name="Заробітна плата", null=True)
    vumogu = models.TextField(blank=True, verbose_name="Вимоги")
    responsibilities = models.TextField(blank=True, verbose_name="Умови праці")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата опублікування")
    pr = models.ForeignKey('Profession', on_delete=models.PROTECT,  verbose_name="Професії")

    def __str__(self):
        return self.posada

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name = 'Вільні вакансії'
        verbose_name_plural = 'Вільні вакансії'
        ordering = ['-time_create']

class Profession(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Професія')
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return  reverse('profession', kwargs={'pr_id': self.pk})

    class Meta:
        verbose_name = 'Професія'
        verbose_name_plural ='Професія'
        ordering = ['id']

class Unemployed(models.Model):
    priz = models.CharField(max_length=100, verbose_name="Прізвище")
    name = models.CharField(max_length=50, verbose_name="Ім'я")
    pobat = models.CharField(max_length=100, verbose_name="По батькові")
    city = models.CharField(max_length=100, verbose_name="Місто")
    street = models.CharField(max_length=50, verbose_name="Вулиця")
    year = models.IntegerField(verbose_name="Вік")
    nomer_phone = models.CharField(max_length=10, verbose_name="Номер телефону")
    em = models.EmailField(verbose_name="Email", null=True)
    special = models.CharField(max_length=100, verbose_name="Спеціальність")
    vc = models.ForeignKey('Vacancies', on_delete=models.PROTECT, verbose_name="Вакансії", null=True)
    class Meta:
        verbose_name = 'Безробітні'
        verbose_name_plural ='Безробітні'

