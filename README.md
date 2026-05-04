# 🛒 CoreShop Django

![Python](https://img.shields.io/badge/python-3.14-blue.svg)
![Django](https://img.shields.io/badge/django-4.2-green.svg)
![Poetry](https://img.shields.io/badge/dependency%20manager-poetry-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

---

## 📝 Описание

CoreShop Django — учебный проект в рамках курса «Python-разработчик» на платформе SkyPro.  
Проект создан для освоения основ Django: настройка проекта, приложения, маршрутизация, работа с шаблонами и обработка форм.

Реализован минимальный интернет-магазин с главной страницей, страницей контактов и формой обратной связи.

### Возможности

- главная страница (`/`)
- страница контактов с формой (`/contacts/`)
- обработка POST-запроса от формы
- страница подтверждения после отправки сообщения
- стилизация Bootstrap

Используемые технологии:

- Django 6.0+
- Python 3.14
- Poetry
- Bootstrap 5

---

## 🚀 Быстрый старт

### Требования

- Python 3.14 (или совместимая версия)
- Poetry
- Git

### Установка

1. Убедитесь, что установлен Poetry:
    ```bash
    pip install poetry
    ```
   
2. Убедитесь, что установлен Git:
https://git-scm.com/downloads

3. Клонируйте репозиторий:
    ```bash
    git clone git@github.com:GrandBalaxon/CoreShop-Django.git
    ```
    ```bash
    cd coreshop-django
    ```
   
4. Установите зависимости:
    ```bash
    poetry install
    ```
---

## ⚙️ Настройка

В корне проекта находится файл `.env.sample` — пример конфигурации.  
Скопируйте его и переименуйте в `.env`:

```bash
cp .env.sample .env
````

Внутри `.env` пропишите свои реальные значения:

---

## 🛠 Использование

Запуск сервера разработки
```bash
python manage.py runserver
````

Откройте в браузере:

* Главная страница: http://127.0.0.1:8000/

* Контакты: http://127.0.0.1:8000/contacts/

На странице контактов заполните форму и нажмите «Отправить» — вы увидите страницу с подтверждением и вашим именем.

---

## 📦 Структура проекта

```
coreshop-django/
│
├── config/                 # Основная конфигурация Django
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── catalog/                # Приложение «Каталог»
│   ├── migrations/         # (пока пусто)
│   ├── templates/
│   │   └── catalog/
│   │       ├── index.html
│   │       ├── contacts.html
│   │       └── message_received.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── static/                 # Статические файлы (CSS, JS)
│   ├── css/
│   │   └── bootstrap.min.css
│   └── js/
│       └── bootstrap.bundle.min.js
│
├── .gitignore
├── manage.py
├── pyproject.toml
├── poetry.lock
├── poetry.toml
└── README.md
```

---

## 📜 Лицензия

Этот проект распространяется под лицензией MIT.