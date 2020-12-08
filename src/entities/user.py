
class User:
    """Class that stores single user's information.

    Attributes:
        id: An integer that is unique identifier for the user.
        username: A string that is user's username
    """

    def __init__(self, username, id=None):
        """Constructor that initiates a new user object"""

        self.id = id
        self.username = username

    def __repr__(self):
        """Defines the string representation of user object"""

        return self.username
