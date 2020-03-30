----------------------
Course Prerequisites
----------------------
    - Right Attitude
    - Background in core python programming
    - OOP Basics
    - 


----------------------
Why Django
----------------------

- widely used 

- open source 

- high level, easy to learn and pickup - encourages rapid development and clean design

- allows you to focus on building your app without re-inventing the wheel


MAIN FEATURES
-----------------------------
    - Fast - designed to help developers take apps from concept to completion fast.

    - Secure - Helps developers avoid common security mistakes.

    - Scalable - has ability to quickly and flexibly scale.


- Follows the MVC pattern

Model View Controller


-----------------
Installation
-----------------
1. Check if django is installed

python(3) -m django --version  


if not installed

Create a Virtual Environment
- acts as dependencies to the Python-related projects.

-  self contained or an isolated environment where all the Python-related packages and specific required versions of the projects are kept.

- Older newer versions of python co-work

    a) create project folder (mkdir my_school_project)

        cd to project folder

    b) run command python(3) -m venv env

    NB: Python will not support version 2 after the year 2020.

    c) run command ls - view environment 

    d) activate the environment 

        source env/bin/activate

    e) install django  in the virtual environment

        - pip install django



2. Create a django project

using django-admin startproject

    - django-admin startproject my_bank

    - Project with many files created

    a) cd to newly created folder
    b) run the project with :python3 manage.py runserver 

    or python3 manage.py runserver 8080

    NB: ensure environment is created/activated else you will get a serious error

- Access the website on url & port

NB: repeat the process until you are comfortable


--------------------------------
Folder Structure Explained
--------------------------------
1. my_bank_project/ 

 - root directory - contains project files

2. env
    - Virtual environment folder 

3. my_bank /
    - project name

4. manage.py
  - command utility for interacting with django
  
5. The inner my_bank/ 

    - Python package for the project.
    - Name can be used to import anything inside it (e.g. my_bank.urls).

6. my_bank/__init__.py: 

    - empty file, tells Python that this directory should be considered a Python package.
    
7. my_bank/settings.py:

    - Settings/configuration for the project.
    - e.g DB settings

8. my_bank/urls.py: 
    - The URL declarations for the project;

9. my_bank/asgi.py: An entry-point for ASGI-compatible web servers to serve your project.
    - Asynchronous Server Gateway Interface)
    - provide a standard interface between async-capable Python web servers, frameworks, and applications.

    - WSGI provided a standard for synchronous Python apps, 
    - ASGI provides one for both asynchronous and synchronous apps, 
    with a WSGI backwards-compatibility implementation and multiple servers
     and application frameworks.

10. my_bank/wsgi.py: An entry-point for WSGI-compatible web servers to serve

    - WSGI provided a standard for synchronous Python apps, 


------------------------
3. Starting the new Project Module (2 Step)
------------------------
My_Bank 
Customers
Accounts 
Currency

(my_school)
Schools - Define Models, urls, views etc
Students
Subjects


1. python(3) manage.py startapp app_name

    - python3 manage.py startapp customer
    - python3 manage.py startapp accounts
    - python3 manage.py startapp customer
    
    - django can have many apps to the single project where each app serves as single and 
    specific functionality to the particular project.


2. Make our project know about our newly created app 
 
    update the file 
    'my_bank/settings.py' INSTALLED_APP section.


3. Configure DB Connection

Database setup

We use Mysql for this purpose.

if missing mysqlclient run below in virtual env

pip install mysqlclient

SETTINGS Database
-------------------
-     'default':{
        'ENGINE': 'django.db.backends.mysql',
        'HOST':'localhost',
        'PORT':3306,
        'NAME':'codev_django',
        'USER':'root',
        'PASSWORD':'pass'
    }



CREATING MODELS
-------------------

class Student(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100,unique=True)
    id_number = models.CharField(max_length=10)
    admission_date = models.DateField()
    age = models.IntegerField()


    class Meta:
    db_table = 'tbl_customer'
    managed = True #flush or sync db



NB: Object Relational Mapper(ORM)

Making a Migrations
1. python3 manage.py makemigrations

Migrating to the Database ('Also Creates the Database tables')

2. python3 manage.py migrate


NB: Login to database and confirm is tables are created



-------------------
DJANGO ADMIN
-------------------
- Used for content management

/admin url

--------------------
Create a Super user 
--------------------


- python3 manage.py createsuperuser

- enter required details

- Login to the Admin Page

- Make the app modifiable by admin

    - 
    modify admin.py in respective module
    from .models import Account
    # Register your models here.

    # Register your models here.
    admin.site.register(Account)


We build our model Bank based on the previous classes.
------------------------
Functionality 
------------------------
    - A public site that allows customers to access.

    - An admin site that lets the bank staff to add, change, and delete customers.

    - Capture Customers

    - Create Accounts for Customers

    - Assign Currency to Account

    - Allow Cutomer Load Money 

    - Allow Customer to Check Balance

    - Allow Customer Transfer to Another Customer.






