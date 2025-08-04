#!/bin/bash

# code-server'ı arkaplanda başlat
code-server /app --auth none --port 8080 &

# Django server'ı başlat
./venv/bin/python manage.py runserver 0.0.0.0:8000
