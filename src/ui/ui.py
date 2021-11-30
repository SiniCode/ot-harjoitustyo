from services.service import service, UsernameExistsError, UsernameNotValidError, PasswordNotValidError, InvalidCredentialsError


class UI:
    """Luokka, joka tarjoaa käyttöliittymän sovellukseen."""

    def __init__(self):
        """Luokan konstruktori."""
        self.main()

    def options(self):
        """Luokan metodi, joka tulostaa aluksi käyttäjän vaihtoehdot."""

        print("Options")
        print("1: log in")
        print("2: create new user")
        print("3: exit")

    def logged_in_options(self):
        """Luokan metodi, joka tulostaa kirjautuneen käyttäjän vaihtoehdot."""

        print("Options")
        print("1: add new recipe")
        print("2: find all recipes")
        print("3: find a recipe")
        print("4: log out")

    def login(self):
        """Luokan metodi, joka kirjaa käyttäjän sisään."""

        while True:
            confirm = input("Do you want to log in? (y/n): ")
            if confirm == "n":
                self.main()

            elif confirm == "y":
                username = input("Username: ")
                password = input("Password: ")

                try:
                    service.login(username, password)
                    print(f'Welcome, {username}!')
                    self.logged_in_main()

                except InvalidCredentialsError:
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
                username = input("Username (3-15 characters): ")
                password = input("Password (3-15 characters): ")

                try:
                    service.create_user(username, password)
                    print(f'Welcome, {username}!')
                    self.logged_in_main()

                except UsernameExistsError:
                    print(f'Username {username} is already in use')
                    continue
                except UsernameNotValidError:
                    print("Invalid username")
                    continue
                except PasswordNotValidError:
                    print("Invalid password")
                    continue

            else:
                continue

    def add_recipe(self):
        """Luokan metodi, jonka avulla kirjautunut käyttäjä voi lisätä uuden reseptin tietokantaan."""

        name = input("Name the recipe: ")
        ingredients = []

        while True:
            confirm = input("Would you like to add an ingredient to the recipe? (y/n) ")
            if confirm == "n":
                break

            elif confirm == "y":
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

        for r in recipes:
            print(r)

        self.logged_in_main()

    def find_ingredients(self):
        """Luokan metodi, joka tulostaa annetun reseptin ainekset ja niiden määrät tallennusjärjestyksessä."""

        name = input("Which recipe would you like to see? ")
        ingredients = service.find_ingredients(name)

        print(f"The ingredients of {name}:")

        for i in ingredients:
            print(f"{i[0]:50} {i[1]}")

        self.logged_in_main()

    def logout(self):
        """Luokan metodi, jonka avulla käyttäjä voi kirjautua ulos."""

        while True:
            confirmation = input("Do you want to log out? (y/n) ")
            if confirmation == "n":
                self.logged_in_main()

            elif confirmation == "y":
                service.logout()
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

        if op == 1:
            self.login()

        elif op == 2:
            self.create_user()

        elif op == 3:
            print("Bye bye!")
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


        if op == 1:
            self.add_recipe()

        elif op == 2:
            self.find_all_recipes()

        elif op == 3:
            self.find_ingredients()

        elif op == 4:
            self.logout()

        else:
            self.logged_in_main()

if __name__ == '__main__':
    ui = UI()
