# Arkkitehtuurikuvaus

## Rakenne

## Käyttöliittymä
Käyttöliittymän näkymät

- Asetukset
- Pelinäkymä
- Huipputulokset

Jokaisella näkymällä on oma luokkansa. Vain yksi näkymä kerrallaan on esillä. Näkymien esittämisestä vastaa [UI](../src/ui/ui.py)-luokka

Aluksi käyttäjälle esitetään asetukset näkymä.

Mahdolliset siirtymät näkymien välillä:
- Asetukset  -> Pelinäkymä
- Pelinäkymä -> Huipputulokset
- Huipputulokset -> Pelinäkymä
- Huipputulokset -> Asetukset


## Sovelluslogiikka

Tietomallin muodostavat GameGrid ja Player
```mermaid
    classDiagram
        
        class GameGrid {
            int grid_size
            int win_length
            grid
            Player winner
            Player turn
            Player player1
            Player player2
        }

        class Player {
            str name
        }
        
        Player "2" -- "1" GameGrid
        
```

Sovelluksen toiminnallisuus on GameGrid luokan oliossa. 

![Pakkausrakenne ja luokat](./kuvat/pakkaus-luokat.png)

## Tietojen pysyväistallennus

Lisätään myöhemmin
