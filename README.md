# django-authentication

## Deployed at https://djangoauthbyazaz.herokuapp.com/


## How to Deploy

  #### 1. git clone https://github.com/Technosoft-Solutions/django-authentication.git
  #### 2. login on heroku
  #### 3. create heroku app using heroku-cli
  #### 4. run git push heroku main

  #### This will start a automatic process of deployment on heroku with necessary builds, installations and configurations like migrations.
  

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
