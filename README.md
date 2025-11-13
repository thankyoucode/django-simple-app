# Simple Django Application

A simple Django project created to **refresh and revisit** core concepts —
focusing mainly on **user registration, login, and logout** functionality
without using any custom user model.

## Users App

This app demonstrates a straightforward flow for:

- Registering new users
- Logging in existing users
- Logging out authenticated users

## Virtual environment

```bash
# 1. Initialize virtual environment and project
uv init .venv

# 2. Install dependencies from pyproject.toml
uv install
```

## Project setup / run

```bash
# 1. Create a new Django project
django-admin startproject myproject
cd myproject

# 2. Create a new app for users
python manage.py startapp users

# 3. Apply initial migrations
python manage.py makemigrations
python manage.py migrate

# 4. Create a superuser (optional, for admin)
python manage.py createsuperuser

# 5. Run the development server
python manage.py runserver
```
