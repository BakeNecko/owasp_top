### Запустить проект:
    1. Перейти в папку приложения modules/owasp
    2. pipenv shell 
    2. make migrate 
    3. make run 

### Документация: http://127.0.0.1:8000/docs
### 1. создание пользователя:
POST url: http://127.0.0.1:8000/register/

data:
```json 
{
    "email": "maka@gmail.com",
    "password": "123123",
    "first_name": "mono",
    "age": 21
}
```

### 2. Получить jwt-токен
POST url: http://127.0.0.1:8000/login/

data: 
```json 
{
    "grant_type": "&username=maka%40gmail.com&password=123123&scope=&client_id=&client_secret= "
}
```

### 3. Создать Админ-пользователя: owasp4
POST url: http://127.0.0.1:8000/create-admin/

data: 
```json
{
    "email": "necko_admin@gmail.com",
    "password": "123123",
    "first_name": "admin",
    "age": 21,
    "secret_admin_key": "12312300"
}
```

### 4. Получить информацию о пользователе через id (owasp4)
GET url: http://127.0.0.1:8000/user/profile_info/1/ # где 1 это id админ-пользователя


### 5. Получить информацию о текущем пользователе
GET url: http://127.0.0.1:8000/profile/