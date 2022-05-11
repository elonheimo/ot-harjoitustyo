# Vaatimusmäärittely

## Sovelluksen tarkoitus
Sovelluksen avulla kaksi pelaajaa voi pelata peliä ristinolla. Huipputulokset tallennetaan tietokantaan.

## Käyttäjät
Alussa pelaja pelaa syöttää haluamansa nimen. Käyttäjällä ei ole salasanaa. Nimi vaikuttaa ainoastaan huipputuloksiin

## Käyttöliittymäluonnos

Sovellus koostuu kolmesta eri näkymästä.

Sovellus aukeaa asetusnäkymään, jossa voidaan valita pelaajien nimet sekä pelimuoto (3x3, 5x5, 7x7)
Alla mahdolliset siirtymät näkymistä toisiin.

Asetukset  -> Pelinäkymä

Pelinäkymä -> Huipputulokset

Huipputulokset -> Pelinäkymä

Huipputulokset -> Asetukset

![Asetukset](/dokumentaatio/kuvat/user_manual1.png)
![Ruudukko](/dokumentaatio/kuvat/user_manual2.png)
![Huipputulokset](/dokumentaatio/kuvat/user_manual4.png)

## Perusversion tarjoama toiminnallisuus
- Asetukset
  - Pelaajat asettavat nimensä
  - Pelimuodon valinta 
    - 3x3, 5x5 tai 7x7 ruudukko
- Pelinäkymä 
  - Pelaajat asettavat vuoron perään merkkejä ruudukkoon
  - Voittoon vaadittavan yhtenäisen suoran pituus
    - 3x3: 3
    - 5x5: 4
    - 7x7: 5
- Huipputulokset
  - Näytöllä näkyy pelimuotokohtainen lista parhaista pelaajista
  - Käyttäjä voi palata asetuksiin vaihtakseen pelimuotoa tai nimiä
  - Käyttäjä voi pelata uudestaan
  
## Jatkokehitysideoita
- Pelaaja voisi pelata yksinpeliä algoritmia vastaan
- Kellotettu pelimuoto, jossa pelaajalla olisi rajoitettu aika asettaa merkki ruuudukkoon
