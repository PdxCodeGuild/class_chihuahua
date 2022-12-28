# README

Welcome to the commerce application built with Django!

In this application, logged users can add products to their carts. Staff users have the additional ability to create their own products and manage them through the Django admin panel. However, staff users can only see and modify the products that they themselves have created, thanks to the modification of the admin behavior through the `MyModelAdmin` class.

The `MyModelAdmin` class overrides the `get_queryset` and `formfield_for_foreignkey` methods in order to filter the queryset of products shown in the Django admin panel based on the user who is currently logged in. If the user is a superuser, they can see and modify all products. If the user is a staff user, they can only see and modify the products that they themselves have created.

To use this application, simply install the required dependencies and run the Django development server.

# Installation

Install the required dependencies by running the following command:

```bash
pip install -r requirements.txt
```
# Usage
Run the Django development server by using the following command:

```bash
python manage.py runserver
```

Then, visit http://localhost:8000 in your web browser to access the application.

# Credits

This application was built with Django and the modifications to the admin behavior were implemented using the MyModelAdmin class.

License
This project is licensed under the MIT license.