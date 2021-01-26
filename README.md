# DjangoAsync
> Async Views in Django 3.1 example

###### About Django Async
Django has support for writing asynchronous (“async”) views, along with an entirely async-enabled request stack if you are running under ASGI. Async views will still work under WSGI, but with performance penalties, and without the ability to have efficient long-running requests

### Run project in your local dev server.
- Python 3-8
- Django 3.1.5
```base
git clone https://github.com/mbrsagor/djangoAsync.git
cd djangoAsync
virtualenv venv --python=python3.8
source venv/bin/activate
pip install -r requirements.text
./manage.py migrare
./manage.py createsuperuser
./manage.py runserver
```
