## 🚀 Начало работы
Следуйте этим шагам, чтобы запустить проект локально.

### 1. Клонируйте репозиторий
```bash
git clone https://gitlab.com/Maquee41/voltzone.git
cd voltzone
```

### 2. Создайте и активируйте виртуальное окружение

#### На Linux/macOS:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

#### На Windows:
```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Установите зависимости
```bash
pip install -r requirements/prod.txt
```

### 4. Настройте переменные окружения

#### 4.1 Скопируйте пример .env файла:

На Linux/macOS:
```bash
cp example.env .env
На Windows:
```

На Windows:
```bash
copy example.env .env
```

### 4.2 Отредактируйте файл .env:

**SECRET_KEY**:
Сгенерируйте надёжный секретный ключ:
```bash
cd voltzone
python manage.py shell
>>> from django.core.management.utils import get_random_secret_key
>>> get_random_secret_key()
>>> exit()
```
Затем скопируйте полученное значение и вставьте его в  `.env`:
```env
SECRET_KEY=ваш-сгенерированный-секретный-ключ
```

### 5. Подготовьте статические файлы
```bash
python manage.py collectstatic
```

### 6. Примените миграции
```bash
python manage.py migrate
```

### 7. Создайте суперпользователя
```bash
python manage.py createsuperuser
```

### 8. Запустите сервер разработки
```bash
python manage.py runserver
```
