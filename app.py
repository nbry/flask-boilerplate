from project import create_app

# Setting up individual config settings for the purposes
# of this assessment is a bit overkill, BUT I believe it's a best
# practice for a production-level app. I also want to emphasize that
# the secret keys I'm using won't be the most secure.
# *
# Separate config settings for different instances of a flask app is
# a great way to aid in setting up testing fixtures in Pytest. For now,
# the configuration files will barely differ.
config_settings = "development.cfg"

# Instantiate the app. This particular line will run when using the
# command "flask run" in the Terminal
app = create_app(config_settings)
