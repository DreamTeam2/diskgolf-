# frisbee-turnaje
Štatistiky z frisbee turnajov

# How to install

Install python 2.7, then:

    pip install -r requirements.txt
    sudo apt-get install python-mysqldb

Create database frisbee with utf8 charset, e.g.:
    
    CREATE DATABASE frisbee DEFAULT CHARACTER SET utf8;

Copy custom_settings.py.template to custom_settings.py (insert your db user and password):

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

    ./manage.py makemigrations
    ./manage.py migrate
    ./manage.py createsuperuser
    ./manage.py runserver
