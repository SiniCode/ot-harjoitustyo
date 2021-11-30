import unittest
from repositories.recipe_repository import recipe_repository
from repositories.user_repository import user_repository
from entities.recipe import Recipe
from entities.user import User

class TestRecipeRepository(unittest.TestCase):
    def setUp(self):
        recipe_repository.delete_all()
        user_repository.delete_all()

        self.user_hemmo = User('hemmo', 'hemmohau')
        self.user_haiku = User('haiku', 'haikuvuf')

        self.recipe_puuro = Recipe('puuro', [('hirssi', '5 dl'), ('tattari', '5 dl'), ('riisi', '5 dl'), ('porkkana', '1'), ('vesi', '3 l'), ('jauheliha', '500 g')])
        self.recipe_puuro2 = Recipe('puuro', [('vesi', '1 l'), ('kaurahiutaleet', '4 dl'), ('suola', '1 tl')])
        self.recipe_keksit = Recipe('keksit', [])

    def test_add_recipe_returns_recipe(self):
        user_repository.create_user(self.user_hemmo)
        self.assertEqual(recipe_repository.add_recipe(self.recipe_keksit, self.user_hemmo), self.recipe_keksit)

    def test_find_recipes_by_user_returns_correct_list(self):
        user_repository.create_user(self.user_hemmo)
        recipe_repository.add_recipe(self.recipe_puuro, self.user_hemmo)
        recipe_repository.add_recipe(self.recipe_keksit, self.user_hemmo)

        self.assertEqual(recipe_repository.find_recipes_by_user(self.user_hemmo), ['puuro', 'keksit'])

    def test_find_recipes_by_user_does_not_show_other_users_recipes(self):
        user_repository.create_user(self.user_hemmo)
        recipe_repository.add_recipe(self.recipe_puuro, self.user_hemmo)
        user_repository.create_user(self.user_haiku)
        recipe_repository.add_recipe(self.recipe_keksit, self.user_haiku)

        self.assertEqual(recipe_repository.find_recipes_by_user(self.user_haiku), [self.recipe_keksit.name])

    def test_find_ingredients_by_recipe_returns_correct_list(self):
        user_repository.create_user(self.user_hemmo)
        recipe_repository.add_recipe(self.recipe_puuro, self.user_hemmo)
        recipe_repository.add_recipe(self.recipe_keksit, self.user_hemmo)

        self.assertEqual(recipe_repository.find_ingredients_by_recipe('puuro', self.user_hemmo), self.recipe_puuro.ingredients)

    def test_find_ingredients_by_recipe_returns_correct_list2(self):
        user_repository.create_user(self.user_hemmo)
        recipe_repository.add_recipe(self.recipe_puuro, self.user_hemmo)
        user_repository.create_user(self.user_haiku)
        recipe_repository.add_recipe(self.recipe_puuro2, self.user_haiku)

        self.assertEqual(recipe_repository.find_ingredients_by_recipe('puuro', self.user_hemmo), self.recipe_puuro.ingredients)

