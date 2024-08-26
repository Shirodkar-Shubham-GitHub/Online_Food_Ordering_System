# Lett' uce Eat - Online Food Ordering System

## Overview
   Welcome to Lett' uce Eat, an online food ordering system where users can browse delicious food items, add them to their cart, and place orders with ease. This project includes features for both users and administrators, with a focus on secure authentication and smooth order management.
    
## Features
## User Features
* Email Verification: Secure your account with email verification during registration.
* Order Food: Browse and order from a variety of food items.
* Add to Cart: Add items to your cart before placing an order.
* Review Items: Leave feedback on food items you've ordered.
* Contact for Cancellation: Reach out to cancel your order if needed.

## Admin Features
* Manage User Profiles: View and manage user accounts.
* Manage Orders: Oversee and manage all customer orders.
* Manage Contacts: Handle customer inquiries and order cancellations.
* Add Food Items: Add new food items to the menu.

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
    python manage.py migrate
 #### 5. Create a Superuser (for admin access):
    python manage.py createsuperuser
 #### 6. Run the Development Server:
    python manage.py runserver
    
## Deployment
   This project is ready to be deployed on PythonAnywhere or any other hosting platform. Follow the platform's instructions to deploy your Django application.
## Usage
#### 1. Registration and Login:
   * Register a new account with email verification.
   * Login to your account using your email and password.
#### 2. Browsing and Ordering:
   * Browse the menu and add your favorite items to the cart.
   * Place an order and receive an email confirmation.
#### 3. Admin Access:
   * Login to the admin panel to manage users, orders, and food items.

## Contributing
   We welcome contributions! Please fork the repository and submit a pull request with your improvements.
## License
   This project is licensed under the MIT License - see the LICENSE file for details.
