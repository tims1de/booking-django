# Cервис booking

[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![PostgerSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=Docker)](https://www.docker.com/)
[![Redis](https://img.shields.io/badge/-Redis-464646?style=flat-square&logo=Redis)](https://redis.io/)
[![Ruff](https://img.shields.io/badge/-Ruff-464646?style=flat-square&logo=Ruff)](https://docs.astral.sh/ruff/)

# Описание 
🚪Проект представляет собой REST API для системы бронирования комнат, разработанный с использованием Django и Django REST Framework. Основная задача проекта — предоставить удобный и масштабируемый backend для управления пользователями, комнатами и их бронированиями. В качестве базы данных используется PostgreSQL, что обеспечивает надежность и производительность при работе с большим объемом данных. Для кэширования отдельных эндпоинтов, в частности получения списка всех комнат, используется Redis, что позволяет значительно снизить нагрузку на базу данных и повысить скорость отклика.

В проекте активно применяются возможности Django ORM, включая использование Q-запросов и аннотаций для сложных выборок и фильтраций данных, таких как расчет количества оставшихся доступных комнат на определенные даты или получение пользователей с определенным количеством бронирований. Также реализована Django Admin-панель для удобного управления моделями пользователей, комнат и бронирований через веб-интерфейс.

Для обеспечения качества кода использовался линтер Ruff, который помогает поддерживать единый стиль и устранять потенциальные ошибки еще на этапе разработки. Проект полностью контейнеризирован с использованием Docker и docker-compose, что облегчает его развертывание и переносимость между разными средами.

API реализует несколько основных эндпоинтов: получение списка всех пользователей, фильтрация пользователей по количеству бронирований, получение списка всех комнат, получение доступных комнат на определенные даты с учетом текущих бронирований, а также создание и просмотр всех бронирований. Такое решение делает проект гибким и удобным для интеграции с фронтенд-приложениями или мобильными клиентами.


# Локальный запуск проекта 

- Склонировать репозиторий:

```bash
   git clone <ссылка на репозиторий>
```

- Установить зависимости из файла requirements.txt:

```bash
   pip install -r requirements.txt
```

- Создать файл .env по образцу:
```bash
  NAME=*********
  USER=*********
  PASSWORD=*****
  HOST=*********
  PORT=*********
  
  REDIS_HOST=***
```

- Создать файл .env-docker по образцу:
```bash
  NAME=*********
  USER=*********
  PASSWORD=*****
  HOST=*********
  PORT=*********
  
  POSTGRES_DB=*********
  POSTGRES_USER=*******
  POSTGRES_PASSWORD=***
  
  REDIS_HOST=***
```

- Создать миграции:
```bash
   python manage.py makemigrations
```

- Выполнить миграции:
```bash
   python manage.py migrate
```

- Запустить проект:
```bash
   python manage.py runserver
```

# Запуск проекта через Docker

- Запустить docker-compose:
```bash
  docker compose up --build
```

#### Автор

Куприянов Т.А. - [https://github.com/tims1de](https://github.com/tims1de)
