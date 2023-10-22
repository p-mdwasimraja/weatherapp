from flask import Flask, render_template, request, escape
import requests
import json
import markupsafe

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("index.html")

@app.route("/weatherapp", methods = ['POST' , "GET"])
def get_weatherdata():
    url = "https://api.openweathermap.org/data/2.5/weather"
    param = {
        'q':request.form.get("city"),
        'appid':request.form.get("appid"),
        'units':request.form.get("units")
    }
    response = requests.get(url,params=param)
    data = response.json()
    return f"data : {data}"

    # Extract relevant data from the API response
    #city = data.get("name")
    #temperature = data.get("main").get("temp") - 273.15  # Convert to Celsius
    #weather = data.get("weather")[0].get("description")

    #return render_template("index.html", city=city, temperature=temperature, weather=weather)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port = 5001)
