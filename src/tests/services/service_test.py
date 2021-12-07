import unittest
from entities.user import User
from entities.recipe import Recipe
from services.service import (
    Service,
    UsernameExistsError,
    UsernameNotValidError,
    PasswordNotValidError,
    InvalidCredentialsError
)


class FakeUserRepo:
    def __init__(self, users=None):
        self.users = users or []

    def find_all(self):
        return self.users


class FakeRecipeRepo:
    def __init__(self, recipes=None):
        self.recipes = recipes or []

    def find_all(self):
        return self.recipes


class TestTodoService(unittest.TestCase):
    def setUp(self):
        self.service = Service(
            FakeUserRepo(),
            FakeRecipeRepo()
        )

        self.recipe_puuro = Recipe(
            'puuro', [('vesi', '1 l'), ('kaurahiutaleet', '4 dl'),
                      ('suola', '1 tl')]
        )

        self.recipe_keksit = Recipe('keksit', [])
        self.user_hemmo = User('hemmo', 'hauhau')
        self.user_haiku = User('haiku', 'vuh123')

    def login_user(self, user):
        self.service.create_user(user.username, user.password)
