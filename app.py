from project import create_app

# Separate config settings for different instances of a flask app is
# a great way to aid in setting up testing fixtures in Pytest.

# By default.  the configuration files will barely differ.
# When deploying this project, you may want to set up a separate production
# configuration file that utilizes environment variables.
config_settings = "development.cfg"

# Instantiate the app. This particular line will run when using the
# command "flask run" in the Terminal
app = create_app(config_settings)
