from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import NewsForm
from .models import News
from .filters import NewsFilter
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin


@login_required
def upgrade_me(request):
    user = request.user
    authors = Group.objects.get(name='authors')
    if not request.user.groups.filter(name='authors').exists():
        authors.user_set.add(user)
    return redirect('/')


# Тут смотрим новости – news
class NewsList(ListView, LoginRequiredMixin):
    # Указываем модель, объекты которой мы будем выводить
    model = News
    # сортируем через наоборот
    ordering = '-pub_date'
    # Имя шаблона для новостей — News
    template_name = 'news.html'
    # Имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'news'
    # ✅указали количество записей на странице (не более 10)
    paginate_by = 3

    # Метод get_context_data позволяет изменить набор данных, который будет передан в шаблон.
    def get_context_data(self, **kwargs):
        # С помощью super() мы обращаемся к родительским классам
        # и вызываем у них метод get_context_data с теми же аргументами,
        # что и были переданы нам.
        # В ответе мы должны получить словарь.
        context = super().get_context_data(**kwargs)
        # # ✅Добавляем в контекст объект фильтрации.
        # context['filterset'] = self.filterset
        # К словарю добавим текущую дату в ключ 'time_now'.
        context['time_now'] = datetime.utcnow()
        # ✅доп переменная анонс (announcement) статей (их правда пока нет, но они будут)
        context['announcement'] = None
        return context


# Тут смотрим конкретную новость/статью – one_news
class NewsDetail(DetailView):
    # модель для получения информации по отдельной новости
    model = News
    # используем новый шаблон — one_news.html
    template_name = 'one_news.html'
    # название объекта, в котором будет выбранная статья
    context_object_name = 'one_news'


class SearchView(ListView):
    model = News
    # сортируем через наоборот
    ordering = '-pub_date'
    template_name = 'search.html'
    # Имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'news'

    # Метод get_context_data позволяет изменить набор данных, который будет передан в шаблон.
    def get_context_data(self, **kwargs):
        # С помощью super() мы обращаемся к родительским классам
        # и вызываем у них метод get_context_data с теми же аргументами,
        # что и были переданы нам.
        # В ответе мы должны получить словарь.
        context = super().get_context_data(**kwargs)
        # ✅Добавляем в контекст объект фильтрации.
        context['filterset'] = self.filterset
        return context

    # Переопределяем функцию получения списка новостей
    def get_queryset(self):
        # Получаем обычный запрос
        queryset = super().get_queryset()
        # Используем наш класс фильтрации.
        # self.request.GET содержит объект QueryDict, который мы рассматривали в этом юните ранее.
        # Сохраняем нашу фильтрацию в объекте класса, чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset = NewsFilter(self.request.GET, queryset)
        # Возвращаем из функции отфильтрованный список новостей
        return self.filterset.qs


# обновляем (редактируем) новость
class NewsUpdate(PermissionRequiredMixin, UpdateView):
    model = News
    form_class = NewsForm
    login_url = '/accounts/login/'
    template_name = 'post_edit.html'
    permission_required = ('NewsPaper.change_news',)


# создаем новость
class NewsCreate(PermissionRequiredMixin, CreateView):
    model = News
    fields = ['author', 'heading', 'text', 'pub_date', 'category']
    template_name = 'news_create.html'
    permission_required = ('NewsPaper.add_news',)
    # после создания возвращаемся на главную страницу
    success_url = reverse_lazy('news_list')

    # переопределяем метод form_valid и устанавливаем поле новости по умолчанию
    def form_valid(self, form):
        news = form.save(commit=False)
        news.news_type = 'NW'
        news.save()
        return super().form_valid(form)


# удаляем новость, после удаления на главную
class NewsDelete(DeleteView):
    model = News
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news_list')


# создаем статью
class ArticleCreate(PermissionRequiredMixin, CreateView):
    model = News
    fields = ['author', 'heading', 'text', 'pub_date', 'category']
    template_name = 'article_create.html'
    permission_required = ('NewsPaper.add_news',)
    success_url = reverse_lazy('news_list')

    # переопределяем метод form_valid и устанавливаем поле статьи по умолчанию
    def form_valid(self, form):
        news = form.save(commit=False)
        news.type = 'AR'
        news.save()
        return super().form_valid(form)


# обновляем (редактируем) статью. После обновления на главную
class ArticleUpdate(PermissionRequiredMixin, UpdateView):
    model = News
    fields = ['author', 'heading', 'text']
    login_url = '/accounts/login/'
    template_name = 'article_edit.html'
    permission_required = ('NewsPaper.change_news',)
    # success_url = reverse_lazy('news_list')


# удаляем статью
class ArticleDelete(DeleteView):
    model = News
    template_name = 'news/article_delete.html'
    success_url = reverse_lazy('news_list')

