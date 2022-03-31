- Monopolia pelataan käyttäen kahta noppaa. 
- Pelaajia on vähintään 2 ja enintään 8. 
- Peliä pelataan pelilaudalla joita on yksi. 
- Pelilauta sisältää 40 ruutua. 
- Kukin ruutu tietää, mikä on sitä seuraava ruutu pelilaudalla. 
- Kullakin pelaajalla on yksi pelinappula. Pelinappula sijaitsee aina yhdessä ruudussa.

```mermaid
    classDiagram
        
        class Pelilauta {

        }

        Ruutu "40" -- "1" Pelilauta
        class Ruutu {
            Ruutu seuraava_ruutu
            list pelinappulat
        }
        
        Pelinappula "*" -- "1" Ruutu
        Pelinappula "1" -- "1" Pelaaja
        class Pelinappula {
            
        }

        Pelaaja "2..8" -- "1" Pelilauta
        class Pelaaja {

        }

        Noppa "2" -- "1" Pelilauta
        class Noppa{

        }
```