# Air Quality Monitor

This repository provides a script that retrieves Air Quality Index (AQI) data from the OpenWeatherMap API based on user-inputted locations. It aimed to provide real-time air quality data to residents and policymakers in areas affected by industrial pollution for health and safety purposes.

## How It Works

The `app.py` file receives a location input from the user, converts it to coordinates, retrieves the AQI using OpenWeatherMap, and prints the location's AQI followed by the current air quality condition.

## Instructions

### Setup

1. **Create an OpenWeather Account**:
    - Create an account on [OpenWeather](https://home.openweathermap.org/users/sign_up).
    - Obtain your free API key from OpenWeather.

2. **Clone the Repository**:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up OpenWeather API Key**:
    - **On Unix-based systems (Linux, macOS)**:
        ```bash
        export OPENWEATHER_API_KEY='your_api_key_here'
        ```
    - **On Windows (Command Prompt)**:
        ```cmd
        set OPENWEATHER_API_KEY=your_api_key_here
        ```
    - **On Windows (PowerShell)**:
        ```powershell
        $env:OPENWEATHER_API_KEY = "your_api_key_here"
        ```

5. **Run the Application**:
    ```bash
    python app.py
    ```

## USA Air Quality Index Levels

Below is a description of USA Air Quality Index levels:

| AQI        | Level of Health Concern               | Color  |
|------------|---------------------------------------|--------|
| 0 to 50    | Good                                  | Green  |
| 51 to 100  | Moderate                              | Yellow |
| 101 to 150 | Unhealthy for Sensitive Groups        | Orange |
| 151 to 200 | Unhealthy                             | Red    |
| 201 to 300 | Very Unhealthy                        | Purple |
| 301 to 500 | Hazardous                             | Maroon |
| 501 to 1000| Very Hazardous                        | Brown  |
