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

        self.recipe_puuro = Recipe('puuro', [('hirssi', '5 dl'), ('tattari', '5 dl'), (
            'riisi', '5 dl'), ('porkkana', '1'), ('vesi', '3 l'), ('jauheliha', '500 g')])
        self.recipe_puuro2 = Recipe(
            'puuro', [('vesi', '1 l'), ('kaurahiutaleet', '4 dl'), ('suola', '1 tl')], 'aamupalat')
        self.recipe_keksit = Recipe('keksit', [], 'jälkiruuat')
        self.recipe_raksut = Recipe(
            'raksut', [('kaurahiutaleet', '1 dl'), ('lihaliemi', '2 dl'), ('muna', '1')])

    def test_add_recipe_returns_recipe(self):
        user_repository.create_user(self.user_hemmo)
        self.assertEqual(recipe_repository.add_recipe(
            self.recipe_keksit, self.user_hemmo), self.recipe_keksit)

    def test_find_recipes_by_user_returns_correct_list(self):
        user_repository.create_user(self.user_hemmo)
        recipe_repository.add_recipe(self.recipe_puuro, self.user_hemmo)
        recipe_repository.add_recipe(self.recipe_keksit, self.user_hemmo)

        self.assertEqual(recipe_repository.find_recipes_by_user(
            self.user_hemmo), [('puuro', 'not defined'), ('keksit', 'jälkiruuat')])

    def test_find_recipes_by_user_does_not_show_other_users_recipes(self):
        user_repository.create_user(self.user_hemmo)
        recipe_repository.add_recipe(self.recipe_puuro, self.user_hemmo)
        user_repository.create_user(self.user_haiku)
        recipe_repository.add_recipe(self.recipe_keksit, self.user_haiku)

        self.assertEqual(recipe_repository.find_recipes_by_user(
            self.user_haiku), [(self.recipe_keksit.name, self.recipe_keksit.category)])

    def test_find_ingredients_by_recipe_returns_correct_list(self):
        user_repository.create_user(self.user_hemmo)
        recipe_repository.add_recipe(self.recipe_puuro, self.user_hemmo)
        recipe_repository.add_recipe(self.recipe_keksit, self.user_hemmo)

        self.assertEqual(recipe_repository.find_ingredients_by_recipe(
            'puuro', self.user_hemmo), self.recipe_puuro.ingredients)

    def test_find_ingredients_by_recipe_returns_correct_list2(self):
        user_repository.create_user(self.user_hemmo)
        recipe_repository.add_recipe(self.recipe_puuro, self.user_hemmo)
        user_repository.create_user(self.user_haiku)
        recipe_repository.add_recipe(self.recipe_puuro2, self.user_haiku)

        self.assertEqual(recipe_repository.find_ingredients_by_recipe(
            'puuro', self.user_hemmo), self.recipe_puuro.ingredients)

    def test_delete_recipe(self):
        user_repository.create_user(self.user_hemmo)
        recipe_repository.add_recipe(self.recipe_puuro, self.user_hemmo)
        recipe_repository.add_recipe(self.recipe_keksit, self.user_hemmo)
        recipe_repository.delete_recipe('puuro', self.user_hemmo)

        self.assertEqual(recipe_repository.find_recipes_by_user(
            self.user_hemmo), [('keksit', 'jälkiruuat')])

    def test_delete_recipe_does_not_delete_recipes_from_other_users(self):
        user_repository.create_user(self.user_hemmo)
        recipe_repository.add_recipe(self.recipe_puuro, self.user_hemmo)
        recipe_repository.add_recipe(self.recipe_keksit, self.user_hemmo)
        user_repository.create_user(self.user_haiku)
        recipe_repository.add_recipe(self.recipe_puuro, self.user_haiku)
        recipe_repository.add_recipe(self.recipe_keksit, self.user_haiku)
        recipe_repository.delete_recipe('puuro', self.user_haiku)

        self.assertEqual(recipe_repository.find_recipes_by_user(
            self.user_hemmo)[0], ('puuro', 'not defined'))

    def test_find_recipe_by_ingredient_returns_correct_list(self):
        user_repository.create_user(self.user_hemmo)
        recipe_repository.add_recipe(self.recipe_puuro2, self.user_hemmo)
        recipe_repository.add_recipe(self.recipe_keksit, self.user_hemmo)
        recipe_repository.add_recipe(self.recipe_raksut, self.user_hemmo)

        self.assertEqual(recipe_repository.find_recipe_by_ingredient(
            'kaurahiutaleet', self.user_hemmo), [('puuro', 'aamupalat'), ('raksut', 'not defined')])

    def test_change_recipe_name(self):
        user_repository.create_user(self.user_hemmo)
        recipe_repository.add_recipe(self.recipe_puuro, self.user_hemmo)
        recipe_repository.add_recipe(self.recipe_keksit, self.user_hemmo)
        recipe_repository.change_recipe_name(
            'puuro', 'koiran puuro', self.user_hemmo)

        self.assertEqual(recipe_repository.find_recipes_by_user(
            self.user_hemmo)[0], ('koiran puuro', 'not defined'))

    def test_change_ingredient_amount(self):
        user_repository.create_user(self.user_hemmo)
        recipe_repository.add_recipe(self.recipe_puuro, self.user_hemmo)
        recipe_repository.change_ingredient_amount(
            'puuro', 'jauheliha', '800 g', self.user_hemmo)

        ingredients = recipe_repository.find_ingredients_by_recipe(
            'puuro', self.user_hemmo)
        self.assertEqual(ingredients[-1], ('jauheliha', '800 g'))

    def test_insert_an_ingredient(self):
        user_repository.create_user(self.user_hemmo)
        recipe_repository.add_recipe(self.recipe_puuro, self.user_hemmo)
        recipe_repository.insert_an_ingredient(
            'puuro', 'öljy', '1 rkl', self.user_hemmo)

        ingredients = recipe_repository.find_ingredients_by_recipe(
            'puuro', self.user_hemmo)
        self.assertEqual(ingredients[-1], ('öljy', '1 rkl'))

    def test_delete_an_ingredient(self):
        user_repository.create_user(self.user_hemmo)
        recipe_repository.add_recipe(self.recipe_puuro, self.user_hemmo)
        recipe_repository.delete_an_ingredient(
            'puuro', 'jauheliha', self.user_hemmo)

        ingredients = recipe_repository.find_ingredients_by_recipe(
            'puuro', self.user_hemmo)
        self.assertEqual(ingredients[-1], ('vesi', '3 l'))
