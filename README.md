# playwright_flight
This is a simple playwright demo using page objects.

In your project directory, create directories named dev and venv.

Create and activate python virtual environment.
$ py -m venv venv
$ venv\Scripts\activate.ps1

Install playwright, pytest, and pytest plugin.
$ py -m pip install playwright
$ py -m pip install pytest
$ py -m pip install pytest-playwright

Store list of dependencies in file named requirements.txt
$ py -m pip freeze > requirements.txt

Install browsers
$ playwright install

For more information on installation see https://playwright.dev/python/docs/intro

Execute in visibly rendered browser with a second pause after each call.
$ py -m pytest tests --headed --slowmo 1000
