# ✅создали файл самостоятельно для тегов
from datetime import datetime
# импорт шаблон
from django import template

# зарегали тег
register = template.Library()


# строчковый временной тег
@register.simple_tag()
def current_time(format_string='%b %d %Y'):
    return datetime.utcnow().strftime(format_string)


# ‼️Параметр декоратора takes_context=True сообщает Django, что для работы тега требуется передать контекст.
# Именно тот контекст, который мы редактировали.
@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
    # context['request'].GET.copy() нам позволяет скопировать все параметры текущего запроса.
    d = context['request'].GET.copy()
    # Далее по указанным полям мы просто устанавливаем новые значения, которые нам передали при использовании тега.
    for k, v in kwargs.items():
        d[k] = v
    # В конце мы кодируем параметры в формат, который может быть указан в строке браузера.
    # Не каждый символ разрешается использовать в пути и параметрах запроса.
    return d.urlencode()
