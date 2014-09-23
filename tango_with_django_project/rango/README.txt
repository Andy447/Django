- __init__.py --> a blank Python script whose presence indicates to the Python interpreter that the directory is a Python package;

- models.py --> a place to store your application¡¦s data models, where you specify the entities and relationships between data;

- tests.py --> where you can store a series of functions to test your application¡¦s code; and

- views.py --> where you can store a series of functions that take a clients¡¦s requests and return responses.

views.py and models.py are the two files you will use for any given application, and form part of the main architectural design pattern employed by Django, i.e. the Model-View-Template pattern. You can check out the official Django documentation to see how models, views and templates relate to each other in more detail.
(https://docs.djangoproject.com/en/1.5/intro/overview/)