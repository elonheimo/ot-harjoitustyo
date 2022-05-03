## Käyttöohje
Lataa viimeisin [release](https://github.com/elonheimo/ot-harjoitustyo/releases). 
Assets -> source code -> lataa tiedosto -> pura pakattu tiedosto

## Konfigurointi 

```DATABASE_FILENAME=database.sqlite```

Voit vaihtaa tietokannan nimeä muokkaamalla juurihakemistossa olevaa .env tiedostoa

## Ohjelman käynnistäminen 

Asenna riippuvuudet

```poetry install```

Käynnistä ohjelma

```poetry run invoke start```

## Ohjelman käyttäminen

### Asetusnäkymä

Sovellus käynnistyy asetusnäkymään

Valitse pelaajien nimet, sekä mieluisa pelimuoto

![](../dokumentaatio/kuvat/user_manual1.png)

### Pelinäkymä

Pelaa peliä asettamalla merkkejä vuoron perään ruudukolle

![](../dokumentaatio/kuvat/user_manual2.png)

Toisen pelaajan voitettua tai pelin päättyessä tasapeliin klikkaa ylhäällä olevaa tekstiä.

![](../dokumentaatio/kuvat/user_manual3.png)


### Voittonäkymä

Tarkastele parhaimpia pelaajia 

Voit pelata uuden pelin tai palata asetuksiin valitsemaan vaikka eri pelimuodon.

![](../dokumentaatio/kuvat/user_manual4.png)
