## Ristinollapeli
Sovelluksen avulla käyttäjä voi pelata peliä ristinolla eri kokoisilla ruudukoilla: 3x3, 5x5, 7x7.

Huipputulokset tallennetaan tietokantaan pelaajanimien perusteella.

## Release

[viikko 5](https://github.com/elonheimo/ot-harjoitustyo/releases/tag/viikko5)

[viikko 6](https://github.com/elonheimo/ot-harjoitustyo/releases/tag/viikko6)

## Dokumentaatio

- [Käyttöohje](/dokumentaatio/kayttoohje.md)

- [Vaatimusmäärittely](/dokumentaatio/vaatimusmaarittely.md)

- [Työaikakirjanpito](/dokumentaatio/tuntikirjanpito.md)

- [Changelog](/dokumentaatio/changelog.md)

- [Arkkitehtuuri](/dokumentaatio/arkkitehtuuri.md)


## Asennusohjeet
1. Asenna riippuvuudet

```bash
poetry install
```

2. Käynnistä ohjelma:
```bash
poetry run invoke start
```


## Komentorivitoiminnot

### Ohjelman suoritus
```bash
poetry run invoke start
```

### Testaus
```bash
poetry run invoke test
```
### Testikattavuus
```bash
poetry run invoke coverage-report
```
raportin voi katsoa avaamalla selaimessa _htmlcov/index.html_ -tiedoston.

### Pylint
[.pylintrc](./.pylintrc) tarkistuskomento:

```bash
poetry run invoke lint
```

