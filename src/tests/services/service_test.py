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

        self.recipe_puuro = Recipe(
            'puuro', [('vesi', '1 l'), ('kaurahiutaleet', '4 dl'),
                      ('suola', '1 tl')]
        )

        self.recipe_keksit = Recipe('keksit', [], 'herkut')
        self.recipe_lihapullat = Recipe(
            'lihapullat', [('vesi', '1 dl'), ('jauheliha', '400g'),
                           ('muna', '1')]
        )

        self.user_hemmo = User('hemmo', 'hauhau')
        self.user_haiku = User('haiku', 'vuh123')

    def test_create_user(self):
        username = self.user_hemmo.username
        password = self.user_hemmo.password

        service.create_user(username, password)

        user = service.get_current_user()
        self.assertEqual(user.username, username)

    def test_create_user_with_existing_username(self):
        username = self.user_hemmo.username

        service.create_user(username, 'first')
        self.assertRaises(
            UsernameExistsError,
            lambda: service.create_user(username, 'second')
        )

    def test_create_user_with_invalid_username(self):
        self.assertRaises(
            UsernameNotValidError,
            lambda: service.create_user('a', '12345')
        )

    def test_create_user_with_invalid_password(self):
        self.assertRaises(
            PasswordNotValidError,
            lambda: service.create_user('name', 'a')
        )

    def test_login(self):
        service.create_user(self.user_hemmo.username, self.user_hemmo.password)
        service.logout()
        service.login(self.user_hemmo.username, self.user_hemmo.password)

        user = service.get_current_user()
        self.assertEqual(user.username, self.user_hemmo.username)

    def test_login_with_invalid_username(self):
        service.create_user('hemmo', 'hauhau')
        service.logout()

        self.assertRaises(
            InvalidCredentialsError,
            lambda: service.login('emmo', 'hauhau')
        )

    def test_login_with_invalid_password(self):
        service.create_user('hemmo', 'hauhau')
        service.logout()

        self.assertRaises(
            InvalidCredentialsError,
            lambda: service.login('hemmo', 'vuhvuh')
        )

    def test_logout(self):
        service.create_user('hemmo', 'hauhau')
        service.logout()

        self.assertEqual(service.get_current_user(), None)

    def test_get_current_user(self):
        service.create_user('hemmo', 'hauhau')
        user = service.get_current_user()
        self.assertEqual(user.username, 'hemmo')

    def test_add_recipe_returns_recipe(self):
        username = self.user_hemmo.username
        password = self.user_hemmo.password
        service.create_user(username, password)

        name = self.recipe_puuro.name
        ingredients = self.recipe_puuro.ingredients
        category = self.recipe_puuro.category
        recipe = service.add_recipe(name, ingredients, category)

        self.assertEqual(recipe.name, self.recipe_puuro.name)

    def test_find_recipes_returns_correct_list1(self):
        service.create_user('hemmo', 'hauhau')
        service.add_recipe('puuro', [], 'aamupalat')
        service.add_recipe('keksit', [], 'jälkiruuat')

        recipes = service.find_recipes()
        reference = [('keksit', 'jälkiruuat'), ('puuro', 'aamupalat')]
        self.assertEqual(recipes, reference)

    def test_find_recipes_returns_correct_list2(self):
        service.create_user('hemmo', 'hauhau')
        service.add_recipe('puuro', [], 'aamupalat')
        service.add_recipe('keksit', [], 'jälkiruuat')

        recipes = service.find_recipes('aamupalat')
        reference = [('puuro', 'aamupalat')]
        self.assertEqual(recipes, reference)

    def test_find_recipes_by_ingredient_returns_correct_list1(self):
        service.create_user('hemmo', 'hauhau')
        ingredients = self.recipe_puuro.ingredients
        service.add_recipe('puuro', ingredients, 'aamupalat')
        ingredients = self.recipe_lihapullat.ingredients
        service.add_recipe('lihapullat', ingredients, 'liharuuat')

        recipes = service.find_recipes_by_ingredient('kaurahiutaleet')
        reference = [('puuro', 'aamupalat')]
        self.assertEqual(recipes, reference)

    def test_find_recipes_by_ingredient_returns_correct_list2(self):
        service.create_user('hemmo', 'hauhau')
        ingredients = self.recipe_puuro.ingredients
        service.add_recipe('puuro', ingredients, 'aamupalat')
        ingredients = self.recipe_lihapullat.ingredients
        service.add_recipe('lihapullat', ingredients, 'liharuuat')

        recipes = service.find_recipes_by_ingredient('vesi')
        reference = [('lihapullat', 'liharuuat'), ('puuro', 'aamupalat')]
        self.assertEqual(recipes, reference)

        recipes = service.find_recipes_by_ingredient('vesi', 'aamupalat')
        reference = [('puuro', 'aamupalat')]
        self.assertEqual(recipes, reference)

    def test_find_ingredients(self):
        service.create_user('hemmo', 'hauhau')
        ingredients = self.recipe_puuro.ingredients
        service.add_recipe('puuro', ingredients, 'aamupalat')

        self.assertEqual(service.find_ingredients('puuro'), ingredients)

    def test_change_recipe_name(self):
        service.create_user('hemmo', 'hauhau')
        service.add_recipe('puuro', [], 'aamupalat')
        service.change_recipe_name('puuro', 'kaurapuuro')

        recipes = service.find_recipes()
        self.assertEqual(recipes[0][0], 'kaurapuuro')

    def test_change_recipe_category(self):
        service.create_user('hemmo', 'hauhau')
        service.add_recipe('puuro', [], 'aamupalat')
        service.change_recipe_category('puuro', 'terveelliset')

        recipes = service.find_recipes()
        self.assertEqual(recipes[0][1], 'terveelliset')

    def test_change_ingredient_amount(self):
        service.create_user('hemmo', 'hauhau')
        ingredients = self.recipe_puuro.ingredients
        service.add_recipe('puuro', ingredients, 'aamupalat')
        service.change_ingredient_amount('puuro', 'vesi', '8 dl')

        ingredients = service.find_ingredients('puuro')

        self.assertEqual(ingredients[0], ('vesi', '8 dl'))

    def test_insert_an_ingredient(self):
        service.create_user('hemmo', 'hauhau')
        ingredients = self.recipe_puuro.ingredients
        service.add_recipe('puuro', ingredients, 'aamupalat')
        service.insert_an_ingredient('puuro', 'sokeri', '1 tl')

        ingredients = service.find_ingredients('puuro')

        self.assertEqual(ingredients[-1], ('sokeri', '1 tl'))

    def test_delete_an_ingredient(self):
        service.create_user('hemmo', 'hauhau')
        ingredients = self.recipe_puuro.ingredients
        service.add_recipe('puuro', ingredients, 'aamupalat')
        service.delete_an_ingredient('puuro', 'suola')

        ingredients = service.find_ingredients('puuro')

        self.assertEqual(ingredients[-1][0], 'kaurahiutaleet')
