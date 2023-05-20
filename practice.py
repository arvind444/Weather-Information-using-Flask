from flask import Flask, render_template, request
import requests

app = Flask(__name__)   # name of the app to use decorator

@app.route("/")
def home_page():
    return render_template("home.html")

@app.route("/result", methods=["POST", "GET"])
def result():
    city_name = request.form['city_name']

    if not city_name:
        return render_template("home.html")
    
    else:
        api_key = "1ab3a5f55b954b848b692717210807"
        url = "https://api.weatherapi.com/v1/current.json?key={}&q={}&aqi=yes".format(api_key, city_name)
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            date = data["location"]["localtime"]
            lat = data["location"]["lat"]
            lon = data["location"]["lon"]
            url_2 = "https://api.weatherapi.com/v1/astronomy.json?key={}&q={}&dt={}".format(api_key, city_name, date)
            response_2 = requests.get(url_2)
            data_2 = response_2.json()
            data_info = {"city" : data["location"]["name"],
                         "state" : data["location"]["region"],
                         "country" : data["location"]["country"],
                         "time_zone" : data["location"]["tz_id"],
                         "time" : data["location"]["localtime"],
                         "lat" : data["location"]["lat"],
                         "lon" : data["location"]["lon"],
                         "last_update" : data["current"]["last_updated"],
                         "temp_in_c" : data["current"]["temp_c"],
                         "temp_in_f" : data["current"]["temp_f"],
                         "weather_condition" : data["current"]["condition"]["text"],
                         "weather_image" : data["current"]["condition"]["icon"],
                         "wind_speed_in_m" : data["current"]["wind_mph"],
                         "wind_speed_in_k" : data["current"]["wind_kph"],
                         "wind_degree" : data["current"]["wind_degree"],
                         "wind_dir" : data["current"]["wind_dir"],
                         "pressure_mb" : data["current"]["pressure_mb"],
                         "pressure_in" : data["current"]["pressure_in"],
                         "precip_mm" : data["current"]["precip_mm"],
                         "precip_in" : data["current"]["precip_in"],
                         "humidity" : data["current"]["humidity"],
                         "cloud" : data["current"]["cloud"],
                         "feels_like_in_c" : data["current"]["feelslike_c"],
                         "feels_like_in_f" : data["current"]["feelslike_f"],
                         "vis_km" : data["current"]["vis_km"],
                         "vis_miles" : data["current"]["vis_miles"],
                         "uv" : data["current"]["uv"],
                         "gust_mph" : data["current"]["gust_mph"],
                         "gust_kph" : data["current"]["gust_kph"],
                         "co" : data["current"]["air_quality"]["co"],
                         "no2" : data["current"]["air_quality"]["no2"],
                         "o3" : data["current"]["air_quality"]["o3"],
                         "so2" : data["current"]["air_quality"]["so2"],
                         "pm_2.5" : data["current"]["air_quality"]["pm2_5"],
                         "pm_10" : data["current"]["air_quality"]["pm10"],
                         "us_index" : data["current"]["air_quality"]["us-epa-index"],
                         "gb_index" : data["current"]["air_quality"]["gb-defra-index"],
                         "sun_rise" : data_2["astronomy"]["astro"]["sunrise"],
                         "sun_set" : data_2["astronomy"]["astro"]["sunset"],
                         "moon_rise" : data_2["astronomy"]["astro"]["moonrise"],
                         "moon_set" : data_2["astronomy"]["astro"]["moonset"],
                         "moon_phase" : data_2["astronomy"]["astro"]["moon_phase"],
                         "moon_illumination" : data_2["astronomy"]["astro"]["moon_illumination"]}
            return render_template("result.html", data = data_info)
        
        else:
            return render_template("error.html", city=city_name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("home.html")

@app.errorhandler(405)
def page_not_found(e):
    return render_template("home.html")

@app.errorhandler(500)
def page_not_found(e):
    return render_template("home.html")

@app.errorhandler(400)
def page_not_found(e):
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=False)