# Vaatimusmäärittely

## Käyttötarkoitus

Sovelluksen avulla käyttäjä voi kirjata muistiin resepteihinsä tarvittavat raaka-aineet ja määrät.
Hän voi hakea tallentamiaan reseptejä nimen tai raaka-aineiden perusteella. Sovellusta voi myös käyttää apuna ruokalistan suunnittelussa.
Jokaisella käyttäjällä on sovellukseen oma käyttäjätunnus ja salasana.

## Perustoiminnallisuus

### Ennen kirjautumista (toteutettu)

- käyttäjä voi luoda uuden käyttäjätunnuksen ja asettaa sille salasanan
  - kaikkien käyttäjätunnusten tulee olla erilaisia keskenään, tunnus on 3-15 merkkiä pitkä
  - myös salasanan tulee olla 3-15 merkkiä pitkä
  - jos tunnus/salasana ei täytä vaatimuksia, sovellus pyytää niitä uudelleen

- käyttäjä voi kirjautua sisään olemassa olevalla tunnuksella ja salasanalla
  - jos käyttäjätunnus/salasana on virheellinen, sovellus pyytää niitä uudestaan

### Kirjautumisen jälkeen

- käyttäjä voi tallentaa sovelluksen tietokantaan reseptin nimen ja siihen tarvittavat raaka-aineet (tehty)

- käyttäjä voi hakea kaikkien tallentamiensa reseptien nimet (tehty)

- käyttäjä voi hakea tallentamiaan reseptejä nimen tai raaka-aineen perusteella (tehty)

- käyttäjä voi poistaa tallentamansa reseptin (tehty)

- käyttäjä voi kirjautua ulos järjestelmästä (tehty)

## Jatkokehitysideoita

- käyttäjä voi muokata tallentamaansa reseptiä (tehty)

- käyttäjä voi pyytää sovellusta luomaan haluamansa mittaisen ruokalistan, jolloin sovellus arpoo tallennettujen reseptien joukosta pyydetyn määrän reseptejä    (tehty)
  - jos ruokalistan pituus on suurempi kuin tallennettujen reseptien määrä, sama resepti voi tulla ruokalistalle useamman kerran

- käyttäjä voi pyytää sovellusta laskemaan useamman reseptin valmistamiseen vaadittavien raaka-aineiden yhteismäärät (tehty)

- käyttäjä voi vaihtaa luodulta ruokalistalta yhden tai useamman reseptin johonkin toiseen

- käyttäjä voi luokitella reseptejä eri kategorioihin (tehty)

- käyttäjä voi tarkentaa hakua ja ruokalistan luomista kategorioiden perusteella (tehty)

- käyttäjä voi tallentaa tiedon siitä, milloin on valmistanut tiettyä ruokaa viimeksi
  - sovellus pitää myös kirjaa siitä, miten monta kertaa käyttäjä on kaikkiaan valmistanut tiettyä ruokaa

- käyttäjä voi tarkastella tilastoja kokkaushistoriastaan

- käyttäjä voi poistaa tunnuksensa, jolloin myös hänen tallentamansa reseptit poistetaan sovelluksen tietokannasta
