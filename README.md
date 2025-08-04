# 📝 Full-Stack Notes App (Vue.js + Django + Docker)

This is a full-stack notes application built with **Vue.js (frontend)** and **Django (backend)**, fully containerized with **Docker** for local development.

## 📁 Project Structure

 myproject
 
    ├── Dockerfile
    ├── db.sqlite3
    ├── docker-compose.yml
    ├── entrypoint.sh
    ├── frontend
    ├── manage.py
    ├── myproject
    ├── notes
    ├── requirements.txt
    ├── templates
    └── venv

  ### 🔧 Requirements

- Docker
- Docker Compose
  

**Django backend → http://localhost:8000**

**Vue.js frontend → http://localhost:5173**

## 👤 User Registration

Users can register at:

http://localhost:8000/api/register/

Only registered users can add notes through the frontend.

## 📄 Notes API
| Method | Endpoint      | Description    | Auth Required |
| ------ | ------------- | -------------- | ------------- |
| GET    | `/api/notes/` | Get all notes  | ✅             |
| POST   | `/api/notes/` | Add a new note | ✅             |


## 🐳 Docker Overview

docker-compose.yml

```
services:
  django:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - .:/app

  vue:
    image: node:20-alpine
    working_dir: /app/frontend
    volumes:
      - ./frontend:/app/frontend
      - /app/frontend/node_modules
    ports:
      - "5173:5173"
    command: sh -c "npm install && npm run dev"

```

## UML Diagram (PlantUML)
Here's the system overview in PlantPUML

![Django + code-server mimarisi](https://uml.planttext.com/plantuml/png/NLAzRjim4Dxv58TCDkgVFKEHE8OBD4tImesN8CF5kWgCA5AWA1T2aRcFeR5hjMJA9lczUYHbr-qatdq_-kx8YzAXTLMkX9DE4QmgfQPhXziCbi-eKmFlO5FHxBc4M-FWlauhXJcMVIi4RfsnS5-I5Q9W1QO4Pojhj2ETm2ZAncVmGm0yN2O96z1iLn5ScRmmchHx12nXG0AfA3mXjej2l9mOB_WGV6EkmVS8UuiWYdqssqdwNiwAEhXjV17xkKb87O6RK4Nacx7v4LZvWlilFjYmYyiabte8pQU0eCCdB0b6wo-VfADnW9SBdzsl1gRJzuSHuJmiaJB5AplqF1xICVhvRlqLvbZ8-TOIEffgPinXz75zTpiMaUNvCNIq8p2gsZUkifMTGCRtXxfljtrRAmIfvBx9fEB5IIkj68JUOxbW_OQiX0phX1AcsjF4F1yJuhT0JKhM_3uua4BRjv1shxPxqwvxyyCSTOT9hh7kMpU13_pRVJE1xcVVPdsxRu1BHJcBvCb08Sprt-pm95KgFKbBI4pVM7vs5dO4TVUgoN5KmNVzttBxtzqlbcG-NEduzA_YWhVWN_eV)

## 📚 Key Takeaways

✅ Built a component-based Vue.js frontend 

✅ Created Django REST API with authentication

✅ Connected frontend to backend via API

✅ Containerized both services using Docker

✅ Learned full-stack development best practices


## ⚡ Quick Start

1. Clone this repository:
   ```bash
   git clone https://github.com/ata6unal/django-code-server.git
   cd django-code-server

```
docker compose up --build
```


  



