# frisbee-turnaje
Štatistiky z frisbee turnajov

# How to install

Install python 2.7, then:

    pip install Django
    pip install django-suit==0.2.15
    pip install django-tables2
    pip install django-super-inlines
    sudo apt-get install python-mysqldb

Create database frisbee with utf8 charset, e.g.:
    
    CREATE DATABASE frisbee DEFAULT CHARACTER SET utf8;

Edit the settings.py (insert your db user and password):

    DATABASES = {
      'default':{
          'ENGINE':'django.db.backends.mysql',
          'NAME': 'frisbee',
          'USER': '...',
          'PASSWORD': '...',
          'HOST': '127.0.0.1',
          'PORT': '3306',
      }
    }
    
Then run following commands:

    ./manage.py migrate
    ./manage.py createsuperuser
    ./manage.py runserver
