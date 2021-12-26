from entities.user import User
from entities.recipe import Recipe

from repositories.user_repository import (
    user_repository as default_user_repo
)

from repositories.recipe_repository import (
    recipe_repository as default_recipe_repo
)


class UsernameExistsError(Exception):
    pass

class UsernameNotValidError(Exception):
    pass

class PasswordNotValidError(Exception):
    pass

class InvalidCredentialsError(Exception):
    pass


class Service:
    """Luokka, joka vastaa sovelluslogiikasta."""

    def __init__(self, user_repository=default_user_repo, recipe_repository=default_recipe_repo):
        """Luokan konstruktori.

        Args:
            user_repository: UserRepository-luokan olio, vapaaehtoinen
            recipe_repository: RecipeRepository-luokan olio, vapaaehtoinen
        """

        self._user = None
        self._user_repository = user_repository
        self._recipe_repository = recipe_repository

    def create_user(self, username, password):
        """Luokan metodi, joka luo uuden käyttäjän ja kirjaa sen samalla sisään.

        Args:
            username: 3-15 merkkiä pitkä merkkijono, joka toimii
                      käyttäjän käyttäjätunnuksena
            password: 3-15 merkkiä pitkä merkkijono, joka toimii
                      käyttäjän salasanana

        Raises:
            UsernameExistsError: virhe, joka tapahtuu, jos käyttäjätunnus
                                 on varattu
            UsernameNotValidError: virhe, joka tapahtuu, jos käyttäjätunnus
                                   rikkoo pituusvaatimusta
            PasswordNotValidError: virhe, joka tapahtuu, jos salasana
                                   rikkoo pituusvaatimusta

        Returns:
            User-olio, joka kuvaa luotua käyttäjää
        """

        existing_user = self._user_repository.find_by_username(username)

        if existing_user is not None:
            raise UsernameExistsError(f'Username {username} is already in use')

        if len(username) < 3 or len(username) > 15:
            raise UsernameNotValidError(
                "Username must be 3 to 15 characters long")

        if len(password) < 3 or len(password) > 15:
            raise PasswordNotValidError(
                "Password must be 3 to 15 characters long")

        user = self._user_repository.create_user(User(username, password))

        self._user = user

        return user

    def login(self, username, password):
        """Luokan metodi, joka kirjaa käyttäjän sisään.

        Args:
            username: merkkijono, joka toimii kirjautuvan käyttäjän
                      käyttäjätunnuksena
            password: merkkijono, joka toimii kirjautuvan käyttäjän salasanana

        Raises:
            InvalidCredentialsError: virhe, joka tapahtuu, jos käyttäjää ei
                                     löydy tai käyttäjätunnus ja salasana
                                     eivät vastaa toisiaan

        Returns:
            User-olio, joka kuvaa kirjautunutta käyttäjää
        """

        user = self._user_repository.find_by_username(username)

        if user is None or user.password != password:
            raise InvalidCredentialsError("Invalid username or password")

        self._user = user

        return user

    def logout(self):
        """Luokan metodi, joka kirjaa nykyisen käyttäjän ulos."""

        self._user = None

    def get_current_user(self):
        """Luokan metodi, joka palauttaa kirjautuneen käyttäjän.

        Returns:
            User-olio, joka kuvaa kirjautunutta käyttäjää
        """

        return self._user

    def add_recipe(self, name, ingredients=[], category="not defined"):
        """Luokan metodi, joka lisää reseptin tietokantaan.

        Args:
            name: merkkijono, joka nimeää reseptin
            ingredients: lista tupleja, jotka ilmoittavat reseptiin
                         tarvittavat ainekset ja niiden määrän, vapaaehtoinen
            category: merkkijono, joka luokittelee reseptin tiettyyn
                      kategoriaan, vapaaehtoinen

        Returns:
            Recipe-olio, joka kuvaa tallennetun reseptin
        """

        user = self.get_current_user()
        recipe = Recipe(name, ingredients, category)

        self._recipe_repository.add_recipe(recipe, user)
        return recipe

    def delete_recipe(self, recipe_name):
        """Luokan metodi, joka poistaa reseptin tietokannasta.

        Args:
            recipe_name: merkkijono, joka kertoo, mikä resepti poistetaan
        """

        user = self.get_current_user()
        self._recipe_repository.delete_recipe(recipe_name, user)

    def find_recipes(self, category=None):
        """Luokan metodi, joka hakee kirjautuneen käyttäjän reseptit
           tietokannasta.

        Args:
            merkkijono, joka rajaa haun tiettyyn kategoriaan, vapaaehtoinen

        Returns:
            lista tupleja, jotka kertovat kirjautuneen käyttäjän tallentamien
            reseptien nimet ja kategoriat järjestettynä aakkosjärjestykseen
            reseptin nimen mukaan
        """

        user = self.get_current_user()

        recipes = self._recipe_repository.find_recipes_by_user(user, category)

        result = []
        for recipe in recipes:
            result.append(recipe)

        result.sort()
        return result

    def find_recipes_by_ingredient(self, ingredient, category=None):
        """Luokan metodi, joka hakee kirjautuneen käyttäjän resepteistä ne,
           joissa annettu ainesosa esiintyy.

        Args:
            ingredient: merkkijono, joka kertoo, minkä ainesosan
                        perusteella haku tehdään
            category: merkkijono, joka rajaa haun tiettyyn kategoriaan,
                      vapaaehtoinen

        Returns:
            lista tupleja, jotka kertovat hakua vastaavien reseptien nimet ja
            kategoriat aakkosjärjestyksessä nimen mukaan
        """

        user = self.get_current_user()

        recipes = self._recipe_repository.find_recipe_by_ingredient(
            ingredient, user, category)

        result = []
        for recipe in recipes:
            result.append(recipe)

        result.sort()
        return result

    def find_ingredients(self, recipe):
        """Luokan metodi, joka hakee pyydettyyn reseptiin tarvittavat
           raaka-aineet.

        Args:
            recipe: merkkijono, joka kertoo haettavan reseptin nimen

        Returns:
            lista reseptiin tarvittavista raaka-aineista ja niiden määristä
            tallennusjärjestyksessä
        """

        user = self.get_current_user()

        ingredients = self._recipe_repository.find_ingredients_by_recipe(
            recipe, user)

        return ingredients

    def change_recipe_name(self, old_name, new_name):
        """Luokan metodi, jonka avulla voi muuttaa reseptin nimeä.

        Args:
            old_name: merkkijono, joka ilmoittaa, minkä reseptin nimi
                      vaihdetaan
            new_name: merkkijono, joka ilmoittaa uuden nimen
        """

        user = self.get_current_user()
        self._recipe_repository.change_recipe_name(old_name, new_name, user)

    def change_recipe_category(self, recipe, new_category):
        """Luokan metodi, joka muuttaa reseptin kategorian.

        Args:
            recipe: merkkijono, joka kertoo, muokattavan reseptin nimen
            new_category: merkkijono, joka kertoo, mihin kategoriaan
                          resepti luokitellaan
        """

        user = self.get_current_user()
        self._recipe_repository.change_recipe_category(
            recipe, new_category, user)

    def change_ingredient_amount(self, recipe, ingredient, new_amount):
        """Luokan metodi, joka muuttaa reseptiin tarvittavan ainesosan määrän.

        Args:
            recipe: merkkijono, joka kertoo, mitä reseptiä halutaan muuttaa
            ingredient: merkkijono, joka kertoo, minkä aineksen määrä
                        halutaan muuttaa
            new_amount: merkkijono, joka ilmoittaa uuden määrän
        """

        user = self.get_current_user()
        self._recipe_repository.change_ingredient_amount(
            recipe, ingredient, new_amount, user)

    def insert_an_ingredient(self, recipe, ingredient, amount):
        """Luokan metodi, joka lisää reseptiin uuden aineksen.

        Args:
            recipe: merkkijono, joka kertoo, mitä reseptiä halutaan muuttaa
            ingredient: merkkijono, joka kertoo, mikä aines lisätään
            amount: merkkijono, joka ilmoittaa aineksen määrän
        """

        user = self.get_current_user()
        self._recipe_repository.insert_an_ingredient(
            recipe, ingredient, amount, user)

    def delete_an_ingredient(self, recipe, ingredient):
        """Luokan metodi, joka poistaa reseptistä annetun aineksen.

        Args:
            recipe: merkkijono, joka ilmoittaa, mitä reseptiä halutaan muuttaa
            ingredient: merkkijono, joka kertoo, mikä aines halutaan poistaa
        """

        user = self.get_current_user()
        self._recipe_repository.delete_an_ingredient(recipe, ingredient, user)

    def delete_everything(self):
        """Luokan metodi, joka tyhjentää koko tietokannan."""

        self._user_repository.delete_all()
        self._recipe_repository.delete_all()



service = Service()
