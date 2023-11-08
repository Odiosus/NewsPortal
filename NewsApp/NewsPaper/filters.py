# ⚠️создали самостоятельно
# импортировали фильтрсэт и модель
import django_filters
from django.forms import DateInput
from django_filters import FilterSet
from .models import News


# # https://django-filter.readthedocs.io/en/stable/guide/usage.html#getting-started
class NewsFilter(FilterSet):
    heading = django_filters.Filter(
        field_name='heading',
        lookup_expr='icontains'
    )
    author = django_filters.Filter(
        field_name='author',
        lookup_expr='exact'
    )
#     # https://django-filter.readthedocs.io/en/stable/ref/widgets.html#rangewidget
    pub_date = django_filters.DateFilter(
        field_name='pub_date',
        lookup_expr='gte',
        widget=DateInput(attrs={'type': 'date'})
    )

    class Meta:
        # в Meta классе мы должны указать Django модель, в которой будем фильтровать записи.
        model = News
        # В fields мы описываем по каким полям модели будет производиться фильтрация.
        fields = {
            # поиск по названию
            'category': ['exact'],
            'type': ['exact'],
        }
