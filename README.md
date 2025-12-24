# 🚀 Blog API – Django REST Framework

A **production-ready Blog REST API** built using **Django REST Framework** with **JWT authentication**, **media handling**, and **Swagger documentation**.

This project demonstrates **real-world backend practices** including authentication, permissions, API documentation, and deployment-ready configuration.

🔗 **Live API Documentation (Swagger):**  
https://drfblogapibysumit.pythonanywhere.com/swagger/


## 🔑 Demo Login Credentials

To make evaluation easier, test credentials are provided below.

### 👤 Demo User Account 1
- **Username:** testuser1
- **Password:** test@123

---

## 📌 Key Highlights

- Clean and scalable Django REST architecture
- JWT-based authentication (industry standard)
- Public & protected API endpoints
- Image upload support
- Interactive Swagger API documentation
- Deployed and accessible online

---

## 🛠 Tech Stack

**Backend**
- Python
- Django
- Django REST Framework (DRF)

**Authentication**
- JWT (SimpleJWT)

**Database**
- SQLite (production-ready structure, easily replaceable)

**API Documentation**
- Swagger (drf-yasg)

**Static & Media Handling**
- WhiteNoise

**Deployment**
- PythonAnywhere

**Version Control**
- Git & GitHub

---

## ✨ Features

- User authentication using JWT
- CRUD operations for blog posts
- Public blog listing (read-only)
- Protected endpoints for create, update, and delete operations
- Image upload support for blogs
- Interactive Swagger API documentation
- CORS enabled for frontend integration
- Clean, scalable project structure

---

## 🔐 Authentication Flow

- Users authenticate using **JWT tokens**
- After login, an **access token** is issued
- Protected endpoints require the token in request headers

**Authorization Header Format:**
- Authorization: Bearer <access_token>

- Unauthenticated users can access **read-only** endpoints (public blogs)

---

## ⚙️ Local Setup

Follow these steps to run the project locally:

```bash
# Clone the repository
git clone https://github.com/sumitbansode360/Blog_api.git

# Navigate into the project
cd Blog_api

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Linux / macOS
source venv/bin/activate
# Windows
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver

```
👨‍💻 Author

Sumit Bansode
Full Stack Developer
(Django | Django REST Framework | React | Next.js)

🔗 LinkedIn:
https://www.linkedin.com/in/sumitbansode/
