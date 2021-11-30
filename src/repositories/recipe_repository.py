from entities.recipe import Recipe
from entities.user import User
from database_connection import get_db_connection

class RecipeRepository:
    """Luokka, joka vastaa resepteihin liittyvistä tietokantaoperaatioista."""

    def __init__(self, connection):
    """Luokan konstruktori.

    Args:
        connection: Connection-olio, joka kuvaa tietokantayhteyttä
    """

    self._connection = connection


    def add_recipe(self, recipe, user):
    """Tallentaa uuden reseptin tietokantaan.

    Args:
        recipe: Recipe-olio, joka kuvaa tallennetaavaa reseptiä
        user: User-olio, joka kuvaa kirjautuneena olevaa käyttäjää

    Returns:
        Recipe-olio, joka kuvaa tallennettua reseptiä
    """

    cursor = self._connection.cursor()

    user_id = cursor.execute(
        "SELECT id FROM Users WHERE username=?", [user.username]).fetchone()[0]

    cursor.execute(
        "INSERT INTO Recipes (name, user_id) VALUES (recipe.name, user_id)")

    recipe_id = cursor.execute(
        "SELECT id FROM Recipes WHERE name=?", [recipe.name]).fetchone()[0]

    for ing in recipe.ingredients:
        cursor.execute(
            "INSERT INTO Ingredients (name, amount, recipe_id) VALUES (ing[0], ing[1], recipe_id)")

    self._connection.commit()

    return recipe

    def find_recipes_by_user(self, user):
        """Luokan metodi, joka etsii kaikkien käyttäjän tallentamien reseptien nimet.

        Args:
            user: User-olio, joka kuvaa kirjautunutta käyttäjää

        Returns:
            lista käyttäjän tallentamien reseptien nimistä
        """

        cursor = self._connection.cursor()

        user_id = cursor.execute(
            "SELECT id FROM Users WHERE username=?", [user.username]).fetchone()[0]

        recipes = cursor.execute(
            "SELECT name FROM Recipes WHERE user_id=?", [user_id]).fetchall()

        return recipes

    def find_ingredients_by_recipe(self, recipe, user):
        """Luokan metodi, joka etsii annettuun reseptiin tarvittavat raaka-aineet ja niiden määrän.

        Args:
            recipe: merkkijono, joka kertoo haettavan reseptin nimen
            user: User-olio, joka kertoo, kenen tallentamia reseptejä tarkastellaan (eri käyttäjillä voi olla samannimisiä reseptejä)

        Returns:
            lista tupleja, jotka ilmoittavat reseptiin tarvittavat ainekset ja niiden määrän
        """

        cursor = self._connection.cursor()

        user_id = cursor.execute(
            "SELECT id FROM Users WHERE username=?", [user.username]).fetchone()[0]

        recipe_id = cursor.execute(
            "SELECT id FROM Recipes WHERE name=?", [recipe]).fetchone()[0]

        ingredients = cursor.execute(
            "SELECT I.name, I.amount FROM Ingredients I, Recipes R, Users U WHERE R_id = I.recipe_id AND R.user_id = U.id AND R.id=? AND U.id=?", (recipe_id, user_id)).fetchall()

        return ingredients

    def delete_all(self):
        """Luokan metodi, joka poistaa kaikki reseptit ja ainekset."""

        cursor = self._connection.cursor()

        cursor.execute("DELETE FROM Recipes")

        cursor.execute("DELETE FROM Ingredients")

        self._connection.commit()



recipe_repository = RecipeRepository(get_db_connection())
