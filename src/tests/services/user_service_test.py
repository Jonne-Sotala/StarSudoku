import unittest
from build.database_connection import DatabaseConnection
from entities.user import User
from repositories.user_repository import UserRepository
from services.user_service import UserService


class TestUserService(unittest.TestCase):
    def setUp(self):
        connection = DatabaseConnection(test=True).connect_to_database()
        self.user_repo = UserRepository(connection)
        self.user_repo.delete_all()
        self.user_service = UserService(self.user_repo)

    def test_create_user(self):
        self.user_service.create_user('Jonne')
        users = self.user_repo.find_all()
        self.assertEqual(1, len(users))
        self.assertEqual('Jonne', users[0].username)

    def test_remove_user(self):
        self.user_service.create_user('Jonne')
        user_id = self.user_repo.find_all()[0].id
        self.user_service.remove_user(user_id)
        users = self.user_repo.find_all()
        self.assertEqual(0, len(users))

    def test_login(self):
        self.user_service.create_user('Jonne')
        user_id = self.user_repo.find_all()[0].id
        self.user_service.login(user_id)
        self.assertEqual(user_id, self.user_service.current_user.id)

    def test_logout(self):
        self.user_service.create_user('Jonne')
        user_id = self.user_repo.find_all()[0].id
        self.user_service.login(user_id)
        self.user_service.logout()
        self.assertEqual(None, self.user_service.current_user)

    def test_get_all(self):
        self.user_service.create_user('Jonne')
        self.user_service.create_user('Pekka')
        users1 = self.user_repo.find_all()
        users2 = self.user_service.get_all()
        self.assertEqual(len(users1), len(users2))
