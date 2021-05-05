import mysql.connector
import bme280_sensor
import time
import importlib
import datetime

cnx = mysql.connector.connect(
  host = "domain.com",
  database = "database",
  user = "user",
  password = "password"
)

primarykey = datetime.datetime.now()
temperature = bme280_sensor.temperature
humidity = bme280_sensor.humidity
pressure = bme280_sensor.pressure
feelslike = bme280_sensor.feels
dewpoint = bme280_sensor.dewpoint

cursor = cnx.cursor()
sql = "INSERT INTO weather_data (datetime, temperature, humidity, pressure, feels, dewpoint) VALUES (%s, %s, %s, %s, %s, %s, %s)"
val = (primarykey, temperature, humidity, pressure, feelslike, dewpoint)

def send_to_db():
  cursor.execute(sql, val)
  cnx.commit()
  cursor.close()
  cnx.close()

def print_all_the_things():
  print("Datetime:", primarykey)
  print("Temp:", temperature)
  print("Humidity:", humidity)
  print("Pressure:", pressure)
  print("Feelslike:", feelslike)
  print("Dewpoint:", dewpoint)

# send_to_db()

# print_all_the_things
