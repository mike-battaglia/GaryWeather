import mysql.connector
import bme280_sensor
import time
import importlib

cnx = mysql.connector.connect(
)

# print(cnx)

# while True:
#  time.sleep(3)
#  print(bme280_sensor.today)
#  print(bme280_sensor.current_time)
#  print(bme280_sensor.temperature)
#  print(bme280_sensor.pressure)
#  print(bme280_sensor.humidity)
#  print(bme280_sensor.feels)
#  print(bme280_sensor.dewpoint)
#  time.sleep(6)
#  importlib.reload(bme280_sensor)
#  time.sleep(3)

def send2db():
  date = bme280_sensor.today
  ctime = bme280_sensor.current_time
  temperature = bme280_sensor.temperature
  humidity = bme280_sensor.humidity
  pressure = bme280_sensor.pressure
  feelslike = bme280_sensor.feels
  dewpoint = bme280_sensor.dewpoint
  print(ctime)
  cursor = cnx.cursor()
  sql = "INSERT INTO weather_data (date, time, temperature, humidity, pressure, feels, dewpoint) VALUES (%s, %s, %s, %s, %s, %s, %s)"
  val = (date, ctime, temperature, humidity, pressure, feelslike, dewpoint)
  cursor.execute(sql, val)
  cnx.commit()
  cursor.close()
  cnx.close()
  time.sleep(60)
  importlib.reload(bme280_sensor)
#  print(date, time)
#  print("T: ", temperature, "F")
#  print("H: ", humidity, "%")
#  print("P: ", pressure, "mb")
#  print("F:", feelslike, "F")
#  print("D:", dewpoint, "F")


#while True:
#  time.sleep(3)
#  send2db()
#  time.sleep(3)

send2db()
