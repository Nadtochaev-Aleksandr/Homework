from django.db import models

# Create your models here.

class Category(models.Model): # задана модель Category, состоящая из одного поля Name
    name = models.CharField(max_length=30) # Единственное поле модели, представленное простым текстовым полем, имеющее ограничение по максимальному количеству символов - 30 единиц

class Post(models.Model): # Задана модель Post, имеющая 5 полей, название, тело, дата создания, дата последнего изменения и связь с моделью Category
    title = models.CharField(max_length=250) # поле название, представленное простым текстовым полем, имеющим ограничение по максимальному числу вводимых символов - 250 символов.
    body = models.TextField() # Поле тело поста, представлено многострочным текстовым полем, не имеющим оограничений
    created_on = models.DateTimeField(auto_now_add=True) # Поле "Дата создания" - представлено полем типа dateTime имеющим аргумент auto_now_add=True - означающим что записвается дата создания поля и больше никогда не меняется
    last_modified = models.DateTimeField(auto_now=True) # Поле "Последние изменения" - представлено полем типа dateTime имеющим аргумент auto_now=True - означающим что записвается дата при каждом изменении поля
    categories = models.ManyToManyField('Category', related_name='posts') # поле Категория, обозначает к какой категории относится данный пост. Связан с моделью категории при помощи связи многие ко многим. данному полю задан второй агрумент related_name позволяющий получить обратную связ
class Comment(models.Model): # модель "Комментарий" имеет 4 поля: автор, тело комментария, дату создания, пост
    autor = models.CharField(max_length=250) # поле автор - представлено простым однострочным текстомым полем задано максимальное количество символов для ввода - 250
    body = models.TextField() # Поле тело комментария, представлено многострочным текстовым полем без ограничений
    created_on = models.DateTimeField(auto_now_add=True) # Поле дата создания, представлено полем с датой, имеющим аргумент auto_now_add=True символизируещим что поле будет заполнено единичжды в момент создания комментария автоматически и больше меняться не будет
    post = models.ForeignKey('Post', on_delete=models.CASCADE) # Поле пост, представляет пост к которому пишится комментарий, имеет связь с моделью пост типа один ко многим, имеет агрумент on_delete=models.CASCADE определяющий порядок действий с полем при удалении связанной с ним модели




