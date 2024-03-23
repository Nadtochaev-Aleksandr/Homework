"""Nadtochaev_Sasha_2021 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include # Стандартные импорты, но мы допонительно ещё импортировали include, чтобы использовать эту функцию на странице

urlpatterns = [ # переменная urlpatterns содержит в себе список функций path которые и являются маршрутами
    path('admin/', admin.site.urls), # первая функция path содержит первый аргумент - имя маршрута как "admin/" и вторым аргументом переда класс admin.site.urls - это класс ответсвенный за работу всей административной панели django. Маршрут: admin/
    path('', include('project.urls')), # вторая функция path содержит первый аргумент - имя маршрута заданный как пустая строка - т.е. пользователь автоматически будет попадать на этот маршрут. Так называемая главна страница. Вторым аргументом передана функция include содержащая в себе путь к файлу project.urls. Следовательно при преходе по данному маршруту пользователь переадресовывается на файл url из папки project
    path('blog/', include('blog.urls')) # вторая функция path содержит первый аргумент - имя маршрута заданный как blog/ - т.е. пользователь при указании blog в адресе будет попадать сюда. Вторым аргументом передана функция include содержащая в себе путь к файлу blog.urls. Следовательно при преходе по данному маршруту пользователь переадресовывается на файл url из папки blog.
]

