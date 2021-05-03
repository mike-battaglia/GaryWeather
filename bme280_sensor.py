import bme280
import smbus2
import math
from datetime import datetime
from datetime  import date
from time import sleep
import sys
import numpy as np


port = 1
address = 0x77 # Adafruit BME280 address. Other BME280s may be different
bus = smbus2.SMBus(port)

bme280.load_calibration_params(bus,address)

# while True:
#    bme280_data = bme280.sample(bus,address)
#    humidity  = bme280_data.humidity
#    pressure  = bme280_data.pressure
#    ambient_temperature = bme280_data.temperature
#    print(humidity, pressure, ambient_temperature)
#    sleep(1)


bme280_data = bme280.sample(bus,address)
humidity  = int(bme280_data.humidity)
pressure  = int(bme280_data.pressure)
temperature = int(((bme280_data.temperature) * 1.8) + 32)

vTemperature = temperature
vWindSpeed = int(1)
vRelativeHumidity = humidity

# Try Wind Chill first
if vTemperature <= 50 and vWindSpeed >= 3:
  vFeelsLike = 35.74 + (0.6215*vTemperature) - 35.75*(vWindSpeed**0.16) + ((0.4275*vTemperature)*(vWindSpeed**0.16))
else:
  vFeelsLike = vTemperature

# Replace it with the Heat Index, if necessary
if vFeelsLike == vTemperature and vTemperature >= 80:
  vFeelsLike = 0.5 * (vTemperature + 61.0 + ((vTemperature-68.0)*1.2) + (vRelativeHumidity*0.094))

  if vFeelsLike >= 80:
    vFeelsLike = -42.379 + 2.04901523*vTemperature + 10.14333127*vRelativeHumidity - .22475541*vTemperature*vRelativeHumidity - .00683783*vTemperature*vTemperature - .05481717*vRelativeHumidity*vRelativeHumidity + .00122874*vTemperature*vTemperature*vRelativeHumidity + .00085282*vTemperature*vRelativeHumidity*vRelativeHumidity - .00000199*vTemperature*vTemperature*vRelativeHumidity*vRelativeHumidity
    if vRelativeHumidity < 13 and vTemperature >= 80 and vTemperature <= 112:
      vFeelsLike = vFeelsLike - ((13-vRelativeHumidity)/4)*math.sqrt((17-math.fabs(vTemperature-95.))/17)
      if vRelativeHumidity > 85 and vTemperature >= 80 and vTemperature <= 87:
        vFeelsLike = vFeelsLike + ((vRelativeHumidity-85)/10) * ((87-vTemperature)/5)

feels = vFeelsLike

now = datetime.now()

current_time = now.strftime("%H:%M")

today = date.today()

# Calculate Dewpoint

# approximation valid for
# 0 degC < T < 60 degC
# 1% < RH < 100%
# 0 degC < Td < 50 degC

# constants
a = 17.271
b = 237.7 # degC

T = bme280_data.temperature
RH = bme280_data.humidity

def dewpoint_approximation(T,RH):
    Td = (b * gamma(T,RH)) / (a - gamma(T,RH))
    return Td

def gamma(T,RH):
    g = (a * T / (b + T)) + np.log(RH/100.0)
    return g

dewpoint = int((dewpoint_approximation(T,RH) * 1.8) + 32)

# today
# current_time
# humidity
# pressure
# temperature
# feels

def print_all():
  print (today)
  print (current_time)
  print ("Humidity: ", humidity)
  print ("Pressure: ", pressure)
  print ("Temperature: ", temperature)
  print ("Feels Like: ", feels)
  print ("Dew Point: ", dewpoint)

#print_all()
#print("---")

def print_some():
  print (current_time)
  print ("T:", temperature)
  print ("H:", humidity)
  print ("P:", pressure)

#print_some()
