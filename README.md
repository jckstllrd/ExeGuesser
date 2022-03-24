# Group-Project-Game
A web game created for our Software Engineering module.

Python version 3.10.0 or later is required for optimal use of the app. If this version is not installed, it can be done so here: https://www.python.org/downloads/release/python-3100/

Django is required for the app to function. Details on how to install Django can be found here: https://docs.djangoproject.com/en/4.0/topics/install/

In order to begin the app, the following command needs to be launched at command line interface: 
$ python manage.py runserver 

Before the app is launched, the following 2 commands need to be run in order for the app to work:
$ python manage.py makemigrations
$ python manage.py migrate

The shell will respond with a message containing a web address (e.g. http://127.0.0.1:8000). This is the address where the game will run from. 
The server will run until a CTRL + BREAK is put into the command line.

There are two types of accounts: users and game keepers. Users are able to join games created by game keepers, and play said games.

Game keepers must upload their selection of images of chosen locations once the app has been started before any games can be played. This must be done on every new device a game keeper uses if they want to run the app from.

Upon start up, the user is given the option to register an account or log in to an existing one. Once signed into an account, they have the option to create a game (if they are a game keeper), or join an existing one. Once the game begins, the user is prompted with an image of a location on campus and the timer begins. The user can obtain a new location upon reloading the game. (explain how the game works)
