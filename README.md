# YaCut - сервис для создания коротких ссылок

## Описание
YaCut - это сервис, позволяющий создавать короткие ссылки для длинных URL-адресов. Есть возможность автоматической и ручной генерации идентификаторов коротких ссылок.

## Технологический стек
- Python 3.9+
- Flask 3.0.2
- SQLAlchemy 2.0+
- SQLite

## Установка и запуск

### Клонирование репозитория
```bash
git clone https://github.com/your-username/yacut.git
cd yacut
```

### Создание и активация виртуального окружения
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Unix/macOS
python3 -m venv venv
source venv/bin/activate
```

### Установка зависимостей
```bash
pip install -r requirements.txt
```

### Настройка переменных окружения
Создайте файл .env в корневой директории проекта:
```
FLASK_APP=yacut
FLASK_ENV=development
DATABASE_URI=sqlite:///db.sqlite3
SECRET_KEY=your-secret-key
```

### Инициализация базы данных
```bash
flask db upgrade
```

### Запуск приложения
```bash
flask run
```

## API Документация
- Файл спецификации OpenAPI: [yacut/static/openapi.yml](yacut/static/openapi.yml)
- Интерактивная документация Swagger доступна по [ссылке](http://localhost:5000/docs)

### Создание короткой ссылки
```http
POST /api/id/

Request:
{
    "url": "https://example.com",
    "custom_id": "example" // опционально
}

Response:
{
    "url": "https://example.com",
    "short_link": "http://hostname/example"
}
```

### Получение оригинальной ссылки
```http
GET /api/id/{short_id}/

Response:
{
    "url": "https://example.com"
}
```

## Контактные данные
- GitHub: [@gera1311](https://github.com/gera1311/yacut)
- Email: [gera.python@yandex.com](mailto:gera.python@yandex.com)
- Березовский Герман Андреевич
