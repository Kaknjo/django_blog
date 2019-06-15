from django.contrib import admin

# Register your models here.

# Importujemo pitanja tako da su vidljiva u admin panelu 

from .models import Question
admin.site.register(Question)
