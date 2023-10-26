## Objective

To Create an sample Django Rest API application and deploy it in a Linux server (Gunicorn and Ngnix).

#### Running Using Default Django server

1. Install Python
   For this application install python version 3.8 and above.
   Windows: Download and install from python official download page https://www.python.org/downloads/
   Linux:

   sudo apt-get update

   sudo apt-get install python3
2. Create a virtual environment
   python -m venv venv
   python3 -m venv venv
3. Activate python environment
   For Linux: source ./venv/bin/activate
   For Windows: .\venv\Source\active
4. Install required packages

   pip install -r requirements.txt
5. Migrate DB change

   python sample_api/manage.py migrate
6. Run the server

   python sample_api/manage.py runserver

Rendering static content in Django: https://docs.djangoproject.com/en/4.2/howto/static-files/

#### Running Django application using Gunicorn

Gunicorn is python's WSGI HTTP server for Unix. It's a pre-frok worker model.

1. Install Gunicorn
   sudo apt-get update
   sudo apt-get install gunicorn
2. Run server using gunicorn
