from django.apps import AppConfig


class BlogConfig(AppConfig): # Класс для управления приложением Blog
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
