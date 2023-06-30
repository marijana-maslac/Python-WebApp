# Python-WebApp

Sveučilišni odjel za stručne studije, Informacijska Tehnologija - 3. godina, 6. semestar
2022/2023

Nositeljica predmeta: Marina Rodić, v. pred.  

## Running locally  

Clone the repository:
```bash
git clone https://github.com/marijana-vranjes/Python-WebApp.git
```

Move into cloned directory: 
```bash
cd Python-WebApp
```

Create a virtual environment:
```bash
python -m venv venv
```

Activate the virtual environment:
```bash
venv\Scripts\activate
```

Move into directory with project files:
```bash
cd Projekt2023PNI
```

Install the requirements:
```bash
pip install -r requirements.txt
```

Apply migrations to database:
```bash
python manage.py migrate
```

Run app:
```bash
python manage.py runserver
```
The development server will be started at http://127.0.0.1:8000/  

# Zadatak za projekt

Izraditi sustav za upis studenata.  
Sustav ce se sastojati od tri uloge: **student**, **profesor** i **administrator**.

- Uloga administrator:
    - autentikacija
    - pregled i promjena liste predmeta
    - dodavanje novog predmeta
    - dodjeljivanje predmeta profesoru
    - pregled liste studenata
    - dodavanje i editiranje studenata
    - izrada/promjena upisnog lista za bilo kojeg studenta
    - pregled liste profesora
    - dodavanje i editiranje profesora
    - pregled popisa studenata za svaki pojedinacni predmet (na svaki predmet dodati link „vidi popis studenata”)
    - za administrator ulogu nije dozvoljeno koristiti Djangov admin sustav  

- Uloga profesor:
    - autentikacija
    - pregled liste predmeta prijavljenog profesora
    - pregled popisa studenata na pojedinom kolegiju (kojem je prijavljeni profesor nositelj)
    - mijenjanje statusa predmeta (po defaultu je samo upisan, a moze se promijeniti u „polozen” ili „izgubio potpis”. Predmet se moze ispisati sve dok mu status nije promijenjen u polozen/izgubio potpis)
    - pregled studenata na svakom pojedinom predmetu prema sljedecim kriterijima:
        1. studenti koji su izgubili potpis
        2. studenti koji su dobili potpis, ali jos nisu polozili predmet
        3. studenti koji su polozili predmet  

- Uloga student:
    - autentikacija
    - upis/ispis predmeta  

## Pravila
Obrana projekta se održava u sklopu ispita. Sastojati će se od pismenog ispita, u vidu jednog ili više zadataka (npr. dodati linkove koji vode na opise predmeta uz prikaz liste predmeta i sl.) kojeg je potrebno odraditi u zadanom vremenskom roku. Nakon pismenog ispita organizirati će se usmeni ispit. Na usmenom ispitu će svaki student prezentirati svoj projekt, te će trebati odgovarati na pitanja vezana uz kôd u projektu. Primjerice - pokazati kroz kôd kako se upiše novi predmet. Projekt je potrebno predati najkasnije tri radna dana prije planiranog ispitnog roka (ako je ispit u utorak-projekt je potrebno predati najkasnije do cetvrtka do 23.59 sati ili ako je ispit u petak projekt je potrebno predati najkasnije do utorka do 23.59 sati). Zakašnjeli projekti se automatizmom prebacuju na idući ispitni rok.
