from entities.user import User
from repositories.user_repository import UserRepository


class UserService:
    """Class that the application uses to store information about users and connect to the database.

    Attributes:
        current_user: A user object that tells the current logged in user.
        user_repo: A UserRepository object that enables this class to connect to the database.
    """

    def __init__(self, user_repo=None):
        """The contructor that initiates the UserService object"""
        self.current_user = None
        if user_repo is None:
            self.user_repo = UserRepository()
        else:
            self.user_repo = user_repo

    def create_user(self, username):
        """Creates a user and saves it to the database"""
        self.user_repo.create(User(username))

    def remove_user(self, user_id):
        """Removes a user from the database specified by user_id"""
        self.user_repo.delete_by_id(user_id)

    def login(self, user_id):
        """Sets the current user"""
        self.current_user = self.user_repo.find_by_id(user_id)
        return self.current_user

    def logout(self):
        """Sets the current user as None"""
        self.current_user = None

    def get_all(self):
        """Returns a list of all of the users"""
        return self.user_repo.find_all()
