class Recipe:
    """Luokka, joka kuvaa yksittäistä reseptiä.

    Attributes:
        name: merkkijono, joka nimeää reseptin
        ingredients: lista tupleja, jotka ilmoittavat
                     reseptiin tarvittavat ainekset ja niiden määrän
        category: merkkijono, joka luokittelee reseptin tiettyyn kategoriaan
    """

    def __init__(self, name, ingredients=[], category="not defined"):
        """Luokan konstruktori, joka luo uuden reseptin.

        Args:
            name: merkkijono, joka nimeää reseptin
            ingredients: lista tupleja, jotka ilmoittavat
                         reseptiin tarvittavat ainekset ja niiden määrän
            category: merkkijono, joka luokittelee reseptin tiettyyn kategoriaan
        """

        self.name = name
        self.ingredients = ingredients
        self.category = category
