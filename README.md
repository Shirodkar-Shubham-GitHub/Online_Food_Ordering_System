# Lett' uce Eat - Online Food Ordering System

## Overview
   Welcome to Lett' uce Eat, an online food ordering system where users can browse delicious food items, add them to their cart, and place orders with ease. This project includes features for both users and administrators, with a focus on secure authentication and smooth order management. The live version of the application is available [here](https://shubham373shirodkar.pythonanywhere.com/).
    
## Features
### User Features
* Email Verification: Secure your account with email verification during registration.
* Google Login: Login easily using your Google account.
* Order Food: Browse and order from a variety of food items.
* Add to Cart: Add items to your cart before placing an order.
* Review Items: Leave feedback on food items you've ordered.
* Contact for Cancellation: Reach out to cancel your order if needed.
* Dashboard: View and edit your profile, check your cart and orders, and change your password.

### Admin Features
* Session Management: Manage active sessions for admins and users.
* Manage User Profiles: View and manage user accounts.
* Manage Orders: Oversee and manage all customer orders.
* Manage Contacts: Handle customer inquiries and order cancellations.
* Add Food Items: Add new food items to the menu.

## Updates

* Google Login: Added Google login integration for easier user access.
* Session Management: Implemented session management for users and admins for better security and control.
* Home Page Update: Limited the menu list on the home page to a maximum of three items.
* Menu Module: Created a separate Menu module with the following features:
  * Search Bar: Allows users to search for menu items.
  * Pagination: Displays a maximum of six items per page.
* Dashboard Enhancements: Introduced a dashboard that includes:
  * User Profile: View and edit your profile.
  * My Cart: Access your cart.
  * My Orders: Track your orders.
  * Change Password: Update your account password.
  * CSS Animations: Added smooth animations for better user experience.
* Database Migration: Migrated the database from SQLite3 to MySQL for improved performance and scalability.
* Deployment: Deployed the project using MySQL on PythonAnywhere for reliable hosting.

## Technologies Used
* Python
* Django
* MySQL
* Bootstrap5

## Installation
 #### 1. Clone the Repository:
    git clone https://github.com/Shirodkar-Shubham-GitHub/Online_Food_Ordering_System
    cd Online_Food_Ordering_System
 #### 2. Create a Virtual Environment:
    python -m venv my_env
    my_env\Scripts\activate
 #### 3. Install Dependencies:
    pip install -r requirements.txt
 #### 4. Apply Migrations:
    python manage.py makemigrations
    python manage.py migrate
 #### 5. Create a Superuser (for admin access):
    python manage.py createsuperuser
 #### 6. Run the Development Server:
    python manage.py runserver

## Project Structure

The following is the structure of the Django project:

```bash
Online_Food_Ordering_System/
│
├── Foods_Ordering/              # Main Django project folder
│   ├── __init__.py
│   ├── asgi.py
|   ├── middleware.py
|   ├── session_middleware.py
│   ├── settings.py           # Project settings (e.g., database, middleware)
│   ├── urls.py               # Main URL routing for the project
│   ├── wsgi.py
│
├── main/                  # Django app folder
│   ├── migrations/           # Migrations folder (auto-generated)
|   ├── static/
|   ├── templates/
|   ├── templatetags/
│   ├── __init__.py
│   ├── admin.py              # Django admin interface settings
│   ├── apps.py
│   ├── models.py             # Database models
│   ├── tests.py              # Unit tests for the app
│   ├── urls.py               # App-specific URL routing
│   ├── views.py              # Business logic and view functions
|
├── accounts/                  # Django app folder 
│   ├── migrations/           # Migrations folder (auto-generated)
|   ├── templates/
│   ├── __init__.py
│   ├── admin.py              # Django admin interface settings
│   ├── apps.py
│   ├── models.py             # Database models
│   ├── tests.py              # Unit tests for the app
│   ├── urls.py               # App-specific URL routing
│   ├── views.py              # Business logic and view functions
│
├── media/                   # The files uploaded by users on the system.
│
├── my_env/                  # A directory with particular  file structure.
│
├── manage.py                 # Django command-line utility
│
├── requirements.txt          # Python dependencies for the project
│
└── README.md                 # Project documentation (this file)
```

## Deployment
   This project was deployed on PythonAnywhere using MySQL as the database. Follow the platform's instructions to deploy your Django application.
   
## Usage
#### 1. Registration and Login:
   * Register a new account with email verification or use Google login.
   * Login to your account using your credentials.
#### 2. Browsing and Ordering:
   * Browse the menu (limited to three items on the home page) or use the Menu module with search and pagination to explore more items.
   * Add your favorite items to the cart and place an order.
#### 3. Dashboard:
   * Manage your profile, cart, orders, and password from the dashboard.
#### 4. Admin Access:
   * Login to the admin panel to manage users, orders, and food items.

## Testing
    python manage.py test

## Future Improvements

### 1. **Payment Gateway Integration for Order Payments**

We plan to implement a secure payment gateway to enhance the checkout experience.
