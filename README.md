# e-commerceproject
This project illustrates a Django application for managing customers and their orders in e-commerce.

## How to set up the environment
1.I installed the latest version of python and pip. 
I crosschecked whether they have been installed by running the following commands:
i) For python I used the command python -- version.
ii) For pip I used the command pip -- version.

2.I created a virtual environment inside using the command: python -m venv .venv 

3.I activated the virtual environment using the command: venv\Scripts\activate.bat

4.I installed django by running the command: pip install django
Then I also run the command pip -- list to see whether django is on the list.

5.Next I created a django project by running the command: django-admin startproject ecommerce.

6.Next I created an app by running the command: python manage.py startapp models

7.Inside the models.py file I created a code for both customer and order.
The customer class represents the customer and stores the customer's first name,last name and verifies their email.
The order class represents the customer's order and stores the date of the order and the calculations of the total amount of the order.

8.Next I run the command: python manage.py runserver and a server was created

9.Next I ran these commands:python manage.py makemigrations models
                            python manage.py migrate

10.Next I created a github repository and initialized it with a README.md file.

11.Next I committed my project in my repository and submitted the link of my repository in google classroom.
