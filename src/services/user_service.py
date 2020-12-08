from entities.user import User
from repositories.user_repository import UserRepository


class UserService:
    """Class that the application uses to store information about users and connect to the database.

    Attributes:
        current_user: A user object that tells the current logged in user.
        user_repo: A UserRepository object that enables this class to connect to the database.
    """

    def __init__(self):
        self.current_user = None
        self.user_repo = UserRepository()

    def create_user(self, username):
        self.user_repo.create(User(username))

    def remove_user(self, user_id):
        self.user_repo.delete_by_id(user_id)

    def login(self, user_id):
        self.current_user = self.user_repo.find_by_id(user_id)
        return self.current_user

    def logout(self):
        self.current_user = None

    def get_all(self):
        return self.user_repo.find_all()
