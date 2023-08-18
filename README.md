# Проект управления пользователями с использованием Django REST Framework

Этот проект представляет собой простую реализацию API для управления пользователями с помощью Django REST Framework.

## Установка

1. Склонируйте репозиторий на вашем локальном компьютере:

```bash
git clone https://github.com/stirelshka8/TestDjango.git
```

2. Создайте виртуальное окружение и активируйте его:

```bash
cd /ПУТЬ/ДО/ПРОЕКТА
python3 -m venv venv
source venv/bin/activate # для Linux/Mac
venv\Scripts\activate # для Windows
```

3. Установите зависимости:

```bash
pip install -r req.txt
```


4. Примените миграции:

```bash
python manage.py migrate
```

5. Запустите сервер:

```bash
python manage.py runserver
```


## Использование API

API предоставляет следующие эндпоинты:

- `POST /auth/phone/` - Регистрация пользователя по номеру телефона.
- `POST /auth/code/` - Подтверждение авторизации по пригласительному коду.
- `POST /user/profile/` - Получение профиля пользователя.
- `POST /activate/invite/` - Активация пригласительного кода.
- `POST /invited/users/` - Получение списка пользователей, активировавших пригласительный код.

## Примеры запросов

### Регистрация пользователя по номеру телефона

```bash
curl -X POST http://localhost:8000/auth/phone/ -d "phone_number=1234567890"
```

### Подтверждение авторизации по пригласительному коду
```bash
curl -X POST http://localhost:8000/auth/code/ -d "phone_number=1234567890&code=1234"
```
### Получение профиля пользователя
```bash
curl -X POST http://localhost:8000/user/profile/ -d "phone_number=1234567890"
```
### Активация пригласительного кода
```bash
curl -X POST http://localhost:8000/activate/invite/ -d "phone_number=1234567890&invite_code=ABCD12"
```
### Получение списка пользователей, активировавших пригласительный код
```bash
curl -X POST http://localhost:8000/invited/users/ -d "phone_number=1234567890"
```

## Использование Docker

### Сборка контейнера
```bash
docker build -t ИМЯ_КОНТЕЙНЕРА:ТЭГ .
```

### Запуск 
```bash
docker run -d -p 8000:8000 ИМЯ_КОНТЕЙНЕРА:ТЭГ . # -d - запуск в "фоновом" режиме
```

## Перейдите по адресу http://localhost:8000