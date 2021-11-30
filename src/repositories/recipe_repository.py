from entities.recipe import Recipe
from entities.user import User
from database_connection import get_db_connection


def get_id_by_row(row):
    return row['id'] if row else None


def get_name_by_row(row):
    return row['name'] if row else None


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

        row = cursor.execute(
            "SELECT * FROM Users WHERE username=?", [user.username]).fetchone()
        user_id = get_id_by_row(row)

        cursor.execute(
            "INSERT INTO Recipes (name, user_id) VALUES (?, ?)", [recipe.name, user_id])

        row = cursor.execute(
            "SELECT * FROM Recipes WHERE name=?", [recipe.name]).fetchone()
        recipe_id = get_id_by_row(row)

        for (name, amount) in recipe.ingredients:
            cursor.execute(
                "INSERT INTO Ingredients (name, amount, recipe_id) VALUES (?, ?, ?)", [name, amount, recipe_id])

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

        row = cursor.execute(
            "SELECT * FROM Users WHERE username=?", [user.username]).fetchone()
        user_id = get_id_by_row(row)

        recipes = cursor.execute(
            "SELECT * FROM Recipes WHERE user_id=?", [user_id]).fetchall()

        result = []
        for row in recipes:
            result.append(get_name_by_row(row))

        return result

    def find_ingredients_by_recipe(self, recipe, user):
        """Luokan metodi, joka etsii annettuun reseptiin tarvittavat raaka-aineet ja niiden määrän.

        Args:
            recipe: merkkijono, joka kertoo haettavan reseptin nimen
            user: User-olio, joka kertoo, kenen tallentamia reseptejä tarkastellaan (eri käyttäjillä voi olla samannimisiä reseptejä)

        Returns:
            lista tupleja, jotka ilmoittavat reseptiin tarvittavat ainekset ja niiden määrän
        """

        cursor = self._connection.cursor()

        row = cursor.execute(
            "SELECT * FROM Users WHERE username=?", [user.username]).fetchone()
        user_id = get_id_by_row(row)

        row = cursor.execute(
            "SELECT * FROM Recipes WHERE name=?", [recipe]).fetchone()
        recipe_id = get_id_by_row(row)

        ingredients = cursor.execute(
            "SELECT I.name, I.amount FROM Ingredients I, Recipes R, Users U WHERE R.id = I.recipe_id AND R.user_id = U.id AND R.id=? AND U.id=?", (recipe_id, user_id)).fetchall()

        result = []
        for (name, amount) in ingredients:
            result.append((name, amount))

        return result

    def delete_all(self):
        """Luokan metodi, joka poistaa kaikki reseptit ja ainekset."""

        cursor = self._connection.cursor()

        cursor.execute("DELETE FROM Recipes")

        cursor.execute("DELETE FROM Ingredients")

        self._connection.commit()


recipe_repository = RecipeRepository(get_db_connection())
