## Dokumentaatio

- [Vaatimusmäärittely](/dokumentaatio/vaatimusmaarittely.md)

- [Työaikakirjanpito](/dokumentaatio/tuntikirjanpito.md)

- [Changelog](/dokumentaatio/changelog.md)

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

###


