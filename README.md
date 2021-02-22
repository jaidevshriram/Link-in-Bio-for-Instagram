# Link-in-Bio-for-Instagram
A free version of linkin.bio for organizations to attach links to instagram posts. Groups may use this code to set up a website which mimics linkin.bio. 

## Usage

1. Create a super user
2. Visit /login and enter credentials
3. Visit /create-post to create a new post
4. Visit / to view all posts so far.

## Set up

Create a python3 virtual environment and [https://docs.djangoproject.com/en/3.1/topics/install/](install Django). Then, install the packages listed in requirements.txt. Once the packages are installed, run the following:

<code>
  python manage.py migrate
</code>

Then, you can run the application using 

<code>
  python manage.py runserver
</code>

## Motivation

The application has currently been built for a student organization at IIIT Hyderabad - Ping! but could easily be modified for other purposes.
