# Djangorestframework-tutorial
## Build the official tutorial app

## QUICK INSTALL
Look at these files
```
urls.py
views.py
models.py
settings.py
```
You can ignore the other ones, they have extra steps from past work in the parts branches.

Run this to clone down this repo
`git clone https://github.com/Gregorio-Moreta/djangorestframework-tutorial/tree/example`

Create your virtual environment
`pipenv shell`

Install dependencies in your virtual envioronment
this should be everything you need but the second command is all the dependencies in case you don't have a Pipfile
`pipenv install` 

Or in case you delete your Pipfile
`pipenv install django djangorestframework psycopg2-binary httpie`

The psycopg2-binary is for SQL, we don't need it now, but you would if your made your database using SQL like we have in the past.

You can skip a lot of the configuration stages because I have done it for you already essentially. You still need to set up your own psql database and users though.

#### Start the Server
We can run `python manage.py runserver` to start the server. We can run this right now to check that our project runs without errors. For now it will load a nice homepage and not do much else.

### Setting Up Postgresql

By default Django uses SQLite. For now we will keep it that way. 

#### DATABASE
When we update our model, be sure to delete the db.sqlite3 file, re-run migration commands.
```
When that's all done we'll need to update our database tables. 
Normally we'd create a database migration in order to do that, but for the purposes of this tutorial, let's just delete the database and start again.

rm -f db.sqlite3
rm -r snippets/migrations
python manage.py makemigrations snippets
python manage.py migrate
You might also want to create a few different users, to use for testing the API. The quickest way to do this will be with the createsuperuser command.

python manage.py createsuperuser
```

## Creating users
I created users two users with the credentials 
- user1 
- user2

Both have the password `password`

Create your own users
```
python3 manage.py createsuperuser user3
```
Add in the password manually

Our databases in tutorial/settings.py should look like this
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

### Settings py file

Our INSTALLED_APPS in tutorial/settings.py should look like this 
```

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'snippets'
]
```
Our REST_FRAMEWORK in tutorial/settings.py should look like this 

```
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}

```