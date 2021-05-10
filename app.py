from project import create_app

# This project is designed to use a directory named /instance for separate
# configuration settings. You can make configurations for applications in
# different environments.

# By using the create_app method, we are creating a Flask instance and feeding
# a config (.cfg) file into it. By default, this Flask app will run on the
# development configuration settings. The create_app factory method can be
# found in /project/__init__.py.

# By default the configuration files will barely differ.
# When deploying this project, you may want to set up a separate production
# configuration file that utilizes environment variables.

config_settings = "development.cfg"

# Instantiate the app. This particular line will run when using the
# command "flask run" in the Terminal
app = create_app(config_settings)
