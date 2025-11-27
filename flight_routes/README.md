# Installation & Setup

## Navigate to Project Directory

```bash
cd flight_routes
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Virtual Environment
```bash
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

## Install Dependencies

```bash
pip install django
```

## Setup Database

```bash
python manage.py makemigrations
python manage.py migrate
```

## Create Superuser

```bash
python manage.py createsuperuser
```

## Run Development Server
```bash
python manage.py runserver
```

## Access the application

Main application: http://127.0.0.1:8000/

Admin panel: http://127.0.0.1:8000/admin/


# 📋 Project Overview
A Django web application for managing and analyzing flight routes between airports with advanced pathfinding algorithms.

# ✨ Features
Add Airport Routes - Create connections with direction and duration

Find Nth Node - Navigate through route networks

Longest Route - Identify maximum duration routes

Shortest Path - Calculate optimal paths

# 🛠️ Technology Stack
Backend: Django 4.x

Database: SQLite

Frontend: HTML5, Bootstrap 5

Algorithms: BFS, Dijkstra's Algorithm