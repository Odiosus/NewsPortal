# # ✅создали файл самостоятельно
# # импорт шаблон
from django import template

# Зарегали фильтр
# ⚠️После добавления файла с новыми фильтрами, необходимо перезагрузить Django-сервер⚠️.
register = template.Library()

# ✅создали словарь с запрещёнкой
bullshit_dictionary = ["начинающих"]


# ✅Создали и зарегали фильтр под именем b_dictionary.
@register.filter()
def b_dictionary(value):
    # ищем запрещёнку в словаре
    for word in bullshit_dictionary:
        if word.lower() in value.lower():
            # value: значение (запрещёнка), к которому нужно применить фильтр
            value = value.replace(word[2:], '*' * len(word))
    # вернули красиво
    return value

