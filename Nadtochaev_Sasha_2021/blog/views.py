# Create your views here.
from django.shortcuts import render
from .models import Post, Comment # Из папки приложения blog.models импортируются модели Post и Comment
from .forms import CommentForm # Из папки blog.form импортируется класс CommentForm


def blog_index(request): # создана функуция представления blog_index, который передан один обязательный аргумент request
    posts = Post.objects.all().order_by('-created_on') # определена переменная posts которая включает в себя queryset всех объектов модели Post (Post.objects.all()), отсортированных по дате создания в обратном порядке (order_by('-created_on'))
    context = { # Определена переменная context, которая будет передана в качестве третьего аргумента в функуию render
        "posts": posts, # данная переменная содержит словарь из одного элемента "posts": posts. Коюч данного словаря "posts" будет подставлен в html шаблон, а значение этого ключа будут выводиться пользователю при отрабатывании шаблона
    }
    return render(request, "blog_index.html", context) # Итог отработки функции представления - возврат функции render, которой переданы 2 обязательных аргумента - request и имя шаблона = "blog_index.html", а значит при срабатывании функции blog_index пользователю будет отображен шаблон blog_index.html. Также передан третий необязательный аргумент context - это словарь, ключи которого будут подставлены в шаблон "blog_index.html", а значения по данным ключам будут отображаться пользователю при отработке шаблона.


def blog_detail(request, pk): # функция представления blog_detail, которой передан один обязательный аргумент request и один не обязательный pk - персональный ключ поста = id, который мы будем получать далее и также передавать в url.py для того чтобы каждому посту соответсвовала своя страница
    post = Post.objects.get(pk=pk) # задана перпеменная post в которую попадает qyaredset объект состоящий из данных модели Post но только с id равным pk пришедшем из url.py. То если из всей модели Post выбираем только те данные которые соответсвтуют посту на который кликнули
    form = CommentForm() # задана переменная form, которая представляет собой экземпляр класса CommentForm
    if request.method == 'POST': # далее следует проверка. Если метод, который пришел в запросе является POST методом то
        form = CommentForm(request.POST) # То форма принимает значения из метода POST запроса
        if form.is_valid(): # проверяется на правильность заполнения (метод is_valid()). Если всё верно - то создаётся комментарий:
            comment = Comment( # создаётся комментарий, который автоматически заполняет модель Comment следующими данными:
                autor=form.cleaned_data['author'], # поле autor заполняется из соответсвующего поля формы form.cleaned_data['author']. Метод cleaned_data - создаёт словарь в котором хранятся данные формы прошедшей валидацию. После валидации форма очищается, а данные из неё хранятся в cleaned_data
                body = form.cleaned_data['body'], # поле body заполняется из соответсвующего поля формы body
                post = post # Поле post заполняется переменной post определенной во второй строчке данной функции представления blog_detail (post = Post.objects.get(pk=pk)) т.е. это этот определенный пост.
            )
            comment.save() # Здесь сохраняется данные комментария, полученные строками выше. Метод save - записывает в базу данных все изменения произведенные в модели
    comments = Comment.objects.filter(post=post) # Определяется переменная comments, которая включает в себя объект quareset, состоящий из объектом модели Comment в которой поле post соответсвует посту, определенному во второй строке функции предстваления blog_detail (post = Post.objects.get(pk=pk)) т.е. для этого определенного поста.
    context = { # создается переменная context из словаря, которая затем будет передана третим аргументом в функцию render
        "post": post, # элемент словаря 1 - post соответсвуюет переменной post определенной во второй строке функции представления blog_detail (post = Post.objects.get(pk=pk))
        "comments":comments, # элемент словаря 2 - comments, соответсвует комментариям определенным в ходе работы формы
        "form":form # элемент словаря 4 - form, соответсвует экземпляру класса CommentForm
    }
    return render(request, "blog_detail.html", context) # Возврат функции render содержащей request (обязательный атрибут), имя шаблона "blog_detail.html" и context, опредененный выше.


def blog_category(request, category): # функция представления blog_category, имеющая один обязательный аргумент request и один необязательный аргумент category, который приходит из url.py, а именно функции path("<category>/", views.blog_category
    posts = Post.objects.filter( # переменная posts, содержащая в себе объект quaryset, соттветсввующий всем объектам модели Post у которых:
        categories__name__contains=category # имя поля categories содержит в себе то что пришло в функцию в качестве второго аргумента (аргумент category)
    ).order_by( #отсортированный
        '-created_on' # по полю created_on в обратном порядке
    )
    context = { # создаётся словарь, который будет передан третим аргументом в функцию render. Словарь содержит
        "category": category, # элемент 1 - катергории, которая задана вторым аргументом в функции представления
        "posts": posts # посты - которые определены во второй строчке функции представления blog_category (posts = Post.objects.filter)
    }
    return render(request, "blog_category.html", context) # Возврат функции render содержащей request (обязательный атрибут), имя шаблона "blog_category.html" и context, опредененный выше.