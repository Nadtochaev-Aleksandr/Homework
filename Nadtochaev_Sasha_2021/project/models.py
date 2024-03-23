from django.db import models

# Create your models here.
class Project(models.Model): # создание модели Project на основе класса models.Model
    title=models.CharField(max_length=100) # создание поля title модели - на основе класса CharField - обычный однострочный текст. Данному полю присвоен аргумент max_length=100, указывающий что данное поле может состоять из максимум 100 символов
    description = models.TextField() # создание поля description, но основе класса models.TextField - многострочный текст
    technology = models.CharField(max_length=50) # создание поля technology модели - на основе класса CharField - обычный однострочный текст. Данному полю присвоен аргумент max_length=100, указывающий что данное поле может состоять из максимум 100 символов
    image = models.FileField(upload_to='img/') # создание поля image на основе класса models.FileField - поля для файлов, которому передан обязательный аргумент upload_to - который указывает откуда брать файлы для загрузки. В данном случае аргументу передано upload_to='img/' - это значит что файлы для загрузки в данное поле должны браться из папки с имененм img, находящейся в папке static