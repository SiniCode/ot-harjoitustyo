from entities.user import User
from database_connection import get_db_connection

class UserRepository:
    """Luokka, joka vastaa käyttäjiin liittyvistä tietokantaoperaatioista."""

    def __init__(self, connection):
        """Luokan konstruktori.

        Args:
            connection: Connection-olio, jokakuvaa tietokantayhteyttä
        """

        self._connection = connection

    def create_user(self, user):
        """Luokan metodi, joka tallentaa uuden käyttäjän tietokantaan.

        Args:
            user: User-olio, joka kuvaa tallennettavaa käyttäjää

        Returns:
            User-olio, joka kuvaa tallennettua käyttäjää
        """

        cursor = self._connection.cursor()

        cursor.execute('INSERT INTO Users (username, password) values (?, ?)', (user.username, user.password))

        self._connection.commit()

        return user


user_repository = UserRepository(get_db_connection())

