from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = '42y7lup4=#x6ae&^(6g6bpfqt&*7n-t=)juhlp&#+@h1d%pw&2'
DEBUG = True
ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "dashboard_app",
    "rest_framework",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Add paths to your project-level templates here if needed
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

ROOT_URLCONF = "analytics_service.urls"
WSGI_APPLICATION = "analytics_service.wsgi.application"

# DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3","NAME": BASE_DIR / "db.sqlite3"}}
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'CLIENT': {
            'host': 'mongodb+srv://shubhamroy12345_db_user:fBfisyI18mp8U5Lo@cluster0.ywle63s.mongodb.net/?appName=Cluster0', # Replace with your MongoDB server address
            'port': 27017,               # Replace with your MongoDB port if different
        },
        'NAME': 'log_analisisis_db'  # Replace with your database name,
    }
}
STATIC_URL = "/static/"

# MongoDB
# MONGO_URI = os.environ.get("MONGO_URI", "mongodb://mongodb:27017/")
