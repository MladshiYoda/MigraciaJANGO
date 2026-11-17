# Аэропорт Керимов — учебный проект Django

8 моделей (Airline, Airport, Aircraft, Flight, Passenger, Ticket, CrewMember, FlightCrew), для каждой — список, детальная страница, добавление, редактирование и удаление через class-based generic views.

## Запуск Windows

```powershell
cd Kerimov
py -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
Открыть http://127.0.0.1:8000/. В архиве уже есть `db.sqlite3` с демонстрационными данными и фотографии в `media/`. После первого запуска данные можно менять и добавлять: они сохраняются в SQLite между запусками.

## Запуск Linux/macOS
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## База данных
По умолчанию SQLite — ничего отдельно запускать не нужно. Если необходим PostgreSQL, установите переменные окружения `DB_ENGINE=postgres`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT` и выполните `migrate`. Никаких паролей в исходном коде нет.

## Управление
Маршруты определены в `KerimovAPK/urls.py`; корневой `Kerimov/urls.py` только включает URL приложения. Навигация использует `{% url %}`. Изображения загружаются через `ImageField`, формы содержат `enctype="multipart/form-data"`, сохранённые фото доступны по `/media/` в режиме разработки.

Порядок заполнения: сначала авиакомпания и аэропорты, затем самолёт, затем рейс; после этого пассажир и билет. Для экипажа сначала создайте сотрудника, затем назначение. При удалении связанных объектов Django применяет каскадное удаление, поскольку так определено в исходных моделях.

Проект предназначен для локального учебного использования. Перед размещением в интернете отключите DEBUG, задайте секретный ключ, правильные ALLOWED_HOSTS, настройте права доступа, статику и обработку пользовательских файлов.
