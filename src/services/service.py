from entities.user import User

from repositories.user_repository import (
    user_repository as default_user_repository
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

    def __init__(self, user_repository=default_user_repository):
        """Luokan konstruktori.

        Args:
            user_repository: UserRepository-luokan olio, vapaaehtoinen
        """

        self._user = None
        self._user_repository = user_repository

    def create_user(self, username, password)
        """Luokan metodi, joka luo uuden käyttäjän ja kirjaa sen samalla sisään.

        Args:
            username: 3-15 merkkiä pitkä merkkijono, joka toimii käyttäjän käyttäjätunnuksena
            password: 3-15 merkkiä pitkä merkkijono, joka toimii käyttäjän salasanana

        Raises:
            UsernameExistsError: virhe, joka tapahtuu, jos käyttäjätunnus on varattu toiselle käyttäjälle
            UsernameNotValidError: virhe, joka tapahtuu, jos käyttäjätunnus ei täytä pituusvaatimusta
            PasswordNotValidError: virhe, joka tapahtuu, jos salasana ei täytä pituusvaatimusta

        Returns:
            User-olio, joka kuvaa luotua käyttäjää
        """

        existing_user = self._user_repository.find_by_username(username)
        if existing_user != None:
            raise UsernameExistsError(f'Username {username} is already in use')

        if len(username) < 3 or len(username) > 15:
           raise UsernameNotValidError("Username must be 3 to 15 characters long")

        if len(password) < 3 or len(password) > 15:
           raise PasswordNotValidError("Password must be 3 to 15 characters long")

        user = self._user_repository.create_user(User(username, password))
        self._user = user

        return user

    def login(self, username, password):
        """Luokan metodi, joka kirjaa käyttäjän sisään.

        Args:
            username: merkkijono, joka toimii kirjautuvan käyttäjän käyttäjätunnuksena
            password: merkkijono, joka toimii kirjautuvan käyttäjän salasanana

        Raises:
            InvalidCredentialsError: virhe, joka tapahtuu, jos käyttäjää ei löydy tai käyttäjätunnus ja salasana eivät vastaa toisiaan

        Returns:
            User-olio, joka kuvaa kirjautunutta käyttäjää
        """

        user = self._user_repository.find_by_username(username)

        if user == None or user.password != password:
             raise InvalidCredentialsError("Invalid username or password")

        self._user = user

        return user

    def logout(self):
        """Luokan metodi, joka kirjaa nykyisen käyttäjän ulos."""

        self._user = None

    def get_current_user(self):
        """Palauttaa kirjautuneen käyttäjän.

        Returns:
            User-olio, joka kuvaa kirjautunutta käyttäjää
        """

        return self._user


service = Service()
