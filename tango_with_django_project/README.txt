The project configuration directory has been created with new Django projects since version 1.4. Having two directories with the same name may seem quite a bit odd, but the change was made to separate out project-related components from its individual applications.

- manage.py --> allows you to run the built-in Django development server to test your work and run database commands. You¡¦ll be using this script a lot throughout the development cycle.

The django-admin.py and manage.py scripts provides a lot of useful, time-saving functionality for you. django-admin.py allows you to start new projects and apps, along with other commands. Within your project directory, manage.py allows you to perform administrative tasks within the scope of your project only. Simply execute the relevant script name without any arguments to see what you can do with each. The official Django documentation provides a detailed list and explanation of each possible command you can supply for both scripts. (https://docs.djangoproject.com/en/1.5/ref/django-admin/)

Changing development server port to 5555: 
python manage.py runserver <your_machines_ip_address>:5555
*Replace <your_machines_ip_address> with your computer¡¦s IP address.

Running the server with your machine¡¦s IP address will enable others to enter in http://<your_machines_ip_address>:<port>/ and view your web application. 