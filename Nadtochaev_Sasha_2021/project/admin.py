from django.contrib import admin
from .models import Project # из папки project/models импортируется модель Project

# Register your models here.

admin.site.register(Project) # Регистрация модели Project в админке, чтобы к данной моделе был доступ через админ панель