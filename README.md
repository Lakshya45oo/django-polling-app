# Polling App (Django)
A Django polling application. Visitors can view polls and results, registered users can vote, and the admin manages polls from the Django admin panel.

## How to run the project
Open a terminal in the project folder and run:

```
pip install Django
python manage.py migrate
python manage.py runserver
```

Then open in the browser:
- App: http://127.0.0.1:8000/polls/
- Admin: http://127.0.0.1:8000/admin/

## Using the app
- Anyone can view polls and results.
- To vote, click **Sign up** and create a new account (any username and password).
- The project includes 5 sample polls in db.sqlite3.

## Technologies
Python 3.14, Django 6.1, SQLite
