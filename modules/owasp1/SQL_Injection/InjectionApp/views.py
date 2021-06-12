import datetime

from django.shortcuts import render

from SQL_Injection import settings
from .models import Users
import jwt


def generate_jwt_token():
    """
    Генерирует веб-токен JSON, в котором хранится идентификатор этого
    пользователя, срок действия токена составляет 12 часов от создания
    """
    dt = datetime.now() + datetime.timedelta(hours=12)

    token = jwt.encode({
        'id': 1,
        'exp': int(dt.strftime('%s'))
    }, settings.SECRET_KEY, algorithm='HS256')

    return token.decode('utf-8')


def user_login(request):
    authentication_error = False
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # SQL запрос нормального человека:
        # if Users.objects.raw(
        #   "SELECT * FROM InjectionApp_users WHERE username = %s AND password = %s", [username, password]):

        # SQL запрос курильщика:
        # print(f"SELECT * FROM InjectionApp_users WHERE username = %s AND password = '{password}';" % username)
        if username == 'admin' and Users.objects.raw(
                f"SELECT * FROM InjectionApp_users WHERE username = %s AND password = '{password}';", [username]):
            return render(request, 'InjectionApp/index.html',
                          context={
                              'flag': 'SQLflag01192injection!'})
        else:
            authentication_error = True

    return render(request, 'InjectionApp/user_login.html', {'authentication_error': authentication_error})
