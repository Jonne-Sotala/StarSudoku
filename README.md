# StarSudoku

StarSudoku on sudokupeli. Sovellukseen voi tehdä käyttäjätunnuksen ja sitten sovelluksen käyttäjä voi ratkaista erilaisia sudokuongelmia. Tällä hetkellä sudokusovellukseen on valmiiksi ladattuna 9 sudokuongelmaa, joista 3 on helppoja, 3 keskitasoisia ja 3 vaikeita. Sovellus ajastaa ratkaisut ja kirjaa ratkaisut muistiin käyttäjäkohtaisesti. 

## Julkaisut

- [StarSudoku v1.0](https://github.com/Jonne-Sotala/StarSudoku/releases/tag/v1.0)
- [Viikko 6](https://github.com/Jonne-Sotala/ot-harjoitustyo/releases/tag/viikko6)
- [Viikko 5 ](https://github.com/Jonne-Sotala/ot-harjoitustyo/releases/tag/viikko5-hotfix)

## Dokumentaatio

- [Käyttöohje](./dokumentaatio/kayttoohje.md)
- [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)
- [Arkkitehtuurikuvaus](./dokumentaatio/arkkitehtuuri.md)
- [Testausdokumentti](./dokumentaatio/testaus.md)
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

