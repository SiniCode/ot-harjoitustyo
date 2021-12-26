# Käyttöohje

## Ohjelman käynnistäminen

Riippuvuudet pitää asentaa ennen ohjelman ensimmäistä käynnistystä komennolla:

```bash
poetry install
```

Myös tietokanta pitää alustaa ennen ensimmäistä käynnistystä komennolla:

```bash
poetry run invoke build
```

Ohjelma käynnistetään komennolla:

```bash
poetry run invoke start
```

Käynnistyksen jälkeen sovellus ohjaa käyttäjän toimintaa joka vaiheessa,
jotta käyttö olisi mahdollisimman sujuvaa.

## Sovellukseen kirjautuminen/uuden käyttäjän luominen

Sovelluksen käynnistyksen jälkeen on mahdollista kirjautua sisään näppäinkomennolla **1** ja syöttämällä käyttäjänimi ja salasana.

Jos käyttäjätunnusta ei vielä ole, sen voi luoda näppäinkomennolla **2**, minkä jälkeen käyttäjän luominen etenee kuten sisään kirjautuminenkin.

Vaihtoehdot tulostuvat näytölle, kun sovelluksen avaa.

## Uuden reseptin lisääminen

Kirjautunut käyttäjä voi tallentaa uuden reseptin näppäinkomennolla **1**, minkä jälkeen
sovellus pyytää syöttämään reseptin nimen. Sen jälkeen reseptiin voi halutessaan lisätä raaka-aineita yksi kerrallaan.
Raaka-aine lisätään syöttämällä ensin aineksen nimi ja sitten sen määrä.
Jotta sovelluksen muut ominaisuudet toimisivat optimaalisesti, määrä kannattaa lisätä muodossa "x yksikkö", missä x on kokonais- tai desimaaliluku (desimaalierottimena piste), yksikkö on yleisesti käytössä oleva lyhenne (esim. dl tai g) ja luvun ja lyhenteen välissä on välilyönti.
Määrän voi määritellä muutenkin, mutta silloin sovelluksen laskutoimitukset eivät välttämättä toimi aivan oikein.
Lopuksi reseptin voi halutessaan asettaa tiettyyn kategoriaan syöttämällä kategorian nimen.

## Reseptien etsiminen

Kirjautunut käyttäjä voi etsiä reseptejä näppäinkomennolla **2**.
Komennon jälkeen aukeavat vaihtoehdot etsiä kaikki käyttäjän tallentamat reseptit komennolla **1** tai
kaikki sellaiset reseptit, joissa esiintyy tietty raaka-aine, näppäinkomennolla **2**.
Kumpikin haku on myös mahdollista kohdistaa vain tiettyyn kategoriaan
syöttämällä kategorian nimi, kun sitä pyydetään.
Kolmas hakuvaihtoehto on hakea tietyn reseptin raaka-aineet näppäinkomennolla **3**
ja syöttämällä halutun reseptin nimi.

## Reseptien muokkaaminen

Kirjautunut käyttäjä voi muokata tallentamiaan reseptejä näppäinkomennolla **3**.
Sovellus kysyy ensin, mitä reseptiä käyttäjä haluaa muokata, ja syötettyään reseptin nimen
käyttäjä voi

 - nimetä reseptin uudelleen komennolla **1** ja syöttämällä uuden nimen

 - lisätä reseptiin uuden ainesosan komennolla **2** ja syöttämällä raaka-aineen nimen ja määrän

 - poistaa reseptistä raaka-aineen komennolla **3** ja syöttämällä raaka-aineen nimen

 - muuttaa jonkin raaka-aineen määrää komennolla **4** ja syöttämällä raaka-aineen nimen ja uuden määrän

 - muuttaa reseptin kategorian komennolla **5** ja syöttämällä uuden kategorian

Kaikki vaihtoehdot tulostuvat näytölle.

## Reseptin poistaminen

Kirjautunut käyttäjä voi poistaa tallentamansa reseptin näppäinkomennolla **4** ja
syöttämällä reseptin nimen.

## Ruokalistan luominen

Kirjautunut käyttäjä voi arpoa reseptiensä joukosta haluamansa mittaisen ruokalistan
näppäinkomennolla **5** ja syöttämällä ruokalistan pituuden.
Halutessaan käyttäjä voi luoda ruokalistan vain tietyn kategorian resepteistä
syöttämällä kategorian nimen, kun sitä kysytään.

## Ainesten laskeminen

Kirjautunut käyttäjä voi pyytää sovellusta laskemaan yhteen haluamiensa reseptien ainekset
näppäinkomennolla **6** ja syöttämällä näiden reseptien nimet yksi kerrallaan.

## Ulos kirjautuminen/Sovelluksen sulkeminen

Kirjautunut käyttäjä voi kirjautua ulos näppäinkomennolla **7**.
Tämä ei kuitenkaan vielä sulje sovellusta, vaan sovellus palaa käynnistysnäkymään.
Käynnistysnäkymässä sovelluksen voi sulkea komennolla **3**.
