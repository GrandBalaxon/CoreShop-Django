# 🛒 CoreShop Django

![Python](https://img.shields.io/badge/python-3.14-blue.svg)
![Django](https://img.shields.io/badge/django-6.0-green.svg)
![Poetry](https://img.shields.io/badge/dependency%20manager-poetry-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

---

## 📝 Описание

CoreShop Django — учебный проект в рамках курса «Python-разработчик» на платформе SkyPro.  
Проект создан для освоения основ Django: настройка проекта, приложения, маршрутизация, работа с шаблонами и обработка форм.

Реализован интернет-магазин с каталогом товаров, детальным просмотром, формой добавления товаров, 
страницей контактов с динамической информацией и обратной связью. Проект использует базу данных PostgreSQL 
и хранение изображений.

### Возможности

- главная страница (`/`)
- страница контактов с формой (`/contacts/`)
- обработка POST-запроса от формы
- страница подтверждения после отправки сообщения
- стилизация Bootstrap
- управление товарами и категориями через встроенную админ-панель
- динамический каталог товаров на главной странице
- форма добавления нового товара с загрузкой изображения
- отображение контактной информации компании, редактируемой через админку
- кастомная команда для загрузки тестовых данных из фикстур
- наследование шаблонов от общего базового шаблона
- детальная страница товара с полным описанием и изображением (URL вида `/product/<id>/`)

Используемые технологии:

- Django 6.0+
- Python 3.14
- Poetry
- Bootstrap 5
- PostgreSQL
- psycopg2-binary
- python-dotenv
- Pillow

---

## 🚀 Быстрый старт

### Требования

- Python 3.14 (или совместимая версия)
- Poetry
- Git
- PostgreSQL

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
   
5. В корне проекта находится файл `.env.sample` — пример конфигурации. Скопируйте его и переименуйте в `.env`:

   ```bash
   cp .env.sample .env
   ````

   Внутри `.env` пропишите свои реальные значения:

---

## 🛠 Использование

Загрузите категории, продукты и контактные данные из фикстуры `catalog_fixture.json` в корне проекта:
```bash
python manage.py load_test_data
````

Запуск сервера разработки
```bash
python manage.py runserver
````

Откройте в браузере:

* Главная страница: http://127.0.0.1:8000/

* Станица для добавления товара: http://127.0.0.1:8000/add-product/

* Страница с полной информацией о товаре: http://127.0.0.1:8000/product/1/

* Админ-панель: http://127.0.0.1:8000/admin/
   
   Для использования админки вам необходимо создать суперпользователя для управления товарами, категориями и 
   контактной информацией.
   ```bash
   python manage.py createsuperuser
   ````

* Контакты: http://127.0.0.1:8000/contacts/

На странице контактов заполните форму и нажмите «Отправить» — вы увидите страницу с подтверждением и вашим именем.

---

## 📦 Структура проекта

```
coreshop-django/
│
├── config/                   # Основная конфигурация Django
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── catalog/                  # Приложение «Каталог»
│   ├── management/
│   │   └── commands/
│   │       └── load_test_data.py
│   ├── migrations/
│   ├── templates/
│   │   └── catalog/
│   │       ├── add_product.html
│   │       ├── base.html     # базовый шаблон
│   │       ├── contacts.html
│   │       ├── index.html
│   │       ├── menu.html     # подшаблон меню
│   │       ├── message_received.html
│   │       ├── product_added.html
│   │       └── product_details.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py             # модели Category, Product, ContactInfo
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── media/
│ 
├── static/                   # Статические файлы (CSS, JS)
│   ├── css/
│   │   └── bootstrap.min.css
│   └── js/
│       └── bootstrap.bundle.min.js
│
├── .env.sample
├── .gitignore
├── catalog_fixture.json 
├── manage.py
├── pyproject.toml
├── poetry.lock
├── poetry.toml
└── README.md
```

---

## 📜 Лицензия

Этот проект распространяется под лицензией MIT.