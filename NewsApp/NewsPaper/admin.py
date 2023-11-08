from django.contrib import admin
# импортировали модели Категорий и Новостей
from .models import Category, News


# Register your models here.
# Зарегистрировали модели Категорий и Новостей
admin.site.register(Category)
admin.site.register(News)
