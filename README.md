# Ohjelmistotekniikan harjoitustyö

## Keittiöapulainen (sovellus)
Sovelluksen avulla käyttäjä voi kirjata muistiin resepteihinsä tarvittavat raaka-aineet ja määrät.
Hän voi hakea tallentamiaan reseptejä nimen tai raaka-aineiden perusteella. Sovellusta voi myös käyttää apuna ruokalistan suunnittelussa.
Jokaisella käyttäjällä on sovellukseen oma käyttäjätunnus ja salasana.

### Dokumentaatio
* [Vaatimusmäärittely](https://github.com/SiniCode/ot-harjoitustyo/blob/main/dokumentaatio/vaatimurmaarittely.md)
* [Työaikakirjanpito](https://github.com/SiniCode/ot-harjoitustyo/blob/main/dokumentaatio/tyoaikaseuranta.md)

### Asennus

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```

2. Alusta tietokanta komennolla:

```bash
poetry run invoke build
```

3. Käynnistä sovellus komennolla:

```bash
poetry run invoke start
```

### Komentorivitoiminnot

#### Ohjelman suorittaminen

Ohjelman pystyy suorittamaan komennolla:

```bash
poetry run invoke start
```

#### Testaus

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

#### Testikattavuus

Testikattavuusraportin voi generoida komennolla:

```bash
poetry run invoke coverage-report
```

Raportti generoituu _htmlcov_-hakemistoon.
