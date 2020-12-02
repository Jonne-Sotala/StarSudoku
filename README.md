# Sudoku sovellus

## Projektin tila

Tällä hetkellä sovelluksessa on kirjautumisnäkymä, jossa voi kirjautua, luoda käyttäjän ja poistaa käyttäjiä. Lisäksi on valikot, joita navigoimalla pääsee ratkaisemaan yhtä sudokua. Vielä kuitenkaan vastausta ei pysty palauttamaan ja sudoku on ennaltamäärätty ja sitä ei pysty vaihtamaan. 

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
2. Alusta sovellus
```bash
python -m pipenv run build
```
3. Käynnista sovellus komennolla:
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

## Releases

[Viikko 5](https://github.com/Jonne-Sotala/ot-harjoitustyo/releases/tag/viikko5)
