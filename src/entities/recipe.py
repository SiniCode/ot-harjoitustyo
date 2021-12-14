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

    def add_ingredient(self, ingredient, amount):
        """Luokan metodi, joka lisää reseptiin uuden aineksen.

        Args:
            ingredient: merkkijono, joka kertoo, mikä ainesosa reseptiin lisätään
            amount: merkkijono, joka ilmoittaa lisättävän aineksen määrän
        """

        self.ingredients.append((ingredient, amount))

    def remove_ingredient(self, ingredient):
        """Luokan metodi, joka poistaa reseptistä nimetyn aineksen.

        Args:
            ingredient: merkkijono, joka kertoo, mikä ainesosa reseptistä poistetaan
        """

        for ing in self.ingredients:
            if ing[0] == ingredient:
                self.ingredients.remove(ing)
                break

    def change_amount(self, ingredient, amount):
        """Luokan metodi, joka muuttaa jo tallennetun aineksen määrän.
        Jos ainesta ei löydy reseptistä, se lisätään.

        Args:
            ingredient: merkkijono, joka kertoo, minkä aineksen määrä halutaan muuttaa
            amount: merkkijono, joka ilmoittaa korjatun määrän
        """

        for ing in self.ingredients:
            if ing[0] == ingredient:
                ing[1] = amount
                break

            if ing == self.ingredients[-1]:
                self.add_ingredient(ingredient, amount)
