# Django Private Chat
> A simple messenger written essentially in Python and Django

Private Chat is a open source project what makes the function of an instant messenger. This is done with a back-end system written essentially in Python and Django.

Available on: [privatechatdemo.herokuapp.com](http://privatechatdemo.herokuapp.com)

## How is the content made dynamic in the pages?

In order for the page content to be dynamic without reloading, options were used for the client side. JavaScript along with the JQuery library has important roles for this. In the chat room, the system makes periodic requests for information about new messages and verification of read messages. This is done with AJAX requests.

![aqui deveria aparecer um icone de pessoa](https://4.bp.blogspot.com/-UNZIh6tkU7A/WFDywvLgf-I/AAAAAAAABdo/5EvlhOIstFAV7YvF4tYJLSTEHXg3DosbwCLcB/s1600/readme2.jpg “Chat Window”)
> Chat window

## How to install?

The code in this repository is shaped for the production environment, but if all dependencies are installed, it also runs in the development environment.

First of all, have pip and virtualenv installed.

Sequence of steps:

1. Create a virtualenv for the project by prescribing Python 3:<br>
```virtualenv --python = python3 [environment name]```

2. Enter the virtualenv folder and activate it:<br>
```source bin/activate```

3. Make the clone or download the project into the part of the newly created virtualenv.

4. Within the project root, install pip dependencies:<br>
```pip install requirements.txt -r.```

5. Run the ```python manage.py makemigrations``` and ```python manage.py migrate``` to create the application tables.

6. To start run ```python manage.py runserver.``` 

## Example usage

Basically what the system does is identify a user action and access the database through ajax requests and bring, add or delete data to the page without having to reload the page.
There are three essential files in the chat system:

```chat.js``` <br>
```views.py``` <br>
```models.py``` <br><br>

Requests are made in the ```chat.js``` file using the JQuery library. The use of the ```setInterval()``` is done in the requests of new messages and the confirmation of reading the message.
Each ajax function does a GET or POST has access to a view within ```views.py``` through a route. In screen views are made of shields not to accept requests that are not AJAX and that are not of the logged in user.
For views to return information to ```chat.js```, instances of the ```models.py``` class Message functions are instantiated.

## What was used

### Used on front-end:
* [Bootstrap 3](http://getbootstrap.com.br/)
* [JQuery](https://jquery.com/)
* [nanoScroller.js](https://jamesflorentino.github.io/nanoScrollerJS/)
* [slick](http://kenwheeler.github.io/slick/)

### Used on back-end
* [Python 3.4](https://www.python.org/)
* [Django 1.10.4](https://www.djangoproject.com/)

### Used on deploy
* [Heroku](https://www.heroku.com/)

## About contributions

The project is open for contributions, preferably with pull requests.

## doubts?

Contact me on diegofernanfo5672@gmail.com

:)
