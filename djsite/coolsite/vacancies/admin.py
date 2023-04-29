from django.contrib import admin

# Register your models here.

from .models import *



class VacanciesAdmin(admin.ModelAdmin):
    list_display = ('id', 'posada', 'firma', 'city', 'street', 'vumogu', 'responsibilities', 'time_create', 'pr')
    list_display_links = ('id', 'posada')
    search_fields = ('posada', 'city')


class ProfessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name', )

class UnemployedAdmin(admin.ModelAdmin):
    list_display = ('id', 'priz', 'name', 'pobat', 'city', 'street', 'year', 'nomer_phone', 'special')
    list_display_links = ('id', 'priz')
    search_fields = ('priz', )

admin.site.register(Vacancies, VacanciesAdmin)
admin.site.register(Profession, ProfessionAdmin)
admin.site.register(Unemployed, UnemployedAdmin)