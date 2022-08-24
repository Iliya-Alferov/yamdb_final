![example workflow](https://github.com/iliya-alferov/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)


# CI и CD проекта api_yamdb

## Описание.
Настройка для приложений Continuous Integration и Continuous Deployment.

+ автоматический запуск тестов,
+ обнавление образов Docker Hub,
+ автоматический деплой на боевой сервер при пуше на главную ветку main.

## Технологии.
Python 3.7
Django 2.2.16
DRF 3.12.4
PostgreSQL 12.2

## Установка.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

~~~
git clone https://github.com/Iliya-Alferov/yamdb_final.git
~~~

~~~
cd api_yamdb
~~~

Создать и активировать виртуальное окружение:

~~~
python -m venv venv
~~~

~~~
source venv/Scripts/activate
~~~

Загрузка образа на DockerHub.(локально из директории с Dockerfile)

~~~
docker build -t iliyaalferov2015/yamdb_final:v7.08.2022
~~~

Авторизоваться через консоль.

~~~
docker login -u iliyaalferov2015
~~~

Загрузить образ на DockerHub.

~~~
docker push iliyaalferov2015/yamdb_final:v7.08.2022
~~~

Переходим на боевой сервер.

~~~
ssh my_cloud@84.201.137.225
~~~

Создаём суперпользователя:(на сервере)

Получаем список запущенных контейнеров.
~~~
sudo docker container ls
~~~

Создаем superuser в контейнере web.

~~~
sudo docker exec -it <container_id> python manage.py createsuperuser
~~~

Войдите в админку.

Создайте одну-две записи объектов.

## Примеры.

Регистрация нового пользователя. 

Пример POST-запроса без токена: регистрация нового пользователя.

*POST localhost/api/auth/signup/*

~~~
{
  "email": "string",
  "username": "string"
}
~~~

~~~
На сервер, в папку sent_emails приходит письмо с "confirmation_code"
~~~

### Пример ответа:

~~~
{
  "email": "string",
  "username": "string"
}
~~~

Получение JWT-токена.

*POST localhost/api/auth/token/*

~~~
{
  "username": "string",
  "confirmation_code": "string"
}
~~~

### Пример ответа:

~~~
{
  "token": "string"
}
~~~

Пример GET-запроса без токена: получение списка всех категорий.

*GET localhost/api/v1/categories/*

~~~
[
  {
    "count": 0,
    "next": "string",
    "previous": "string",
    "results": [
      {
        "name": "string",
        "slug": "string"
      }
    ]
  }
]
~~~

Пример POST-запроса с токеном: добавление новой категории.

Права доступа: администратор.

*POST localhost/api/v1/categories/*

~~~
{
  "name": "string",
  "slug": "string"
}
~~~

### Пример ответа:

~~~
{
  "name": "string",
  "slug": "string"
}
~~~

Пример DELETE-запроса с токеном: удаление категории.

Права доступа: администратор.

*DELETE localhost/api/v1/categories/{slug}/*


Пример GET-запроса без токена: получение списка всех жанров.

*GET localhost/api/v1/categories/genres/*

~~~
[
  {
    "count": 0,
    "next": "string",
    "previous": "string",
    "results": [
      {
        "name": "string",
        "slug": "string"
      }
    ]
  }
]
~~~

Пример POST-запроса с токеном: добавление нового жанра.

Права доступа: администратор.

*POST localhost/api/v1/genres/*

~~~
{
  "name": "string",
  "slug": "string"
}
~~~

### Пример ответа:

~~~
{
  "name": "string",
  "slug": "string"
}
~~~

Пример DELETE-запроса с токеном: удаление жанра.

Права доступа: администратор.

*DELETE localhost/api/v1/genres/{slug}/*

Пример GET-запроса без токена: получение списка всех произведений.

*GET localhost/api/v1/titles/*

~~~
[
  {
    "count": 0,
    "next": "string",
    "previous": "string",
    "results": [
      {
        "id": 0,
        "name": "string",
        "year": 0,
        "rating": 0,
        "description": "string",
        "genre": [
          {
            "name": "string",
            "slug": "string"
          }
        ],
        "category": {
          "name": "string",
          "slug": "string"
        }
      }
    ]
  }
]
~~~

Пример POST-запроса с токеном: добавление нового произведения.

Права доступа: администратор.

*POST localhost/api/v1/titles/*

~~~
{
  "name": "string",
  "year": 0,
  "description": "string",
  "genre": [
    "string"
  ],
  "category": "string"
}
~~~

### Пример ответа:

~~~
{
  "id": 0,
  "name": "string",
  "year": 0,
  "rating": 0,
  "description": "string",
  "genre": [
    {
      "name": "string",
      "slug": "string"
    }
  ],
  "category": {
    "name": "string",
    "slug": "string"
  }
}
~~~

Получение информации о произведении, без токена.

*GET localhost/api/v1/titles/{titles_id}/*

~~~
{
  "id": 0,
  "name": "string",
  "year": 0,
  "rating": 0,
  "description": "string",
  "genre": [
    {
      "name": "string",
      "slug": "string"
    }
  ],
  "category": {
    "name": "string",
    "slug": "string"
  }
}
~~~

Пример DELETE-запроса с токеном: удаление жанра.

Права доступа: администратор.

*DELETE localhost/api/v1/titles/{titles_id}/*


Пример GET-запроса без токена: получение списка всех отзывов.

*GET localhost/api/v1/{titles_id}/reviews/*

~~~
[
  {
    "count": 0,
    "next": "string",
    "previous": "string",
    "results": [
      {
        "id": 0,
        "text": "string",
        "author": "string",
        "score": 1,
        "pub_date": "2019-08-24T14:15:22Z"
      }
    ]
  }
]
~~~

Пример POST-запроса с токеном: добавление нового отзыва.

Права доступа: аутентифицированные пользователи.

*POST localhost/api/v1/titles/{title_id}/reviews/*

~~~
{
  "text": "string",
  "score": 1
}
~~~

### Пример ответа:
~~~
{
  "id": 0,
  "text": "string",
  "author": "string",
  "score": 1,
  "pub_date": "2019-08-24T14:15:22Z"
}
~~~


