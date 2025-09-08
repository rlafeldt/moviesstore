# Movies Store

A Django-based e-commerce web application for purchasing and reviewing movies.

## Features

- **Movie Catalog**: Browse and view detailed information about movies
- **User Authentication**: Registration, login, and user account management
- **Reviews**: Users can write and read movie reviews
- **Shopping Cart**: Add movies to cart and manage orders
- **Order Management**: Track purchase history and order details

## Technology Stack

- **Backend**: Django 5.0
- **Database**: SQLite3
- **Frontend**: Django Templates
- **Authentication**: Django's built-in auth system

## Project Structure

```
moviesstore/
├── accounts/          # User authentication and account management
├── cart/              # Shopping cart and order functionality
├── home/              # Homepage and general site pages
├── movies/            # Movie catalog and reviews
├── moviesstore/       # Main Django project settings and configuration
├── media/             # User-uploaded files (movie images)
└── manage.py          # Django management script
```

## Models

### Movie (`movies.models.Movie`)
- Movie catalog with name, price, description, and images

### Review (`movies.models.Review`)
- User reviews for movies with comments and timestamps

### Order (`cart.models.Order`)
- Customer orders with total price and date

### Item (`cart.models.Item`)
- Individual items within orders (movie + quantity + price)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd moviesstore
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install django pillow
```

4. Run database migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create a superuser (optional):
```bash
python manage.py createsuperuser
```

6. Start the development server:
```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

## Usage

- Visit the homepage to browse available movies
- Register an account or login to write reviews and make purchases
- Add movies to your cart and complete orders
- View your order history in your account

## Development

This appears to be a course project (located in a "2340" directory, suggesting a class number). The application uses Django's default SQLite database and includes basic e-commerce functionality with user authentication and order management.