import unittest
from entities.user import User
from entities.recipe import Recipe
from services.service import (
    service,
    UsernameExistsError,
    UsernameNotValidError,
    PasswordNotValidError,
    InvalidCredentialsError
)

class TestService(unittest.TestCase):
    def setUp(self):
        service.delete_everything()
        self.service = service

        self.recipe_puuro = Recipe(
            'puuro', [('vesi', '1 l'), ('kaurahiutaleet', '4 dl'),
                      ('suola', '1 tl')]
        )

        self.recipe_keksit = Recipe('keksit', [])
        self.recipe_lihapullat = Recipe(
            'lihapullat', [('vesi', '1 dl'), ('jauheliha', '400g'),
                           ('muna', '1')]
        )

        self.user_hemmo = User('hemmo', 'hauhau')
        self.user_haiku = User('haiku', 'vuh123')

    def login_user(self, user):
        self.service.create_user(user.username, user.password)

    def test_create_user(self):
        username = self.user_hemmo.username
        password = self.user_hemmo.password

        self.service.create_user(username, password)

        user = self.service.get_current_user()
        self.assertEqual(user.username, username)

    def test_create_user_with_existing_username(self):
        username = self.user_hemmo.username

        self.service.create_user(username, 'first')
        self.assertRaises(
            UsernameExistsError,
            lambda: self.service.create_user(username, 'second')
        )

    def test_create_user_with_invalid_username(self):
        self.assertRaises(
            UsernameNotValidError,
            lambda: self.service.create_user('a', '12345')
        )

    def test_create_user_with_invalid_password(self):
        self.assertRaises(
            PasswordNotValidError,
            lambda: self.service.create_user('name', 'a')
        )

    def test_add_recipe(self):
        username = self.user_hemmo.username
        password = self.user_hemmo.password
        self.service.create_user(username, password)

        name = self.recipe_puuro.name
        ingredients = self.recipe_puuro.ingredients
        category = self.recipe_puuro.category
        recipe = self.service.add_recipe(name, ingredients, category)

        self.assertEqual(recipe.name, self.recipe_puuro.name)
