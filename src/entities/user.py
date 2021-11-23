class User:
    """Luokka, joka kuvaa sovelluksen yksittäistä käyttäjää.

    Attributes:
        username: 3-15 merkkiä pitkä merkkijono, joka toimii käyttäjätunnuksena
        password: 3-15 merkkiä pitkä merkkijono, joka toimii salasanana
    """

    def __init__(self, username, password):
        """Luokan konstruktori, joka luo uuden käyttäjän.

        Args:
            username: 3-15 merkkiä pitkä merkkijono, joka toimii käyttäjätunnuksena
            password: 3-15 merkkiä pitkä merkkijono, joka toimii salasanana
        """

        self.username = username
        self.password = password
