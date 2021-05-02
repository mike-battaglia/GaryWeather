import mysql.connector
import bme280_sensor
import time
import importlib
import mysqlcreds

bme_date = bme280_sensor.today
bme_time = bme280_sensor.current_time
bme_temperature = bme280_sensor.temperature
bme_pressure = bme280_sensor.pressure
bme_humidity = bme280_sensor.humidity
bme_feels = bme280_sensor.feels
bme_dewpoint = bme280_sensor.dewpoint

db = mysql.connector.connect(
  user = "w",
  password = "x",
  host = "y",
  database = "z"
)

print(db)

# cur = db.cursor()

# sql = "INSERT INTO weatheer_data (date, time, temperature, humidity, pressure, feels, dewpoint) VALUES (%s, %s, %s, %s, %s, %s, %s)"
# val = (bme_date, bme_time, bme_temperature, bme_humidity, bme_pressure, bme_feels, bme_dewpoint)

# while True:
#  time.sleep(3)
#  print("Clock", bme_time)
#  print("Temp:", bme_temperature)
#  time.sleep(6)
#  importlib.reload(bme280_time)
#  time.sleep(3)

# leaving off here, data is not refreshing between iterations
