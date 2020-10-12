# My smart city Zadar
## Radionica - web programiranje u Pythonu (Flask)
U ovoj radionici pokazali smo kako konzumirati podatke o vremenu u nekom gradu, te ih prikazati na web stranici

## Upute za pokretanje aplikacije
* klonirajte repozitorij: git clone https://github.com/nikovrdoljak/mysczd_flask
* uđite u stvorenu mapu: cd .\mysczd_flask\ 
* kreirajte virtualnu okolinu: python -m venv venv
* aktivirajte virtualnu okolinu (powershell): .\venv\Scripts\Activate.ps1
* instalirajte pakete: pip install -r requirements.txt
* postavite ENV varijablu: $env:FLASK_APP="main.py"
* u datoteci main.py postavite u liniji 11 vaš API KEY za OpenWeather
* pokrenite aplikaciju: flask run
* otvorite u web pregledniku: http://127.0.0.1:5000/

## Detaljnije o Flasku
[Uvof u Flask](https://medium.com/@nikovrdoljak/uvod-u-flask-3859458237f7)
