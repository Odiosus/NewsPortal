# ✅создали файл самостоятельно и импортировали пути
from django.urls import path
# ✅импорт представлений
from .views import NewsList, NewsDetail, SearchView, NewsCreate, NewsUpdate, NewsDelete, ArticleCreate, ArticleUpdate, \
    upgrade_me, CategoryListView, subscribe
from .views import ArticleDelete
from django.contrib.auth.decorators import login_required


urlpatterns = [
    # path — путь.
    # путь ко всем новостям остаётся пустым
    # объявленное представление является классом — представляем этот класс в виде view
    # вызываем метод as_view.
    path('', NewsList.as_view(), name='news_list'),
    path('<int:pk>', NewsDetail.as_view(), name='one_news'),
    # регистрируем новое представление SearchView
    path('search/', SearchView.as_view(), name='search'),
    path('news/create/', NewsCreate.as_view(), name='news_create'),
    path('news/<int:pk>/edit/', login_required(NewsUpdate.as_view()), name='news_update'),
    path('news/<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
    path('article/create/', ArticleCreate.as_view(), name='article_create'),
    path('article/<int:pk>/edit/', login_required(ArticleUpdate.as_view()), name='article_update'),
    path('article/<int:pk>/delete/', ArticleDelete.as_view(), name='article_delete'),
    path('upgrade/', upgrade_me, name='upgrade'),
    path('category/<int:pk>', CategoryListView.as_view(), name='category_list'),
    path('category/<int:pk>/subscribers', subscribe, name='subscribe'),

]
