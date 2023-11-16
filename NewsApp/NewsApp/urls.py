from django.contrib import admin
from django.urls import path, include

urlpatterns = [
   # инклюдировались
   path('admin/', admin.site.urls),
   path('pages/', include('django.contrib.flatpages.urls')),
   # Делаем так, чтобы все адреса из нашего приложения (NewsPaper/urls.py)
   # подключались к главному приложению с префиксом news/.
   path('news/', include('NewsPaper.urls')),
   path('', include('protect.urls')),
   path('sign/', include('sign.urls')),
   path('accounts/', include('allauth.urls')),
]

