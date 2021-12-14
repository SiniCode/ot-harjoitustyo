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
            "INSERT INTO Recipes (name, category, user_id) VALUES (?, ?, ?)", 
             [recipe.name, recipe.category, user_id])

        cursor.execute(
            "SELECT * FROM Recipes WHERE name=? AND user_id=?", (recipe.name, user_id))
        row = cursor.fetchone()
        recipe_id = get_id_by_row(row)

        query = """INSERT INTO Ingredients (name, amount, recipe_id) VALUES (?, ?, ?)"""

        for (name, amount) in recipe.ingredients:
            values = [name, amount, recipe_id]
            cursor.execute(query, values)

        self._connection.commit()
        cursor.close()

        return recipe

    def delete_recipe(self, recipe, user):
        """Luokan metodi, joka poistaa reseptin tietokannasta.

        Args:
            recipe: merkkijono, joka kertoo poistettavan reseptin nimen
            user: User-olio, joka kertoo, kenen tallentama resepti poistetaan
        """

        cursor = self._connection.cursor()

        row = cursor.execute(
            "SELECT * FROM Users WHERE username=?", [user.username]).fetchone()
        user_id = get_id_by_row(row)

        cursor.execute(
            "SELECT * FROM Recipes WHERE name=? AND user_id=?", (recipe, user_id))
        row = cursor.fetchone()
        recipe_id = get_id_by_row(row)

        cursor.execute(
            "DELETE FROM Ingredients WHERE recipe_id=?", [recipe_id])
        cursor.execute("DELETE FROM Recipes WHERE id=?", [recipe_id])

        self._connection.commit()
        cursor.close()

    def find_recipes_by_user(self, user, category=None):
        """Luokan metodi, joka etsii kaikkien käyttäjän tallentamien reseptien nimet.

        Args:
            user: User-olio, joka kuvaa kirjautunutta käyttäjää
            category: merkkijono, joka kertoo, minkä kategorian reseptit 
                      halutaan mukaan, vapaaehtoinen

        Returns:
            lista käyttäjän tallentamien reseptien nimistä
        """

        cursor = self._connection.cursor()

        row = cursor.execute(
            "SELECT * FROM Users WHERE username=?", [user.username]).fetchone()
        user_id = get_id_by_row(row)

        if category is not None:
            recipes = cursor.execute(
                "SELECT * FROM Recipes WHERE user_id=? AND category=?,
                 [user_id, category]).fetchall()
        else:
            recipes = cursor.execute(
                "SELECT * FROM Recipes WHERE user_id=?", [user_id]).fetchall()

        cursor.close()

        result = []
        for row in recipes:
            result.append(get_name_by_row(row))

        return result

    def find_recipe_by_ingredient(self, ingredient, category=None, user):
        """Luokan metodi, joka etsii niiden käyttäjän tallentamien reseptien nimet,
           joissa haettu aines esiintyy.

        Args:
            ingredient: merkkijono, joka kertoo, minkä aineksen perusteella haku suoritetaan
            category: merkkijono, joka kertoo, minkä kategorian reseptejä haetaan, vapaaehtoinen
            user: User-olio, joka kuvaa käyttäjän, jonka tallentamia reseptejä haetaan

        Returns:
            lista hakua vastaavien reseptien nimistä
        """

        cursor = self._connection.cursor()

        row = cursor.execute(
            "SELECT * FROM Users WHERE username=?", [user.username]).fetchone()
        user_id = get_id_by_row(row)

        if category is not None:
            query = """SELECT * FROM Recipes R, Ingredients I
                         WHERE R.user_id=? AND R.id = I.recipe_id AND 
                         I.name=? AND R.category=?"""
            values = [user_id, ingredient, category]
        else:
            query = """SELECT * FROM Recipes R, Ingredients I
                     WHERE R.user_id=? AND R.id = I.recipe_id AND I.name=?"""
            values = [user_id, ingredient]

        recipes = cursor.execute(query, values).fetchall()

        cursor.close()

        result = []
        for row in recipes:
            result.append(get_name_by_row(row))

        return result

    def find_ingredients_by_recipe(self, recipe, user):
        """Luokan metodi, joka etsii annettuun reseptiin tarvittavat raaka-aineet ja niiden määrän.

        Args:
            recipe: merkkijono, joka kertoo haettavan reseptin nimen
            user: User-olio, joka kertoo, kenen tallentamia reseptejä tarkastellaan

        Returns:
            lista tupleja, jotka ilmoittavat reseptiin tarvittavat ainekset ja niiden määrän
        """

        cursor = self._connection.cursor()

        row = cursor.execute(
            "SELECT * FROM Users WHERE username=?", [user.username]).fetchone()
        user_id = get_id_by_row(row)

        row = cursor.execute(
            "SELECT * FROM Recipes WHERE name=? AND user_id=?", (recipe, user_id)).fetchone()
        recipe_id = get_id_by_row(row)

        query = """SELECT I.name, I.amount FROM Ingredients I, Recipes R
                     WHERE R.id = I.recipe_id AND R.id=?"""

        ingredients = cursor.execute(query, [recipe_id]).fetchall()

        cursor.close()

        result = []
        for (name, amount) in ingredients:
            result.append((name, amount))

        return result

    def change_recipe_name(self, old_name, new_name, user):
        """Luokan metodi, joka muuttaa reseptin nimen tietokannassa.

        Args:
            old_name: merkkijono, joka kertoo, minkä reseptin nimi halutaan muuttaa
            new_name: merkkijono, joka kertoo uuden nimen
            user = User-olio, joka kertoo, kenen tallentamasta reseptistä on kyse
        """

        cursor = self._connection.cursor()

        row = cursor.execute(
            "SELECT * FROM Users WHERE username=?", [user.username]).fetchone()
        user_id = get_id_by_row(row)

        row = cursor.execute(
            "SELECT * FROM Recipes WHERE name=? AND user_id=?", (old_name, user_id)).fetchone()
        recipe_id = get_id_by_row(row)

        query = """UPDATE Recipes SET name=? WHERE id=?"""
        values = (new_name, recipe_id)
        cursor.execute(query, values)

        self._connection.commit()
        cursor.close()

    def change_recipe_category(self, recipe, new_category, user):
        """Luokan metodi, joka muuttaa reseptin kategorian tietokannassa.

        Args:
            recipe: merkkijono, joka kertoo reseptin nimen
            new_category: merkkijono, joka kertoo kategorian, johon resepti siirretään
            user: User-olio, joka kertoo, kenen tallentamaa reseptiä käsitellään
        """

        cursor = self._connection.cursor()

        row = cursor.execute(
            "SELECT * FROM Users WHERE username=?", [user.username]).fetchone()
        user_id = get_id_by_row(row)

        query = """UPDATE Recipes SET category=? WHERE name=? AND user_id=?"""
        values = (new_category, recipe, user_id)
        cursor.execute(query, values)

        self._connection.commit()
        cursor.close()

    def change_ingredient_amount(self, recipe, ingredient, new_amount, user):
        """Luokan metodi, joka muuttaa reseptiin tarvittavan ainesosan määrän.

        Args:
            recipe: merkkijono, joka kertoo, mitä reseptiä halutaan muuttaa
            ingredient: merkkijono, joka kertoo, minkä aineksen määrä halutaan muuttaa
            new_amount: merkkijono, joka ilmoittaa uuden määrän
            user: User-olio, joka kertoo, kenen tallentamaa reseptiä muutetaan
        """

        cursor = self._connection.cursor()

        row = cursor.execute(
            "SELECT * FROM Users WHERE username=?", [user.username]).fetchone()
        user_id = get_id_by_row(row)

        row = cursor.execute(
            "SELECT * FROM Recipes WHERE name=? AND user_id=?", (recipe, user_id)).fetchone()
        recipe_id = get_id_by_row(row)

        query = """UPDATE Ingredients SET amount=? WHERE name=? AND recipe_id=?"""
        values = (new_amount, ingredient, recipe_id)
        cursor.execute(query, values)

        self._connection.commit()
        cursor.close()

    def insert_an_ingredient(self, recipe, ingredient, amount, user):
        """Luokan metodi, joka lisää reseptiin uuden aineksen.

        Args:
            recipe: merkkijono, joka kertoo, mitä reseptiä halutaan muuttaa
            ingredient: merkkijono, joka kertoo, mikä aines lisätään
            amount: merkkijono, joka ilmoittaa aineksen määrän
            user: User-olio, joka kertoo, kenen tallentamaa reseptiä muutetaan
        """

        cursor = self._connection.cursor()

        row = cursor.execute(
            "SELECT * FROM Users WHERE username=?", [user.username]).fetchone()
        user_id = get_id_by_row(row)

        row = cursor.execute(
            "SELECT * FROM Recipes WHERE name=? AND user_id=?", (recipe, user_id)).fetchone()
        recipe_id = get_id_by_row(row)

        query = """INSERT INTO Ingredients (name, amount, recipe_id) VALUES (?, ?, ?)"""
        values = [ingredient, amount, recipe_id]

        cursor.execute(query, values)

        self._connection.commit()
        cursor.close()

    def delete_an_ingredient(self, recipe, ingredient, user):
        """Luokan metodi, joka poistaa reseptistä annetun aineksen.

        Args:
            recipe: merkkijono, joka ilmoittaa, mitä reseptiä halutaan muuttaa
            ingredient: merkkijono, joka kertoo, mikä aines halutaan poistaa
            user: User-olio, joka kertoo, kenen tallentamaa reseptiä muokataan
        """

        cursor = self._connection.cursor()

        row = cursor.execute(
            "SELECT * FROM Users WHERE username=?", [user.username]).fetchone()
        user_id = get_id_by_row(row)

        row = cursor.execute(
            "SELECT * FROM Recipes WHERE name=? AND user_id=?", (recipe, user_id)).fetchone()
        recipe_id = get_id_by_row(row)

        query = """DELETE FROM Ingredients WHERE name=? AND recipe_id=?"""
        values = (ingredient, recipe_id)
        cursor.execute(query, values)

        self._connection.commit()
        cursor.close()

    def delete_all(self):
        """Luokan metodi, joka poistaa kaikki reseptit ja ainekset."""

        cursor = self._connection.cursor()

        cursor.execute("DELETE FROM Recipes")

        cursor.execute("DELETE FROM Ingredients")

        self._connection.commit()
        cursor.close()


recipe_repository = RecipeRepository(get_db_connection())
