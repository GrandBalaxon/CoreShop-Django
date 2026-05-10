# 🛒 CoreShop Django

![Python](https://img.shields.io/badge/python-3.14-blue.svg)
![Django](https://img.shields.io/badge/django-6.0-green.svg)
![Poetry](https://img.shields.io/badge/dependency%20manager-poetry-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

---

## 📝 Описание

CoreShop Django — учебный проект в рамках курса «Python-разработчик» на платформе SkyPro.  
Создан для освоения Django от фундамента до Class-Based Views (CBV).

В проекте реализован интернет‑магазин цифровых плагинов и примеров кода с блогом:
- **Каталог** – просмотр товаров, детальная страница, добавление нового продукта.
- **Контакты** – страница с динамическими реквизитами компании и формой обратной связи.
- **Блог** – полный CRUD для постов с публикацией, счетчиком просмотров и использованием CBV.

Все контроллеры (`catalog`, `blog`) переписаны с функций (FBV) на классы (CBV): `ListView`, `DetailView`, `CreateView`, 
`UpdateView`, `DeleteView`, `TemplateView`.

### Возможности

**Магазин (приложение `catalog`)**
- главная страница с карточками товаров из базы данных
- страница контактов с формой обратной связи и информацией о компании, редактируемой через админ‑панель
- страница подтверждения отправки сообщения (POST-запрос)
- детальная страница товара с полным описанием и изображением (URL: `/product/<pk>/`)
- форма добавления нового товара с загрузкой изображения (URL: `/add-product/`)
- кастомная команда `load_test_data` для заполнения базы из фикстуры

**Блог (приложение `blog`)**
- список статей с выводом только опубликованных записей (URL: `/blog/`)
- детальная страница статьи с увеличением счетчика просмотров для опубликованного поста (URL: `/blog/post/<pk>/`)
- создание новой статьи (URL: `/blog/post/new/`)
- редактирование статьи (URL: `/blog/post/<pk>/edit/`)
- удаление статьи (URL: `/blog/post/<pk>/delete/`)
- кнопка «Опубликовать» на неопубликованной статье, переводящая её в статус `is_published`
- после успешного редактирования – перенаправление на страницу просмотра статьи
- все шаблоны блога наследуют общий базовый шаблон `base.html` и подключают подшаблон `menu.html`

**Общие**
- наследование шаблонов: общий `base.html` и подшаблон меню `menu.html` находятся в `templates/`
- маршруты блога зарегистрированы через `include` в корневом `urls.py`
- все URL оканчиваются на `/`
- админ‑панель для управления товарами, категориями, постами блога и контактами

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

* Блог – http://127.0.0.1:8000/blog/

    Доступны все операции: создание, чтение, редактирование, удаление, публикация.

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
├── blog/                      # Приложение «Блог»
│   ├── migrations/
│   ├── templates/blog/
│   │   ├── home.html
│   │   ├── blog_detail.html
│   │   ├── write_blog.html
│   │   ├── update_blog.html
│   │   └── blog_confirm_delete.html
│   ├── models.py             # BlogPost, BlogCategory (или Category)
│   ├── views.py              # CBV для блога
│   ├── urls.py
│   └── admin.py
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
│   └── views.py              # CBV для каталога
│
├── templates/                # Общие шаблоны
│   ├── base.html
│   └── menu.html
│
├── media/                    # Загружаемые изображения
│   └── images/
│       ├── blog/
│       └── catalog/
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