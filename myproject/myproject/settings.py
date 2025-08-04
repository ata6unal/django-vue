import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-1234567890abcdefghijklmnopqrstuvwxyz!@#'


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'corsheaders',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'notes',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # ya klasör var ya boş liste []
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # mutlaka olmalı
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ... diğer ayarlar

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Veritabanı motoru
        'NAME': BASE_DIR / 'db.sqlite3',         # Veritabanı dosyasının konumu
    }
}




# Buradaki CORS_ALLOW_ALL_ORIGINS = True kaldırılmalı, bunun yerine sadece izin verilen originler yazılmalı:
CORS_ALLOW_ALL_ORIGINS = False  # ya da tamamen sil

# Sadece frontend adreslerini izinli yap
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:5173",
]

CORS_ALLOW_CREDENTIALS = True

DEBUG = True

STATIC_URL = '/static/'

LOGIN_URL = '/login/'





# CSRF_TRUSTED_ORIGINS ayarı
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:3000",
   
]

# CSRF_COOKIE_HTTPONLY = False kalabilir (frontend'de JS ile token alabilmek için)
ROOT_URLCONF = 'myproject.urls'
# ALLOWED_HOSTS zaten '*' ama gerekirse bunu şu şekilde bırakabilirsin
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/accounts/login/'

