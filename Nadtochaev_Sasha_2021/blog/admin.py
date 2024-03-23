from django.contrib import admin
from .models import Category, Post, Comment # Импорт необходимые нам модели из файла models приложения blog
# Register your models here.

admin.site.register(Category) # Регистрируем модель Category для отображения её в админ панели
admin.site.register(Post) # Регистрируем модель Post для отображения её в админ панели
admin.site.register(Comment) # Регистрируем модель Comment для отображения её в админ панели