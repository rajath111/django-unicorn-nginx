## Objective

To Create an sample Django Rest API application and deploy it in a Linux server (Gunicorn and Ngnix).

### Running Using Default Django server

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

### Running Django application using Gunicorn

Gunicorn is python's WSGI HTTP server for Unix. It's a pre-frok worker model.

Perform above defined steps from 1 to 5. And then execute below steps.

1. Run server using gunicorn
   cd sample_api/
   gunicorn 'sample_api.wsgi:application'

Observation: Gunicorn does not serve static content.


### Serving Django Application using Ngnix server

This steps you can follow to run Nginx server in Linux platform. Please refer this link for windows platform - https://nginx.org/en/docs/windows.html.

1. Install Ngnix
   sudo apt update
   sudo apt install nginx
2. Configure NgnixThe configuration can be found in nginx_v1.config file. Copy its content to /etc/nginx/nginx.conf file.
3. Run nginx server
   sudo service nginx start


### Validating

Run below command to test wheter the server is running.

wget http://localhost/test

You will get response like `Running Successfully! `.


### Future Taks

1. Open port 80 and access Django service from internet
2. Add TLS encryption
3. Create DNS entry for custom domain
