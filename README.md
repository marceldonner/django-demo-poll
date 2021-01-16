# django-demo-poll

This is a simple recreation of the official [Django tutorial](https://docs.djangoproject.com/en/3.1/intro/tutorial01/).

## setting up django-demo-poll (terminal)

1. First, simply clone the repository via `git clone`
2. (optinal) Create a virtual enviroment with `python- m venv /path/to/new/virtual/environment` and activate via `"venvname"/bin/activate`
3. Install the required packages with `pip install -r requirements.txt`
4. cd into the `mysite` directory
5. Apply migrations with `python manage.py migrate`
6. Create an admin user for Django Admin with `python manage.py createsuperuser` and set your credentials
7. Start the server with `py manage.py runserver`

## usage

* To access the app enter `http://127.0.0.1:8000/` into your browser, this page should show you an 404 error.
* Access the admin panel at `/admin`, log in and add some questions with answers to the list.
* If the question has a text, choices and has it's publish date specied in the past click on `save` and access it at `/polls`.
* Here you can see the available polls. Click on one of them to see the answer options, select one, press vote and see the results.
