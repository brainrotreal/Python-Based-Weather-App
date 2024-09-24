import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QFont

class WeatherApp(QMainWindow):
    def __init__(self):
        super().__init__()
        # Set up window settings UwU
        self.setWindowTitle("Weather Application")
        self.setGeometry(100, 100, 400, 200)
        self.setStyleSheet("background-color: #F0F0F0;")

        # Cweate w-wabew fow city input OwO
        self.location_label = QLabel("Enter City:", self)
        self.location_label.move(20, 20)
        self.location_label.setFont(QFont("Arial", 12))

        # Cweate input box fow the city name UwU
        self.location_input = QLineEdit(self)
        self.location_input.move(120, 20)
        self.location_input.resize(200, 25)
        self.location_input.setStyleSheet("border: 2px solid #808080; border-radius: 5px; padding: 5px;")

        # Button to get the weathwer *boop* >w<
        self.get_weather_button = QPushButton("Get Weather", self)
        self.get_weather_button.move(150, 60)
        self.get_weather_button.clicked.connect(self.get_weather)
        self.get_weather_button.setStyleSheet("background-color: #4CAF50; color: white; border: none; padding: 10px 20px; border-radius: 5px;")

        # Wabew to dispway the weathwer wesuwt uwu
        self.weather_label = QLabel("", self)
        self.weather_label.move(20, 100)
        self.weather_label.resize(360, 80)
        self.weather_label.setStyleSheet("background-color: #E0E0E0; border-radius: 5px; padding: 10px; font-size: 14px;")

    def get_weather(self):
        # Get city nyame from the input box OwO
        city = self.location_input.text()
        api_key = "YOUR_API_KEY" # Visit https://openweathermap.org/api and subscwibe to get an API key, then insewt the API key hewe UwU.
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        
        try:
            # Send wequest to get the weathwer data >w<
            response = requests.get(url)
            data = response.json()
            # Dispway the weathwer wesuwt in the wabew OwO
            weather = f"Weather in {city}: {data['weather'][0]['description']}\nTemperature: {data['main']['temp']}°C\nHumidity: {data['main']['humidity']}%"
            self.weather_label.setText(weather)
        except Exception as e:
            # Dispway an ewwow message if somethwing goes wwong >_<
            self.weather_label.setText(f"Error: {e}")

if __name__ == "__main__":
    # Set up and wun the PyQt app UwU
    app = QApplication(sys.argv)
    window = WeatherApp()
    print("Working")
    window.show()
    sys.exit(app.exec_())
