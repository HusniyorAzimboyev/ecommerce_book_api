# E-Commerce Book API

A robust and scalable E-Commerce Book API 📚 built with Django REST Framework (DRF) 🐍. This API allows users to manage books, handle authentication via Djoser, and process payments using Stripe. It also integrates with Infobip for SMS notifications.

## Features
- 📖 CRUD operations for books
- 🔑 User authentication with Djoser
- 🛒 Stripe integration for payments
- 📲 SMS notifications via Infobip
- 📄 API documentation with Swagger
- 🛡️ Secure and scalable architecture

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/HusniyorAzimboyev/ecommerce_book_api.git
   cd ecommerce-book-api
   ```

2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```sh
   python manage.py migrate
   ```
5. Create your .env file.

6. Create a superuser (optional, for admin access):
   ```sh
   python manage.py createsuperuser
   ```

7. Run the development server:
   ```sh
   python manage.py runserver
   ```

## API Documentation
Swagger UI is available at:
```
http://127.0.0.1:8000/
```

## Technologies Used
- Django REST Framework (DRF) 🐍
- Djoser 🔑 (Authentication)
- Stripe 💳 (Payments)
- Infobip 📲 (SMS Notifications)
- PostgreSQL / SQLite 🗄️
- Swagger 📄 (API Documentation)
