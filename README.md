# YNDC Board Ups and Neighborhood Surveys

An application to help track and manage property boardups and cleanups for the [Youngstown Neighborhood Development Corporation](http://yndc.org/).

## Overview
1. Install python environment
2. Install python library requirements
3. Local settings
4. Database and migrations
5. Create a user

## Python environment
It is recommended that you use [virtualenv](https://pypi.python.org/pypi/virtualenv) for your python environment. [virtualenv-burrito](https://github.com/brainsik/virtualenv-burrito) is an easy way to get a working python development environment. After installing virtualenv-burrito, use the command `mkvirtualenv` to create a new venv. 

## Python requirements
Once inside your venv you need to install the python dependencies. The command `pip install -r requirements.txt` should do it.

## Local settings
`cd` into `yndc/settings` and use the local settings template to create your local settings file. `cp local.py.example local.py`. This changes the development environment to use Django's FileSystemStorage for file uploads.

## Database and migrations
You can currently use sqlite as your development database. Run `./manage.py migrate` to set it up.

## Create a user
Run `./manage.py createsuperuser` to create a superuser.

## Run server
Run `./manage.py runserver` to run the server. Hit it in the browser at `localhost:8000`.
