from flask import Flask, render_template, request
import requests
import pytz

app = Flask(__name__)


@app.route('/temperature', methods=['POST'])
def temperature():
    """Api call to get lat + lon after user input"""
    location = request.form['country']
    appid = Your Api
    api = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={appid}"
    try:
        json_object = requests.get(api).json()
        response = requests.get(api)
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        return "404 Page not found"

    lat = str(json_object['coord']['lat'])
    lon = str(json_object['coord']['lon'])
    country1 = json_object['sys']['country']
    countryname = pytz.country_names[country1]


    """Api call to get the tempatures"""
    api = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&units=metric&exclude=current,minutely,hourly,alerts&appid={appid}"

    json_object = requests.get(api).json()
    del json_object['daily'][7]
    return render_template('temperature.html', city=location, country=countryname, daily=json_object['daily'])



@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

