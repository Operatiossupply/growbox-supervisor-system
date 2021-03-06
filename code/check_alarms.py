########
# check alarms
# Version: V20-01-27 (This is a working BETA vesion)
# Todd Moore
# 1.27.20
#
# This project is released under The MIT License (MIT)
# Copyright 2019 Todd Moore
########

########
# # Code is compatible with Python 2.7 and Python 3.5.
#!/usr/bin/env python
# coding=utf-8
########

########
# # python module that checks temp, humidity, soil moisture, & sets alarms if too high or too low.
# also checks Gas Density & sets smoke alarm if too high.
########

from grovepi import digitalWrite
import config

def check_temp():
    # --------------------------------------------------------------------
    # check for temp alarm
    if config.HI_TEMP_ALARM > config.tempF > config.LO_TEMP_ALARM:
        config.temp_alarm = "OFF"
        config.blynk_temp_led_color = "#009900"   # LED is GREEN on blynk app 
    else:
        config.temp_alarm = "ON"
        config.blynk_temp_led_color = "#FF0000"   # LED is RED on blynk app

    if config.BME280_HI_TEMP_ALARM > config.bme280_tempF > config.BME280_LO_TEMP_ALARM:
        config.bme280_temp_alarm = "OFF"
        config.blynk_bme280_temp_led_color = "#009900"   # LED is GREEN on blynk app 
    else:
        config.bme280_temp_alarm = "ON"
        config.blynk_bme280_temp_led_color = "#FF0000"   # LED is RED on blynk app

    if (config.DEBUG):
        print("Temp Alarm is ", config.temp_alarm)
        print("BME280 Temp Alarm is ", config.bme280_temp_alarm)
        print("check_alarms.check_temp done")
   
def check_humidity():
    # --------------------------------------------------------------------
    # check for humidity alarm
    if config.HI_HUMID_ALARM > config.humidity > config.LO_HUMID_ALARM:
        config.humid_alarm = "OFF"
        config.blynk_humid_led_color = "#009900"   # LED is GREEN on blynk app
    else:
        config.humid_alarm = "ON"
        config.blynk_humid_led_color = "#FF0000"   # LED is RED on blynk app

    if config.BME280_HI_HUMID_ALARM > config.humidity > config.BME280_LO_HUMID_ALARM:
        config.bme280_humid_alarm = "OFF"
        config.blynk_bme280_humid_led_color = "#009900"   # LED is GREEN on blynk app
    else:
        config.bme280_humid_alarm = "ON"
        config.blynk_bme280_humid_led_color = "#FF0000"   # LED is RED on blynk app

    if (config.DEBUG):
        print("Humid Alarm is ", config.humid_alarm)
        print("BME280 Humid Alarm is ", config.bme280_humid_alarm)
        print("check_alarms.check_humidity done")
        
def check_moisture():
    # --------------------------------------------------------------------
    # Check if there is a soil moisture alarm
    #   Here are suggested sensor values:
    #       Min  Typ  Max  Condition
    #       0    0    0    sensor in open air
    #       0    20   300  sensor in dry soil
    #       300  580  700  sensor in humid soil
    #       700  940  950  sensor in water

    # Human Readable Sensor values: 
    # Values  Condition
    # --------------------------
    # 0-17    'AIR'
    # 18-424  'DRY'
    # 425-689 'HUMID'
    # 690+    'WATER'
    
    # convert moisture value to human readable text 
    if 17 >= config.moisture >= 0:
        config.moisture_alarm = 'AIR'
        config.blynk_moist_led_color = "#CC6600"   # # LED is ORANGE on blynk app
    elif 424 >= config.moisture >= 18:
        config.moisture_alarm = 'DRY'
        config.blynk_moist_led_color = "#CCCC00"   # # LED is YELLOW on blynk app
    elif 689 >= config.moisture >= 425:
        config.moisture_alarm = 'PERFECT'
        config.blynk_moist_led_color = "#009900"   # LED is GREEN on blynk app
    elif config.moisture >= 690:
        config.moisture_alarm = 'WATER'
        config.blynk_moist_led_color = "#0000CC"   # LED is BLUE on blynk app

    if 17 >= config.moisture2 >= 0:
        config.moisture2_alarm = 'AIR'
        config.blynk_moist2_led_color = "#CC6600"   # # LED is ORANGE on blynk app
    elif 424 >= config.moisture2 >= 18:
        config.moisture2_alarm = 'DRY'
        config.blynk_moist2_led_color = "#CCCC00"   # # LED is YELLOW on blynk app
    elif 689 >= config.moisture2 >= 425:
        config.moisture2_alarm = 'PERFECT'
        config.blynk_moist2_led_color = "#009900"   # LED is GREEN on blynk app
    elif config.moisture2 >= 690:
        config.moisture2_alarm = 'WATER'
        config.blynk_moist2_led_color = "#0000CC"   # LED is BLUE on blynk app

    if (config.DEBUG):
        print("Moisture Alarm is ", config.moisture_alarm)
        print("Moisture 2 Alarm is ", config.moisture2_alarm)
        print("check_alarms.check_moisture done")
      
# run main() function
if __name__ == "__main__":
    config.DEBUG = True
    check_temp()
    print("High Temp, Low Temp, Temp, & Temp Alarm Vectors are: ", config.HI_TEMP_ALARM, config.LO_TEMP_ALARM, 
            config.tempF, config.temp_alarm)
    
    print("BME280 High Temp, Low Temp, Temp, & Temp Alarm Vectors are: ", config.BME280_HI_TEMP_ALARM, config.BME280_LO_TEMP_ALARM, 
            config.bme280_tempF, config.bme280_temp_alarm)

    check_humidity()
    print("BME280 High Humid, Low Humid, Humidity, & Humidity Alarm Vectors are: ", config.BME280_HI_HUMID_ALARM, 
            config.BME280_LO_HUMID_ALARM, config.bme280_humidity, config.bme280_humid_alarm)

    print("High Humid, Low Humid, Humidity, & Humidity Alarm Vectors are: ", config.HI_HUMID_ALARM, 
            config.LO_HUMID_ALARM, config.humidity, config.humid_alarm)
 
    check_moisture()
    print("Moisture is: ", config.moisture)
