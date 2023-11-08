# ⚠️создали самостоятельно
# ✅импортировали модели
from django import forms

from .models import News


# создали форму
class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = [
            'heading',
            'text',
            'author',
            'category',
            'pub_date',
            'type'
        ]
