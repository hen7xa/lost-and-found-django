# Lost and Found

A small Django web app where students can post lost and found items for their college.

## Features
- Post a lost or found item (title, description, location, status, contact info, date)
- Home page lists all items, newest first
- Filter the list by Lost or Found
- Admin site to manage items

## Tech
Python, Django, SQLite, HTML and CSS

## Run it locally
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```