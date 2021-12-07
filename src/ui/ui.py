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
        print("  1: log in")
        print("  2: create new user")
        print("  3: exit")
        print()

    def logged_in_options(self):
        """Luokan metodi, joka tulostaa kirjautuneen käyttäjän vaihtoehdot."""

        print()
        print("Options")
        print("  1: add new recipe")
        print("  2: find all recipes")
        print("  3: find a recipe")
        print("  4: rename a recipe")
        print("  5: delete a recipe")
        print("  6: log out")
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

        self.logged_in_main()

    def find_all_recipes(self):
        """Luokan metodi, joka tulostaa käyttäjän tallentamien reseptien nimet aakkosjärjestyksessä."""

        recipes = service.find_recipes()

        print("Saved recipes:")
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

    def rename_recipe(self):
        """Luokan metodi, jonka avulla käyttäjä voi nimetä tallentamansa reseptin uudelleen."""

        recipe = input("Which recipe would you like to rename? ")
        print()
        new_name = input("New name: ")
        service.change_recipe_name(recipe, new_name)
        print()
        print(f"Recipe renamed as {new_name}!")

        self.logged_in_main()


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
            self.find_all_recipes()

        elif op == 3:
            self.find_ingredients()

        elif op == 4:
            self.rename_recipe()

        elif op == 5:
            self.delete_recipe()

        elif op == 6:
            self.logout()

        else:
            self.logged_in_main()


if __name__ == '__main__':
    ui = UI()
