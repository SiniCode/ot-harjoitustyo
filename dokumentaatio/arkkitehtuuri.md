# Arkkitehtuurikuvaus

## Rakenne

Ohjelma on rakennettu kolmitasoisen kerrosarkkitehtuurin periaatteita noudattaen.

### Pakkausrakenne

![](./kuvat/pakkausrakenne.png)

Pakkaus *ui* sisältää käyttöliittymästä, *services* sovelluslogiikasta ja *repositories* tietokantaoperaatiosta vastaavan koodin.
Pakkaus *entities* sisältää luokkia, jotka kuvastavat sovelluksen käyttämiä tietokohteita, *User* ja *Recipe*.

## Tärkeimmät toiminnallisuudet (täydentyy myöhemmin)

Sovelluksen tärkeimmät toiminnallisuudet kuvattuna sekvenssikaavioina.

### Käyttäjän kirjautuminen sisään

Kun käyttäjä avaa sovelluksen, näytöllä näkyvät vaihtoehdot, joista ensimmäinen on sisään kirjautuminen.
Käyttäjä kutsuu käyttöliittymän login-metodia antamalla näppäimistöltä komennon "1".
Sekvenssikaavio kuvaa, mitä sovelluksessa tapahtuu tämän jälkeen, jotta käyttäjä saadaan kirjattua sisään.

![](./kuvat/login.png)

Käyttöliittymästä vastaava UI lukee käyttäjän syötteistä käyttäjätunnuksen ja salasanan 
ja antaa ne sitten parametreina sovelluslogiikasta vastaavan Service-luokan *login*-metodille.
Tämä metodi kutsuu puolestaan tietokantaoperaatioista vastaavan UserRepositoryn *find_by_username*-metodia,
jonka palauttaman arvon avulla tarkastetaan, että käyttäjätunnus ja salasana ovat valideja.
Jos käyttäjätunnus on olemassa ja salasana täsmää siihen, kirjautuminen onnistuu ja käyttöliittymä 
näyttää kirjautuneen käyttäjän toimintovaihtoehdot.
