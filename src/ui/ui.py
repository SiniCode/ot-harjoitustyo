from services.service import service, UsernameExistsError, UsernameNotValidError, PasswordNotValidError, InvalidCredentialsError


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
        print("  5: Log out")
        print()

    def login(self):
        """Luokan metodi, joka kirjaa käyttäjän sisään."""

        while True:
            confirm = input("Do you want to log in? (y/n): ")
            if confirm == "n":
                self.main()

            elif confirm == "y":
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
                    continue

            else:
                continue

    def create_user(self):
        """Luokan metodi, jonka avulla luodaan uusi käyttäjä ja asetetaan sille salasana."""

        while True:
            confirm = input("Do you want to create a new user? (y/n) ")
            if confirm == "n":
                self.main()

            elif confirm == "y":
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
                    continue
                except UsernameNotValidError:
                    print()
                    print("Invalid username")
                    continue
                except PasswordNotValidError:
                    print()
                    print("Invalid password")
                    continue

            else:
                continue

    def add_recipe(self):
        """Luokan metodi, jonka avulla kirjautunut käyttäjä voi lisätä uuden reseptin tietokantaan."""

        name = input("Name the recipe: ")
        ingredients = []

        while True:
            print()
            confirm = input(
                "Would you like to add an ingredient to the recipe? (y/n) ")
            if confirm == "n":
                break

            elif confirm == "y":
                print()
                ingredient = input("Ingredient: ")
                amount = input("Amount: ")
                ingredients.append((ingredient, amount))

            else:
                continue

        service.add_recipe(name, ingredients)

        print()
        print(f"{name} added to your recipies!")

        self.logged_in_main()

    def find_all_recipes(self):
        """Luokan metodi, joka tulostaa käyttäjän tallentamien reseptien nimet aakkosjärjestyksessä."""

        recipes = service.find_recipes()

        print("Your recipes:")
        print()
        for r in recipes:
            print(r)

        self.logged_in_main()

    def find_recipes_by_ingredient(self):
        """Luokan metodi, joka tulostaa aakkosjärjestyksessä niiden käyttäjän tallentamien reseptien nimet, joissa annettu aines esiintyy."""

        ingredient = input("Ingredient: ")
        print()

        recipes = service.find_recipes_by_ingredient(ingredient)

        print(f"Your recipes including {ingredient}:")
        print()
        for r in recipes:
            print(r)

        self.logged_in_main()

    def find_ingredients(self):
        """Luokan metodi, joka tulostaa annetun reseptin ainekset ja niiden määrät tallennusjärjestyksessä."""

        name = input("Which recipe would you like to see? ")

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

            option = input("What would you like to do? ")

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
        """Luokan metodi, jonka avulla käyttäjä voi nimetä tallentamansa reseptin uudelleen.

        Args:
            recipe: merkkijono, joka kertoo, mitä reseptiä halutaan muuttaa
        """

        new_name = input("New name: ")

        service.change_recipe_name(recipe, new_name)

        print()
        print(f"Recipe renamed as {new_name}!")

        self.logged_in_main()

    def add_an_ingredient(self, recipe):
        """Luokan metodi, joka lisää reseptiin uuden ainesosan.

        Args:
            recipe: merkkijono, joka kertoo, mihin reseptiin ainesosa lisätään
        """

        ingredient = input("Which ingredient would you like to add? ")
        amount = input("Amount: ")

        service.insert_an_ingredient(recipe, ingredient, amount)

        print()
        print("New ingredient added!")

        self.logged_in_main()

    def remove_an_ingredient(self, recipe):
        """Luokan metodi, joka poistaa reseptistä tallennetun aineksen.

        Args:
            recipe: merkkijono, joka kertoo, mistä reseptistä aines poistetaan
        """

        ingredient = input("Which ingredient would you like to remove? ")

        service.delete_an_ingredient(recipe, ingredient)

        print()
        print(f"{ingredient} removed!")

        self.logged_in_main()

    def change_ingredient_amount(self, recipe):
        """Luokan metodi, jonka avulla käyttäjä voi muuttaa tietyn aineksen määrää tallennetussa reseptissä.

        Args:
            recipe: merkkijono, joka kertoo, mitä reseptiä halutaan muuttaa
        """

        ingredient = input("Name of the ingredient: ")
        amount = input("Updated amount: ")

        service.change_ingredient_amount(recipe, ingredient, amount)

        print()
        print("The recipe is updated!")

        self.logged_in_main()

    def update_recipe(self):
        """Luokan metodi, jonka avulla käyttäjä voi muuttaa tallentamiaan reseptejä."""

        recipe = input("Which recipe would you like to update? ")

        while True:
            print()
            print("Options: ")
            print("  1: Rename the recipe")
            print("  2: Add an ingredient")
            print("  3: Remove an ingredient")
            print("  4: Change the amount of an ingredient")
            print()

            option = input("What would you like to do? ")

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

            else:
                continue

    def delete_recipe(self):
        recipe = input("Which recipe would you like to delete? ")
        service.delete_recipe(recipe)
        print()
        print(f"Recipe {recipe} deleted!")

        self.logged_in_main()

    def logout(self):
        """Luokan metodi, jonka avulla käyttäjä voi kirjautua ulos."""

        while True:
            confirmation = input("Do you want to log out? (y/n) ")
            if confirmation == "n":
                self.logged_in_main()

            elif confirmation == "y":
                print()
                user = service.get_current_user()
                service.logout()
                print(f"Goodbye!")
                self.main()

            else:
                continue

    def main(self):
        self.options()

        option = input("Choose option: ")

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
            print("Have a delicious day!")
            exit()

        else:
            self.main()

    def logged_in_main(self):
        self.logged_in_options()

        option = input("Choose option: ")

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
            self.logout()

        else:
            self.logged_in_main()


if __name__ == '__main__':
    ui = UI()
