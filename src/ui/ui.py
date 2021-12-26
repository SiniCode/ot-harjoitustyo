from services.service import service, UsernameExistsError, UsernameNotValidError, PasswordNotValidError, InvalidCredentialsError
import random


class UI:
    """Luokka, joka tarjoaa käyttöliittymän sovellukseen."""

    def __init__(self):
        """Luokan konstruktori."""
        self.main()

    def options(self):
        """Luokan metodi, joka tulostaa aluksi käyttäjän vaihtoehdot."""

        print()
        print("Options")
        print("  1: Log in")
        print("  2: Create new user")
        print("  3: Exit")
        print()

    def logged_in_options(self):
        """Luokan metodi, joka tulostaa kirjautuneen käyttäjän vaihtoehdot."""

        print()
        print("Options")
        print("  1: Add new recipe")
        print("  2: Look for recipes")
        print("  3: Update recipe")
        print("  4: Delete recipe")
        print("  5: Create a menu")
        print("  6: Calculate ingredients")
        print("  7: Log out")
        print()

    def login(self):
        """Luokan metodi, joka kirjaa käyttäjän sisään."""

        print()
        username = input("Username: ")
        password = input("Password: ")

        try:
            service.login(username, password)
            print()
            print(f'Welcome, {username}!')
            self.logged_in_main()

        except InvalidCredentialsError:
            print()
            print("Invalid username or password")
            self.main()

    def create_user(self):
        """Luokan metodi, jonka avulla luodaan uusi käyttäjä ja asetetaan
           sille salasana. Samalla uusi käyttäjä kirjataan sisään."""

        print()
        username = input("Username (3-15 characters): ")
        password = input("Password (3-15 characters): ")

        try:
            service.create_user(username, password)
            print()
            print(f'Welcome, {username}!')
            self.logged_in_main()

        except UsernameExistsError:
            print()
            print(f'Username {username} is already in use')
            self.main()

        except UsernameNotValidError:
            print()
            print("Invalid username")
            self.main()

        except PasswordNotValidError:
            print()
            print("Invalid password")
            self.main()

    def add_recipe(self):
        """Luokan metodi, jonka avulla kirjautunut käyttäjä voi lisätä
           uuden reseptin tietokantaan."""

        name = input("Name the recipe: ").strip()
        ingredients = []

        while True:
            print()
            confirm = input(
                "Would you like to add an ingredient to the recipe? (y/n) ").strip()
            if confirm == "n" or confirm == "N":
                break

            elif confirm == "y" or confirm == "Y":
                print()
                ingredient = input("Ingredient: ").strip()
                amount = input("Amount: ").strip()
                ingredients.append((ingredient, amount))

            else:
                continue

        category = "not defined"
        while True:
            print()
            categorize = input(
                "Would you like to categorize this recipe? (y/n) ").strip()

            if categorize == "y" or categorizw == "Y":
                print()
                category = input("Name the category: ").strip()
                break

            elif categorize == "n" or categorize == "N":
                break

        service.add_recipe(name, ingredients, category)

        print()
        print(f"{name} added to your recipies!")

        self.logged_in_main()

    def _narrow_search_to_category(self):
        """Luokan metodi, joka kysyy käyttäjältä, haluaako hän rajata
           tekemänsä haun tiettyyn kategoriaan.

        Returns:
            merkkijono, joka ilmoittaa kategorian, johon haku rajataan
            None, jos käyttäjä ei halua rajata hakua
        """

        category = None

        while True:
            narrow_search = input(
                "Would you like to search within a certain category (y/n)? ").strip()

            if narrow_search == "y" or narrow_search == "Y":
                print()
                category = input("Name the category: ").strip()
                print()
                break

            elif narrow_search == "n" or narrow_search == "N":
                break

        return category

    def find_all_recipes(self):
        """Luokan metodi, joka tulostaa käyttäjän tallentamien reseptien
           nimet ja kategoriat aakkosjärjestyksessä nimen mukaan."""

        category = self._narrow_search_to_category()

        recipes = service.find_recipes(category)

        print("Your recipes:")
        print()
        for (name, category) in recipes:
            print(f"{name:40} ({category})")

        self.logged_in_main()

    def find_recipes_by_ingredient(self):
        """Luokan metodi, joka tulostaa aakkosjärjestyksessä niiden
           käyttäjän tallentamien reseptien nimet ja kategoriat,
           joissa annettu aines esiintyy."""

        ingredient = input("Ingredient: ").strip()
        print()

        category = self._narrow_search_to_category()

        recipes = service.find_recipes_by_ingredient(ingredient, category)

        print(f"Your recipes including {ingredient}:")
        print()
        for (name, category) in recipes:
            print(f"{name:40} ({category})")

        self.logged_in_main()

    def find_ingredients(self):
        """Luokan metodi, joka tulostaa annetun reseptin ainekset
           ja niiden määrät tallennusjärjestyksessä."""

        name = input("Which recipe would you like to see? ").strip()

        self._check_user_recipes(name)

        ingredients = service.find_ingredients(name)

        print()
        print(f"The ingredients of {name}:")
        print()

        for i in ingredients:
            print(f"{i[0]:40} {i[1]}")

        self.logged_in_main()

    def look_for_recipes(self):
        """Luokan metodi, jonka avulla käyttäjä voi tehdä hakuja tietokannasta"""

        while True:
            print()
            print("Options:")
            print("  1: Find all recipes")
            print("  2: Search recipes by ingredient")
            print("  3: Find the ingredients of a recipe")
            print()

            option = input("What would you like to do? ").strip()

            try:
                op = int(option)
            except ValueError:
                continue

            print()

            if op == 1:
                self.find_all_recipes()

            elif op == 2:
                self.find_recipes_by_ingredient()

            elif op == 3:
                self.find_ingredients()

            else:
                continue

    def rename_recipe(self, recipe):
        """Luokan metodi, jonka avulla käyttäjä voi nimetä tallentamansa
           reseptin uudelleen.

        Args:
            recipe: merkkijono, joka kertoo, mitä reseptiä halutaan muuttaa
        """

        new_name = input("New name: ").strip()

        service.change_recipe_name(recipe, new_name)

        print()
        print(f"Recipe renamed as {new_name}!")

        self.logged_in_main()

    def add_an_ingredient(self, recipe):
        """Luokan metodi, joka lisää reseptiin uuden ainesosan.

        Args:
            recipe: merkkijono, joka kertoo, mihin reseptiin ainesosa lisätään
        """

        ingredient = input("Which ingredient would you like to add? ").strip()
        amount = input("Amount: ").strip()

        service.insert_an_ingredient(recipe, ingredient, amount)

        print()
        print("New ingredient added!")

        self.logged_in_main()

    def _check_ingredients(self, recipe, ingredient):
        """Luokan metodi, joka tarkastaa, löytyykö annettu aines reseptistä.

        Args:
            recipe: merkkijono, joka kertoo tarkasteltavan reseptin nimen
            ingredient: merkkijono, joka kertoo, mitä ainesta etsitään
        """

        recipe_ingredients = service.find_ingredients(recipe)

        for (name,amount) in recipe_ingredients:
            if name == ingredient:
                return
            if (name,amount) == recipe_ingredients[-1]:
               print(f"Recipe {recipe} doesn't contain {ingredient}")
               self.logged_in_main()

    def remove_an_ingredient(self, recipe):
        """Luokan metodi, joka poistaa reseptistä tallennetun aineksen.

        Args:
            recipe: merkkijono, joka kertoo, mistä reseptistä aines poistetaan
        """

        ingredient = input(
            "Which ingredient would you like to remove? ").strip()

        self._check_ingredients(recipe, ingredient)

        service.delete_an_ingredient(recipe, ingredient)

        print()
        print(f"{ingredient} removed!")

        self.logged_in_main()

    def change_ingredient_amount(self, recipe):
        """Luokan metodi, jonka avulla käyttäjä voi muuttaa tietyn
           aineksen määrää tallennetussa reseptissä.

        Args:
            recipe: merkkijono, joka kertoo, mitä reseptiä halutaan muuttaa
        """

        ingredient = input("Name of the ingredient: ").strip()

        self._check_ingredients(recipe, ingredient)

        amount = input("Updated amount: ").strip()

        service.change_ingredient_amount(recipe, ingredient, amount)

        print()
        print("The recipe is updated!")

        self.logged_in_main()

    def change_recipe_category(self, recipe):
        """Luokan metodi, jonka avulla käyttäjä voi luokitella reseptin
           uudelleen.

        Args:
            recipe: merkkijono, joka kertoo muokattavan reseptin nimen
        """

        category = input("Give the name of the category: ").strip()

        service.change_recipe_category(recipe, category)

        print("The recipe is updated!")

        self.logged_in_main()

    def _check_user_recipes(self, recipe):
        """Luokan metodi, joka tarkastaa, löytyykö tietty resepti käyttäjän
           tallentamista resepteistä."""

        user_recipes = service.find_recipes()

        for (name, category) in user_recipes:
            if name == recipe:
                return
            if (name, category) == user_recipes[-1]:
                print()
                print("Recipe not found")
                self.logged_in_main()

    def update_recipe(self):
        """Luokan metodi, jonka avulla käyttäjä voi muuttaa tallentamiaan
           reseptejä."""

        recipe = input("Which recipe would you like to update? ").strip()

        self._check_user_recipes(recipe)

        while True:
            print()
            print("Options: ")
            print("  1: Rename the recipe")
            print("  2: Add an ingredient")
            print("  3: Remove an ingredient")
            print("  4: Change the amount of an ingredient")
            print("  5: Change the category of the recipe")
            print()

            option = input("What would you like to do? ").strip()

            try:
                op = int(option)
            except ValueError:
                continue

            print()

            if op == 1:
                self.rename_recipe(recipe)

            elif op == 2:
                self.add_an_ingredient(recipe)

            elif op == 3:
                self.remove_an_ingredient(recipe)

            elif op == 4:
                self.change_ingredient_amount(recipe)

            elif op == 5:
                self.change_recipe_category(recipe)

            else:
                continue

    def delete_recipe(self):
        """Luokan metodi, jonka avulla käyttäjä voi poistaa reseptin
           tietokannasta."""

        recipe = input("Which recipe would you like to delete? ").strip()

        self._check_user_recipes(recipe)

        service.delete_recipe(recipe)

        print()
        print(f"Recipe {recipe} deleted!")

        self.logged_in_main()

    def create_menu(self):
        """Luokan metodi, jonka avulla käyttäjä voi luoda valitsemansa
           mittaisen ruokalistan."""

        try:
            days = int(
                input("How many days would you like the menu to cover? "))
        except ValueError:
            print()
            print("Please, give a number")
            print()
            self.create_menu()

        category = self._narrow_search_to_category()

        menu = []
        recipes = service.find_recipes(category)

        if recipes == []:
            print("Please, add some recipes first.")
            self.logged_in_main()

        random.shuffle(recipes)

        while len(menu) < days:
            menu += recipes

        print()
        print(f"Menu suggestion for {days} days:")
        print()

        for d in range(days):
            print(menu[d][0])

        self.logged_in_main()

    def _add_recipe_to_calculation(self, ingredients, user_recipes):
        """Luokan metodi, jonka avulla raaka-aineiden laskentaan voidaan
           lisätä reseptejä.

        Args:
            ingredients: lista, jossa kunkin reseptin raaka-aineet ja niiden
                         määrät on esitetty listana tupleja
            user_recipes: lista käyttäjän tallentamista resepteistä
        """

        while True:
            print()
            add = input(
                "Would you like to add another recipe to calculation (y/n) ").strip()
            print()

            if add == "y" or add == "Y":
                recipe = input("Which recipe? ").strip()

                if recipe not in user_recipes:
                    print("Recipe not found")
                    continue

                ingredients.append(service.find_ingredients(recipe))

            elif add == "n" or add == "N":
                break

    def _add_ingredients_to_dictionary(self, ingredients):
        """Luokan metodi, joka luo laskennan aineksista sanakirjaolion.

        Args:
            ingredients: lista, jossa kunkin laskennassa huomioitavan
                         reseptin ainekset ja niiden määrät on ilmoitettu
                         listana tupleja

        Returns:
            sanakirjaolio, jossa ainesten nimet ovat avaimina ja arvona on
            lista, joka ilmoittaa, kuinka paljon kyseistä ainesta kussakin
            reseptissä tarvitaan
        """

        ingredient_dict = {}

        for recipe in ingredients:
            for (ingredient, amount) in recipe:
                if not ingredient in ingredient_dict:
                    ingredient_dict[ingredient] = [amount]
                else:
                    ingredient_dict[ingredient].append(amount)

        return ingredient_dict

    def calculate_ingredients(self):
        """Luokan metodi, jonka avulla käyttäjä voi laskea yhteen
           antamiinsa resepteihin tarvittavat raaka-aineet."""

        recipe_list = service.find_recipes()
        user_recipes = []

        for (name, category) in recipe_list:
            user_recipes.append(name)

        ingredients = []

        recipe = input(
            "Which recipe would you like to add to calculation? ").strip()

        if recipe not in user_recipes:
            print("Recipe not found")
            self.calculate_ingredients()

        ingredients.append(service.find_ingredients(recipe))

        self._add_recipe_to_calculation(ingredients, user_recipes)

        ingredient_dict = self._add_ingredients_to_dictionary(ingredients)

        result = []

        for ingredient, amounts in ingredient_dict.items():
            memory = []
            number = None
            litres = 0.0
            grams = 0.0
            tablespoons = 0.0
            teaspoons = 0.0
            a = 0.0

            for amount_str in amounts:
                amount = amount_str.split()
                try:
                    number = float(amount[0])
                except ValueError:
                    memory.append(amount_str)

                if number is not None and len(amount) > 1:
                    if amount[1][0] == "k":
                        number *= 1000
                    elif amount[1][0] == "d":
                        number /= 10
                    elif amount[1][0] == "c":
                        number /= 100
                    elif amount[1][0] == "m":
                        number /= 1000

                    if amount[1] in ["l", "dl", "cl", "ml"]:
                        litres += number
                    elif amount[1] in ["kg", "g"]:
                        grams += number
                    elif amount[1] in ["rkl", "tbsp"]:
                        tablespoons += number
                    elif amount[1] in ["tl", "tsp"]:
                        teaspoons += number
                    elif amount[1] in ["kpl", "pcs"]:
                        a += number
                    else:
                        memory.append(amount_str)

                elif number is not None:
                    a += number

            ingredient_str = f"{ingredient}: "

            if litres > 0:
                ingredient_str += f"{litres} litres "
            if grams > 0:
                ingredient_str += f"{grams} grams "
            if tablespoons > 0:
                ingredient_str += f"{tablespoons} tablespoons "
            if teaspoons > 0:
                ingredient_str += f"{teaspoons} teaspoons "
            if a > 0:
                ingredient_str += f"{a} pcs "
            for ing in memory:
                ingredient_str += f"{ing} "

            result.append(ingredient_str)

        for string in result:
            print(string)

        self.logged_in_main()

    def logout(self):
        """Luokan metodi, jonka avulla käyttäjä voi kirjautua ulos."""

        while True:
            confirmation = input("Do you want to log out? (y/n) ").strip()
            if confirmation == "n" or confirmation == "N":
                self.logged_in_main()

            elif confirmation == "y" or confirmation == "Y":
                print()
                service.logout()

                print(f"Have a delicious day!")

                self.main()

            else:
                continue

    def main(self):
        """Luokan metodi, joka näyttää kirjautumattoman
           käyttäjän vaihtoehdot."""

        self.options()

        option = input("Choose option: ").strip()

        try:
            op = int(option)
        except ValueError:
            self.main()

        print()

        if op == 1:
            self.login()

        elif op == 2:
            self.create_user()

        elif op == 3:
            exit()

        else:
            self.main()

    def logged_in_main(self):
        """Luokan metodi, joka näyttää kirjautuneen
           käyttäjän vaihtoehdot."""

        self.logged_in_options()

        option = input("Choose option: ").strip()

        try:
            op = int(option)
        except ValueError:
            self.logged_in_main()

        print()

        if op == 1:
            self.add_recipe()

        elif op == 2:
            self.look_for_recipes()

        elif op == 3:
            self.update_recipe()

        elif op == 4:
            self.delete_recipe()

        elif op == 5:
            self.create_menu()

        elif op == 6:
            self.calculate_ingredients()

        elif op == 7:
            self.logout()

        else:
            self.logged_in_main()


if __name__ == '__main__':
    ui = UI()
