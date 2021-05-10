"""
Sample helper class named "General". You can delete this later.

I'm using this file as an example for how you might separate project concerns.
Having this helper directory may help you separate heavy logic from route files.

In other words, route files should only have route-related logic.
Heavier logic can be abstracted out into methods.

...this is just my humble opinion, of course.

Make sure to import helpers into project/helpers/__init__.py for ease of use!
"""


class General:
    @classmethod
    def sample_helper(cls):
        """
        Sample helper method

        :return: Default API Message
        """
        return "Thank you for using nbry's Flask Boilerplate!"
