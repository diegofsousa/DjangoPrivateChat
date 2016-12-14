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

6. To start run ```python manage.py runserver```.
