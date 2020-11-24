# Sudoku sovellus

## Projektin tila

Tällä hetkellä projektiin on luotu vasta peruskäyttöliittymä ja ohjelmassa pääsee ratkaisemaan yhtä sudokua. Vielä kuitenkaan vastausta ei pysty palauttamaan. 

## Käyttöohje

Sovelluksen valikoiden välillä voi liikkua nuolinäppäimillä. Alavalikkoon pääsee painamalla ENTER-näppäintä ja takaisin päävalikkoon pääsee painamalla BACKSPACE-näppäintä. Sudokun ratkaisu tilassa ohjeet näkyvät oikealla puolella ikkunaa. 

## Dokumentaatio

- [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)
- [Arkkitehtuurikuvaus](./dokumentaatio/arkkitehtuuri.md)
- [Työaikakirjanpito](./dokumentaatio/tuntikirjanpito.md)

## Asennus

Sovellus on tehty käyttäen Python-versiota `3.8.6`. Muiden versioiden toiminnasta ei ole takuuta. Huomaa, että joissakin koneissa voit joutua korvaamaan komennon `python` komennolla `python3`.

1. Asenna riippuvuudet
```bash
python -m pipenv install
```
2. Käynnista sovellus komennolla:
```bash
python -m pipenv run start
```

## Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelman voi suorittaa komennolla:

```bash
python -m pipenv run start
```

### Testaus

Testit voi suorittaa komennolla:

```bash
python -m pipenv run test
```

### Testikattavuus

Testikattavuudet voi luoda komennoilla:

```bash
python -m pipenv run coverage
```
```bash
python -m pipenv run coverage-report
```
Raportti on sitten generoitunut htmlcov-hakemistoon ja sen voi katsoa avaamalla index.html tiedoston selaimella. 

### Laatutarkastus

Laatutarkastukset voidaan suorittaa komennolla:

```bash
python -m pipenv run lint
```
