# My Flask REST API Boilerplate and Set Up

An opinionated boilerplate and set up for a Flask REST API project. I have personally used this set up to bootstrap Flask projects extremely quickly. Please feel free to use it!

------------

### My boilerplate & set up may be useful to you IF:
- Your Flask projects normally have an enormous, monolithic `app.py` file.
- You're looking for opinions on project organization and modularity.
- You're looking to bootstrap a REST API project for a personal project or coding challenge.
- You're looking to play around with a ready-to-go Flask application.
- You want to try out Pytest, an extremely simple and expressive testing library.
- You want to try your hand in at configurations-based programming.
- You want to see an example of a factory pattern.
- You want to learn how to set up a basic testing fixture.


------------

## Project Features

#### Separation of concerns:
- Separate directories for routes, tests, models, and helpers.
- Application factory pattern - For ease of feeding different sets of configurations (.cfg files) and setting up testing fixtures. Check it all out in /project/__init__.py
- Using Flask blueprints to separate groups of routes.
- Utilzing helper classes to abstract heavy logic from the routes (with a provided example).

#### Initial testing configurations:
- Testing with Pytest - For clear, expressive testing.
- Sample testing fixture - For testing a separate instance of a Flask application, connected to its own database and set with its own unique conditions.
- Sample tests for the app, routes, and configuration settings.

#### Works right out of the box
1. Clone the repo
2. Set up virtual environment - `python3 -m venv venv`
3. Activate virtual environment - `source venv/bin/activate` (might be different for Windows)
4. Install dependencies - `pip install -r requirements.txt`
5. Set to development - `export FLASK_ENV=development`
6. Run the app - `flask run`

By default, Flask runs on port 5000 on localhost. Try testing the `/ping` route to see if it's running!

------------

## Installation Requirements
#### Necessary:
- Python 3
- pip
- Python virtual environments

#### Optional:
- Relational Database - This boilerplate is tested with PostgreSQL. Using with this with a database will require additional set up.

------------

#### Set up with a database:
This project is designed to work with PostgreSQL, or any Relational Database that is compatible with SQL Alchemy. The project has database-related code commented out by default. Additional set up is required (which I will outline at a future date). Search for comments throughout the project that say "USE THE FOLLOWING IF SETTING UP PROJECT WITH A DATABASE".

#### Set up without a database:
If you don't need to set up a project with a database: you can 
- You can delete all commented-out code under the caption: "USE THE FOLLOWING IF SETTING UP PROJECT WITH A DATABASE".
- You can also delete the models directory.
- You can delete seed.py.
