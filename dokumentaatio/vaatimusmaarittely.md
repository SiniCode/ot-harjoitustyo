# Vaatimusmäärittely

## Käyttötarkoitus

Sovelluksen avulla käyttäjä voi kirjata muistiin resepteihinsä tarvittavat raaka-aineet ja määrät.
Hän voi hakea tallentamiaan reseptejä nimen tai raaka-aineiden perusteella. Sovellusta voi myös käyttää apuna ruokalistan suunnittelussa.
Jokaisella käyttäjällä on sovellukseen oma käyttäjätunnus ja salasana.

## Perustoiminnallisuus

### Ennen kirjautumista

- käyttäjä voi luoda uuden käyttäjätunnuksen ja asettaa sille salasanan
  - kaikkien käyttäjätunnusten tulee olla erilaisia keskenään, tunnus on 3-15 merkkiä pitkä
  - myös salasanan tulee olla 3-15 merkkiä pitkä
  - jos tunnus/salasana ei täytä vaatimuksia, sovellus pyytää niitä uudelleen

- käyttäjä voi kirjautua sisään olemassa olevalla tunnuksella ja salasanalla
  - jos käyttäjätunnus/salasana on virheellinen, sovellus pyytää niitä uudestaan

### Kirjautumisen jälkeen

- käyttäjä voi tallentaa sovelluksen tietokantaan reseptin nimen ja siihen tarvittavat raaka-aineet

- käyttäjä voi hakea kaikkien tallentamiensa reseptien nimet

- käyttäjä voi hakea tallentamiaan reseptejä nimen tai raaka-aineen perusteella

- käyttäjä voi poistaa tallentamansa reseptin

- käyttäjä voi kirjautua ulos järjestelmästä

## Jatkokehitysideoita

- käyttäjä voi muuttaa tallentamansa reseptin nimen

- käyttäjä voi lisätä tallentamaansa reseptiin uuden raaka-aineen

- käyttäjä voi poistaa raaka-aineen tallentamastaan reseptistä

- käyttäjä voi muuttaa raaka-aineen määrää reseptissä

- käyttäjä voi pyytää sovellusta luomaan haluamansa mittaisen ruokalistan, jolloin sovellus arpoo tallennettujen reseptien joukosta pyydetyn määrän reseptejä
  - jos ruokalistan pituus on suurempi kuin tallennettujen reseptien määrä, sama resepti voi tulla ruokalistalle useamman kerran

- käyttäjä voi pyytää sovellusta laskemaan useamman reseptin valmistamiseen vaadittavien raaka-aineiden yhteismäärät

- käyttäjä voi luokitella reseptejä eri kategorioihin

- käyttäjä voi muuttaa reseptin kategorian niin halutessaan

- käyttäjä voi tarkentaa hakua ja ruokalistan luomista kategorioiden perusteella
