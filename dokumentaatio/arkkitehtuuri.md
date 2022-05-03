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

Repositories pakkauksen luokka ```HighscoreReposity``` vastaa tiedon pysyväistallennuksesta. 

### Tiedostot

Sovellus tallentaa tiedot  SQLite tietokantaan. Tietotokantatiedoston nimi on määritelty [.env](../.env) konfiguraatiotiedostossa. Tapahtumat (voitot ja häviöt) tallennetaan SQLite-tietokannan tauluun ```events```

## Päätoiminnallisuudet
```mermaid
sequenceDiagram
    actor user
    UI ->> UI: show_settings_view()
    user ->> UI: click "Play" button
    UI ->> GameGrid: Gamegrid(3, player1, player2)
    GameGrid ->> UI: gamegrid
    UI ->> UI: show_grid_view()
    UI ->> GameGrid: gamgrid.place_to_grid(0,0,"player")
    GameGrid ->> HighscoreReposiry: add_event("player", "WIN", "3x3")
    UI ->> UI: show_highscores_view()
    UI ->> GameGrid: get_highscores()
    GameGrid ->> HighscoreRepository: get_highscores()
    HighscoreRepository ->> GameGrid: 
    GameGrid ->> UI: 
```