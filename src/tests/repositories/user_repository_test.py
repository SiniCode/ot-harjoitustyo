import unittest
from repositories.user_repository import user_repository
from entities.user import User

class TestUserRepository(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all()
        self.user_hemmo = User('hemmo', 'hemmohau')

    def test_create_user_returns_user(self):
        self.assertEqual(user_repository.create_user(self.user_hemmo), self.user_hemmo)

    def test_find_by_username(self):
        user_repository.create_user(self.user_hemmo)
        user = user_repository.find_by_username(self.user_hemmo.username)
        self.assertEqual(user.username, self.user_hemmo.username)
