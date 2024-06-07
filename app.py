import requests
import geopy
import joblib
import os

# Load the trained model
model = joblib.load('hackathonrf.joblib')

# Define AQI category labels
aqi_labels = {
    0: 'good',
    1: 'moderate',
    2: 'unhealthy_sensitive',
    3: 'unhealthy',
    4: 'very_unhealthy',
    5: 'hazardous'
}

# Function to get latitude and longitude from location name
def get_coordinates(location):
    geolocator = geopy.geocoders.Nominatim(user_agent="air_quality_app")
    location = geolocator.geocode(location)
    return location.latitude, location.longitude

# Function to get AQI value from OpenWeatherMap API
def get_aqi(latitude, longitude):
    api_key = os.getenv('OPENWEATHER_API_KEY')
    url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={latitude}&lon={longitude}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    aqi_value = data['list'][0]['main']['aqi']
    return aqi_value

# Function to make prediction
def predict_air_quality(location):
    latitude, longitude = get_coordinates(location)
    aqi_value = get_aqi(latitude, longitude)
    prediction = model.predict([[aqi_value, aqi_value, aqi_value, aqi_value]])
    label_string = aqi_labels[prediction[0]]
    return f"{location} air quality is currently '{label_string}'"

if __name__ == "__main__":
    location = input("Enter location: ")
    result = predict_air_quality(location)
    print(result)
