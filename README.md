# Payments

Тестовое задание на Python-разработчик. 
Django-приложение для визуализации данных о платежах с использованием PostgreSQL и Chart.js.

## Особенности

- **Одностраничное приложение** с интерактивными графиками
- **Два типа визуализации**: линейный график и гистограмма
- **Docker-контейнеризация** для простого развертывания
- **Админ-панель Django** для управления данными
- **База данных PostgreSQL** с надежным хранением

## Структура проекта

```
Payments/
├── Payments/                # Основное приложение
├── payment_app/			 # Настройки проекта
├── Dockerfile               # Конфигурация образа
├── docker-compose.yml       # Оркестрация контейнеров
├── requirements.txt         # Зависимости Python
└── README.md                # Этот файл
```

## Визуализация

### Линейный график
- Зависимость суммы платежей от даты
- Группировка по дням с суммированием

### Гистограмма  
- Общие суммы платежей по клиентам
- Группировка по клиентам с суммированием

## Технологический стек

- **Backend**: Django 4.2, Python 3.8
- **Database**: PostgreSQL latest
- **Frontend**: Chart.js, чистый HTML/CSS/JS
- **Containerization**: Docker, Docker Compose

## Требования
- Docker
- Docker Compose

## Установка
- Клонировать репозиторий:

```bash
git clone https://github.com/<your-username>/Payments.git
cd Payments
```

## Использование
- Запуск
```bash
docker-compose up --build
```

- После запуска сервис будет доступен по адресу:
http://localhost:8000/

- Создание суперпользователя

```bash
docker-compose exec web python manage.py createsuperuser
```

- Доступ к админ-панели по URL: http://localhost:8000/admin/ (логин/пароль: созданные на предыдущем шаге)

- Локальная разработка без Docker
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

- Доступ к базе данных
```bash
docker-compose exec postgres psql -U postgres -d payment_db
```

- Очистка и пересборка
```bash
docker-compose down -v
docker system prune -a
docker-compose up --build
```

- Просмотр логов
```bash
docker-compose logs web
docker-compose logs postgres
```

## Контактная информация
- Электронная почта: orlovva.19@gmail.com