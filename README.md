# Lett' uce Eat - Online Food Ordering System

## Overview
   Welcome to Lett' uce Eat, an online food ordering system where users can browse delicious food items, add them to their cart, and place orders with ease. This project includes features for both users and administrators, with a focus on secure authentication and smooth order management. The live version of the application is available [here](https://shubham990shirodkar.pythonanywhere.com/).
    
## Features
### User Features
* Email Verification: Secure your account with email verification during registration.
* Order Food: Browse and order from a variety of food items.
* Add to Cart: Add items to your cart before placing an order.
* Review Items: Leave feedback on food items you've ordered.
* Contact for Cancellation: Reach out to cancel your order if needed.

### Admin Features
* Manage User Profiles: View and manage user accounts.
* Manage Orders: Oversee and manage all customer orders.
* Manage Contacts: Handle customer inquiries and order cancellations.
* Add Food Items: Add new food items to the menu.

## Technologies Used
* Python
* Django
* SQLite3
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

## Testing
    python manage.py test
## Future Improvements

### 1. **Payment Gateway Integration for Order Payments**

We plan to implement a secure and reliable payment gateway to enable users to complete their orders directly on the platform. This enhancement will streamline the checkout process and improve user experience.

#### Planned Features:
- **Multiple Payment Methods**: Integration of popular payment options such as credit/debit cards, UPI, net banking, and mobile wallets.
- **Payment Gateways**: Implementation of widely used payment gateways like PayPal, Razorpay, or Paytm.
- **Secure Transactions**: Ensure that all transactions are encrypted and meet the required security standards, such as PCI-DSS compliance.
- **Order Confirmation and Receipts**: Automatically generate order receipts and send email confirmations after successful payments.
- **Test Environment**: A sandbox environment for testing the payment process before deployment to production.

#### Future Development Phases:
1. **Research and Select Payment Gateway**: Evaluate and choose the payment gateway based on transaction fees, country-specific availability, and ease of integration.
2. **Backend Integration**: Use the payment gateway's API to securely process payments in the backend.
3. **Frontend Checkout Page**: Design a user-friendly checkout page that allows users to select their preferred payment method.
4. **Testing and Debugging**: Test the entire payment process in a sandbox environment before going live.
5. **Deployment**: Once the payment gateway integration is completed and tested, it will be deployed to the production environment.

Expect to implement the payment gateway within the next few releases.
