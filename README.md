# Librarious (For Thee, Library-holic drinker)

## How to install
    1. Create a virtualenv, enter to virtualenv
    2. ```pip install -r requirements```
    3. ```python manage.py migrate```
    4. There is a workaround to load worldmap data

        Enter a django shell and do as follows,
        >>> from world import load
        >>> load.run()

## How to run?
    1. Enter to virtualenv
    2. ```python manage.py runserver```

## Dependencies
    1. Postgresql. For mac, use Postgres (because it also includes postgis)


## What's inside Librarious
    1. OAuth 2.0
    2. REST API
    3. GIS
    4. Ordering a.k.a. Borrowing book ~should be~ easy
    5. Rating and Review as a Member
    6. Member Login

## How to get client id and secret?

Go to ```/o/applications/register```

Login with your username and password

Descripe your "application" name, set Client Type to *Confidental* and Authorization grant type to *Resource owner password-based*. Don't forget to set Redirect urls as well. And you're all set!

Remember you Client ID and Client Secret!

For more info visit https://django-oauth-toolkit.readthedocs.io/en/latest/


## How to get auth token?

Get Access Token by accessing ```/o/token/```

Send data as follows:

    grant_type=password&username=<your-username>&password=<your-password>

Don't forget to set header:
    Authorization : Basic <your-client-id> <your-client-secret>


If you're in a right path, you'll get result like follows:


    {
        "access_token": "69dLJ5UsfzBRfb0DicDaCnRtRYrDSr",
        "expires_in": 36000,
        "token_type": "Bearer",
        "scope": "read write groups",
        "refresh_token": "IYBosRDlm0cRkNKcvdgFuFtfVQVIgU"
    }


## How to order a book?

FYI, ordering a book is a librarian task! You can do it via CRUD or RESTful API

For RESTful API, you can use ```/api/borrowing/create/``` and your data will look like follows,

    {
        "member": <member-id>,
        "book": <book-id>,
        "due_date": "2019-01-15"
    }

Very simple, huh?


For more documentation visit:

    1. https://django-oauth-toolkit.readthedocs.io/en/latest/
    2. https://docs.djangoproject.com/en/2.1/ref/contrib/gis/
    3. https://www.django-rest-framework.org/

## How to implement GIS?
    Make sure you have loaded worldmap data. If so, go to ```/admin/librarious/worldborder/```


## How to run celery task?
To run celery task, to ```celery -A librarious worker --loglevel=info```
