# 🚀 TaskFlow - Django Task Manager

TaskFlow is a modern task management web application built using **Python**, **Django**, **SQLite**, **HTML**, and **CSS**. It helps users organize daily tasks, manage deadlines, track progress, and improve productivity through a clean and intuitive interface.

## ✨ Features

### 🔐 Authentication System

* User Registration
* User Login & Logout
* Profile Management
* Change Password

### 📋 Task Management

* Create Tasks
* View Task Details
* Update Existing Tasks
* Delete Tasks
* Mark Tasks as Completed
* Star Important Tasks
* Due Date Tracking
* Overdue Task Detection

### 🏷️ Category Management

* Create Categories
* Edit Categories
* Delete Categories
* Assign Custom Colors
* Category-wise Task Organization

### 🔍 Search & Filters

* Search by Title or Description
* Filter by Status
* Filter by Priority
* Filter by Category
* Sort Tasks by Date, Due Date, or Title

### 📊 Dashboard

* Total Tasks
* Pending Tasks
* In Progress Tasks
* Completed Tasks
* Overdue Tasks
* Urgent Tasks
* Starred Tasks
* Recent Activity Overview

---

## 🛠️ Tech Stack

| Technology            | Purpose               |
| --------------------- | --------------------- |
| Python 3              | Backend Development   |
| Django                | Web Framework         |
| SQLite3               | Database              |
| HTML5                 | Frontend Structure    |
| CSS3                  | User Interface Design |
| Django ORM            | Database Operations   |
| Django Authentication | User Management       |

---

## 📁 Project Structure

```text
taskmanager/
│
├── accounts/
│   ├── forms.py
│   ├── urls.py
│   └── views.py
│
├── tasks/
│   ├── models.py
│   ├── forms.py
│   ├── urls.py
│   └── views.py
│
├── templates/
│   ├── accounts/
│   └── tasks/
│
├── static/
│   └── css/
│
├── taskmanager/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── db.sqlite3
└── manage.py
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/taskflow.git
cd taskflow
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux / macOS:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install django
```

### Apply Migrations

```bash
python manage.py migrate
```

### Run Development Server

```bash
python manage.py runserver
```

Open your browser:

```text
http://127.0.0.1:8000/
```

---

## 📌 Core Functionalities

* User-specific task management
* Category-based organization
* Priority and status tracking
* Search and filtering system
* Dashboard analytics
* Responsive UI
* Secure authentication
* Django Admin support

---

## 🔒 Security Features

* Django Authentication System
* Password Hashing
* CSRF Protection
* Login Required Routes
* User Data Isolation
* Session Management

---

## 🎯 Concepts Demonstrated

* Django Models
* Django Forms
* Django ORM
* Function-Based Views (FBVs)
* Authentication & Authorization
* CRUD Operations
* Query Filtering
* Template Rendering
* URL Routing
* Database Relationships

---

## 👨‍💻 Author

**Meet Heruwala**

* Python Developer
* Django Developer
* BCA Graduate
* Smart India Hackathon Participant
* Python with AI Certified

GitHub: https://github.com/MeetModi752006

LinkedIn: https://www.linkedin.com/in/meet-heruwala-1444493bb/

---  

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

It helps others discover the project and motivates future improvements.
