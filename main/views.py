from django.shortcuts import render
from django.utils.translation import gettext


def main_view(request):
    context = {
        'enter': gettext('Вход'),
        'registration': gettext('Регистрация'),
        'users': gettext('Пользователи'),
        'header': gettext('Привет от Хекслета!'),
        'body': gettext('Практические курсы по программированию'),
        'link': 'hexlet.io',
        'footer': 'Hexlet 2021',
    }
    return render(request, 'index.html', context)
