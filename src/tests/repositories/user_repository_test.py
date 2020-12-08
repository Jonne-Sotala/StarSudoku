import unittest
from build.database_connection import DatabaseConnection
from repositories.user_repository import UserRepository
from entities.user import User


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        connection = DatabaseConnection(test=True).connect_to_database()
        self.user_repo = UserRepository(connection)
        self.user_jonne = User('Jonne')
        self.user_pekka = User('Pekka')
        self.user_repo.delete_all()

    def test_create(self):
        self.user_repo.create(self.user_jonne)
        users = self.user_repo.find_all()
        self.assertEqual(1, len(users))
        self.assertEqual(self.user_jonne.username, users[0].username)

    def test_delete(self):
        self.user_repo.create(self.user_jonne)
        user_to_delete = self.user_repo.find_all()[0]
        self.user_repo.delete(user_to_delete)
        users = self.user_repo.find_all()
        self.assertEqual(0, len(users))

    def test_delete_by_id(self):
        self.user_repo.create(self.user_jonne)
        user_to_delete = self.user_repo.find_all()[0]
        self.user_repo.delete_by_id(user_to_delete.id)
        users = self.user_repo.find_all()
        self.assertEqual(0, len(users))

    def test_find_all(self):
        self.user_repo.create(self.user_jonne)
        self.user_repo.create(self.user_pekka)
        users = self.user_repo.find_all()
        self.assertEqual(2, len(users))
        self.assertEqual(self.user_jonne.username, users[0].username)
        self.assertEqual(self.user_pekka.username, users[1].username)

    def test_find_by_id(self):
        self.user_repo.create(self.user_jonne)
        user_to_find = self.user_repo.find_all()[0]
        user = self.user_repo.find_by_id(user_to_find.id)
        self.assertEqual(user_to_find.id, user.id)
