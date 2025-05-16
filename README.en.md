## 🚀 Getting Started

Follow these steps to run the project locally.

### 1. Clone the Repository

```bash
git clone https://gitlab.com/Maquee41/voltzone.git
cd voltzone
```

### 2. Create and Activate Virtual Environment

#### On Linux/macOS:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

#### On Windows:
```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements/prod.txt
```

### 4. Configure Environment Variables

#### 4.1 Copy the example `.env` file:

##### On Linux/macOS:
```bash
cp example.env .env
```

##### On Windows:
```bash
copy example.env .env
```

#### 4.2 Edit the `.env` file:

**SECRET_KEY**:
Generate a secure secret key:
```bash
cd voltzone
python manage.py shell
>>> from django.core.management.utils import get_random_secret_key
>>> get_random_secret_key()
>>> exit()
```
Then copy the output and paste it into your `.env`:
```env
SECRET_KEY=your-generated-secret-key
```

### 5. Staticfiles

```bash
python manage.py collectstatic
```

### 6. Apply Migrations

```bash
python manage.py migrate
```

### 7. Create superuser

```bash
python manage.py createsuperuser
```

### 8. Run the Development Server

```bash
python manage.py runserver
```
