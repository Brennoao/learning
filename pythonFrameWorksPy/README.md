# CODES FOR MANIPULATION

## virtual environmet

> create environment
>> ~~~
>> python3 -m venv name_environmente
>> ~~~

> activate environment
>> ~~~
>> source venv/bin/activate
>> ~~~

> deactivate environment
>> ~~~
>> deactivate
>> ~~~

## django

> new project
>> ~~~
>> django-admin startproject biblioteca .
>> ~~~

> new app inside project
>> ~~~
>> python3 manage.py startapp name_the_app
>> ~~~

> generate file migration
>> ~~~
>> python3 manage.py makemigrations
>> ~~~

> create table in the database
>> ~~~
>> python3 manage.py migrate
>> ~~~

> admin codes
>> create admin user
>>> ~~~
>>> python3 manage.py createsuperuser
>>> ~~~