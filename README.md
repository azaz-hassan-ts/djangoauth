# django-auth
## Deployed at https://djangoauthbyazaz.herokuapp.com/

# Python: Getting Started

A barebones Django app, which can easily be deployed to Heroku.

This application supports the [Getting Started with Python on Heroku](https://devcenter.heroku.com/articles/getting-started-with-python) article - check it out.

## Running Locally

Make sure you have Python 3.9 [installed locally](https://docs.python-guide.org/starting/installation/). To push to Heroku, you'll need to install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli), as well as [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).

```sh
$ git clone https://github.com/azaz-hassan-ts/djangoauth.git
$ cd djangoauth

$ python3 -m venv getting-started
$ pip install -r requirements.txt

$ createdb django_auth

$ python manage.py migrate
$ python manage.py collectstatic

$ heroku local
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku main

$ heroku run python manage.py migrate
$ heroku open
```
or

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)


## How to hit apis

### Got to https://djangoauthbyazaz.herokuapp.com/rest-auth to find url patterns to hit

### To Register User
Go to Postman and enter this url: https://djangoauthbyazaz.herokuapp.com/rest-auth/registration/ \
Select Post method, in body tab, select raw and JSON from dropdown format\
Use this json format:
```
{
    "username": "",
    "email": "",
    "password1": "",
    "password2": ""
}
```

Enter data and send request to register user\

### How to login
On Postman: Enter this URL: https://djangoauthbyazaz.herokuapp.com/rest-auth/login/ \
Select POst, body, raw and json format\
Use this json format:\
```
{
    "username": "",
    "email": "",
    "password": ""
}
```
Use the username, email and password used to register here and send request, it will send back a token which indicates, registration and login is successful. 

## Documentation

For more information about using Python on Heroku, see these Dev Center articles:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)


