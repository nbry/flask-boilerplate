"""
Testing default routes from boiler plate code.
"""


def test_general_helper_route(client):
    """
    GIVEN an instance of the flask app
    WHEN user visits the /helper route
    THEN ensure a message is returned!
    """
    res = client.get('/helper')
    res_message = res.json['message']

    assert res.status_code == 200
    assert res_message == "Thank you for using nbry's Flask Boilerplate!"
