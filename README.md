# ShopEase — Mini E-Commerce Web Application

A clean, fully functional Django e-commerce application built as a student portfolio project. It demonstrates real-world development practices including user authentication, session-based cart management, order processing, and Django admin integration.

---

## Features

### Customer Features
- **Browse Products** — View all products in a responsive grid with category filtering
- **Product Detail** — Full product page with description, stock status, and related items
- **Shopping Cart** — Session-based cart with add / remove / update quantity
- **User Registration & Login** — Built on Django's built-in authentication system
- **Checkout** — Enter shipping details and place an order (no payment required)
- **Order History** — View all past orders with status tracking
- **Order Detail** — Itemised breakdown of each order

### Admin Features
- Manage products (add / edit / delete / toggle availability)
- Manage categories
- View and update order statuses
- Inline order item view on each order record

---

## Tech Stack

| Layer     | Technology                        |
|-----------|-----------------------------------|
| Backend   | Python 3.10+ / Django 4.2+        |
| Frontend  | HTML5, CSS3, JavaScript           |
| UI Kit    | Bootstrap 5.3                     |
| Icons     | Bootstrap Icons 1.11              |
| Fonts     | Google Fonts — Inter              |
| Database  | SQLite (dev) / PostgreSQL (prod)  |
| Images    | Pillow                            |

---

## Project Structure

```
E-COMMERCE/
├── ecommerce/          # Django project config (settings, urls, wsgi)
├── products/           # Product & Category models, views, admin
│   └── management/
│       └── commands/
│           └── seed_data.py   # Sample data seeder
├── cart/               # Session-based cart logic + views
├── orders/             # Order models, checkout, history views
├── users/              # Registration & authentication views
├── templates/          # All HTML templates
│   ├── base.html
│   ├── products/
│   ├── cart/
│   ├── orders/
│   └── users/
├── static/
│   ├── css/style.css
│   └── js/main.js
├── media/              # Uploaded product images (created at runtime)
├── db.sqlite3          # SQLite database (created after migration)
├── manage.py
├── requirements.txt
└── README.md
```

---

## Setup Instructions

### 1. Clone / Navigate to the Project

```bash
cd "E-COMMERCE"
```

### 2. Create a Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py migrate
```

### 5. Seed Sample Data (10 products, 4 categories)

```bash
python manage.py seed_data
```

### 6. Create a Superuser (Admin Access)

```bash
python manage.py createsuperuser
```

Follow the prompts to set a username, email, and password.

### 7. Run the Development Server

```bash
python manage.py runserver
```

Open your browser and visit: **http://127.0.0.1:8000/**

---

## Key URLs

| Page              | URL                          |
|-------------------|------------------------------|
| Home / Shop       | `/`                          |
| Product Detail    | `/product/<id>/`             |
| Shopping Cart     | `/cart/`                     |
| Checkout          | `/orders/checkout/`          |
| Order History     | `/orders/history/`           |
| Login             | `/users/login/`              |
| Register          | `/users/register/`           |
| Admin Panel       | `/admin/`                    |

---

## Switching to PostgreSQL

In `ecommerce/settings.py`, replace the `DATABASES` section with:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ecommerce_db',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

Then install the driver:

```bash
pip install psycopg2-binary
```

---

## Default Admin Credentials (after createsuperuser)

Set during setup — access the admin panel at `/admin/`.

---

## Notes

- No payment gateway is integrated — checkout is for demo purposes
- Product images are optional; placeholder icons are shown if no image is uploaded
- Cart data is stored in the user's browser session
- Stock levels are decremented automatically when an order is placed

---
