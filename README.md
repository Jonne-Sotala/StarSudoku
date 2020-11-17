# Sudoku sovellus

## Dokumentaatio

- [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](./dokumentaatio/tuntikirjanpito.md)

## Asennus

Sovellus on tehty kayttaen Python-versiota `3.8.6`. Muiden versioiden toiminnasta ei ole takuuta. Huomaa, etta joissakin koneissa voit joutua korvaamaan komennon `python` komennolla `python3`.

1. Asenna riippuvuudet
```bash
python -m pipenv install
```
2. Kaynnista sovellus komennolla:
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
