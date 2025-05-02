# ⚡ VoltZone Electronics Store

A full-featured electronics e-commerce platform built with Django.

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)

## 🚀 Getting Started

Follow these steps to run the project locally.

### 1. Clone the Repository

```bash
git clone https://gitlab.com/Maquee41/voltzone.git
cd votlzone
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

### 4. Apply Migrations

```bash
python manage.py migrate
```

### 5. Configure Environment Variables

#### 5.1 Copy the example `.env` file:

##### On Linux/macOS:
```bash
cp example.env .env
```

##### On Windows:
```bash
copy example.env .env
```

#### 5.2 Edit the `.env` file:

- **ALLOWED_HOSTS**:
  ```env
  ALLOWED_HOSTS=localhost,127.0.0.1
  # or
  ALLOWED_HOSTS=*
  ```

- **DEBUG**:
  ```env
  DEBUG=True
  ```

- **SECRET_KEY**:
  Generate a secure secret key:
  ```bash
  python manage.py shell
  >>> from django.core.management.utils import get_random_secret_key
  >>> get_random_secret_key()
  ```
  Then copy the output and paste it into your `.env`:
  ```env
  SECRET_KEY=your-generated-secret-key
  ```

### 6. Run the Development Server

```bash
python manage.py runserver
```

---

## 🎆 Now you're ready to start developing VoltZone