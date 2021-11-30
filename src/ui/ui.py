from services.service import service, UsernameExistsError, UsernameNotValidError, PasswordNotValidError, InvalidCredentialsError


class UI:
    """Luokka, joka tarjoaa käyttöliittymän sovellukseen."""

    def __init__(self):
        """Luokan konstruktori."""
        self.main()

    def options(self):
        """Luokan metodi, joka tulostaa aluksi käyttäjän vaihtoehdot."""

        print("Options")
        print("1: kirjaudu sisään")
        print("2: luo uusi käyttäjä")

    def login(self):
        """Luokan metodi, joka kirjaa käyttäjän sisään.

        Returns:
            Palauttaa True, jos kirjautuminen onnistuu, ja False, jos käyttäjä keskeyttää kirjautumisen
        """

        while True:
            confirm = input("Do you want to log in? (y/n): ")
            if confirm == "n":
                return False
            username = input("Username: ")
            password = input("Password: ")

            try:
                service.login(username, password)
                print(f'Welcome, {username}!')
                return True
            except InvalidCredentialsError:
                print("Invalid username or password")
                continue

    def create_user(self):
        """Luokan metodi, jonka avulla luodaan uusi käyttäjä ja asetetaan sille salasana.

        Returns:
            Palauttaa True, jos käyttäjän luominen onnistuu, ja False, jos käyttäjä keskeyttää luomisen
        """

        while True:
            confirm = input("Do you want to create a new user? (y/n) ")
            if confirm == "n":
                return False
            username = input("Username (3-15 characters): ")
            password = input("Password (3-15 characters): ")

            try:
                service.create_user(username, password)
                print(f'Welcome, {username}!')
                return True
            except UsernameExistsError:
                print(f'Username {username} is already in use')
                continue
            except UsernameNotValidError:
                print("Invalid username")
                continue
            except PasswordNotValidError:
                print("Invalid password")
                continue
                continue

    def main(self):
        self.options()
        option = input("Choose option: ")
        if int(option) == 1:
            self.login()
        elif int(option) == 2:
            self.create_user()


if __name__ == '__main__':
    ui = UI()
