from entities.user import User
from database_connection import get_db_connection

def get_user_by_row(row):
    return User(row['username'], row['password']) if row else None

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

        cursor.execute('INSERT INTO Users (username, password) values (?, ?)', [user.username, user.password])

        self._connection.commit()

        return user

    def find_by_username(self, username):
        """Palauttaa käyttäjän käyttäjätunnuksen perusteella, jos käyttäjä on tallennettu tietokantaan.

        Args:
            username: Merkkijono, joka kuvaa haettavan käyttäjän käyttäjätunnusta

        Returns:
            User-olio, joka kuvaa käyttäjätunnuksen haltijaa.
            None, jos käyttäjätunnusta ei löydy tietokannasta.
        """

        cursor = self._connection.cursor()

        cursor.execute('SELECT * FROM Users WHERE username = ?', [username])

        row = cursor.fetchone()

        return get_user_by_row(row)

    def delete_all(self):
        """Luokan metodi, joka poistaa kaikki käyttäjät."""

        cursor = self._connection.cursor()

        cursor.execute('DELETE FROM Users')

        self._connection.commit()


user_repository = UserRepository(get_db_connection())

