from flask import Flask, render_template
import requests
import babel
from babel.dates import format_datetime, get_timezone
app = Flask(__name__)

@app.route("/")
def index():
    # https://openweathermap.org/api
    url = 'https://api.openweathermap.org/data/2.5/weather'
    parameters = {'id': '3186952', 'appid': 'VAS_APP_ID', 'units': 'metric', 'lang': 'hr'}
    response = requests.get(url, parameters)
    weather = response.json()
    return render_template('index.html', weather = weather)

@app.template_filter('datetime')
def format_datetime(value, format='medium'):
    zadar = get_timezone('Europe/Berlin')
    if format == 'full':
        format="EEEE, d. MMMM y 'at' HH:mm"
    elif format == 'time':
        format="HH:mm"
    return babel.dates.format_datetime(value, format, tzinfo=zadar)