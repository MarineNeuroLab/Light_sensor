"""
Print out values from a TSL2591 light sensor when the BOOT button on the QT Py is pressed
Description: https://learn.adafruit.com/adafruit-tsl2591/python-circuitpython
"""

import time
import board
import busio
import digitalio
import adafruit_tsl2591
import neopixel

i2c = busio.I2C(board.SCL1, board.SDA1)  # Create sensor object
sensor = adafruit_tsl2591.TSL2591(i2c)  # Initialise the sensor
Bbutton = digitalio.DigitalInOut(board.BUTTON) #Instantiate the boot button on the QT Py
pixels = neopixel.NeoPixel(board.NEOPIXEL, 1) # Instantiate neopixel LED
pixels[0] = (0, 5, 0)  # Set the QT Py neopixel to a dim green

### SETTINGS #########################################################

### Choose which sensor gain to use
# sensor.gain = adafruit_tsl2591.GAIN_LOW # 1x gain (for bright light)
sensor.gain = adafruit_tsl2591.GAIN_MED  # 25x gain
# sensor.gain = adafruit_tsl2591.GAIN_HIGH # 428x gain
# sensor.gain = adafruit_tsl2591.GAIN_MAX # 9876x gain (for dim light)

### Choose which sensor integration time to use
sensor.integration_time = adafruit_tsl2591.INTEGRATIONTIME_100MS
# sensor.integration_time = adafruit_tsl2591.INTEGRATIONTIME_200MS
# sensor.integration_time = adafruit_tsl2591.INTEGRATIONTIME_300MS
# sensor.integration_time = adafruit_tsl2591.INTEGRATIONTIME_400MS
# sensor.integration_time = adafruit_tsl2591.INTEGRATIONTIME_500MS
# sensor.integration_time = adafruit_tsl2591.INTEGRATIONTIME_600MS

######################################################################

# Main code
record = False #The value of this variable determines if sensor values are to be recorded. Will be set to TRUE when the BOOT button on the QT Py is pressed

while True: #Do the following continuously:
    Bbutton_state = Bbutton.value  #Check the state of the BOOT button
    pixels[0] = (0, 0, 5)  #Make the QT Py neopixel a dim blue to indicate it is idle

    if not Bbutton_state:  #If the BOOT button is pressed:
        record = True #Change this value to indicate that sensor values should be recorded
        time.sleep(0.5) #Introduce a delay to reduce sensitivity to button pressing speeds

        while record is True: #Until the BOOT button is pressed again:
            Bbutton_state = Bbutton.value  #Keep checking the state of the boot button
            pixels[0] = (0, 0, 0)  #Turn off the QT Py neopixel to indicate that recording is in progress

            """
            Things that that the sensor can measure:
            print('Total light: {0}lux'.format(sensor.lux))
            print('Visible: {0}'.format(sensor.visible)) #Range: 0-2147483647 (32 bit)
            print('Infrared: {0}'.format(sensor.infrared)) #Range: 0-65535 (16 bit)
            print('Full spectrum: {0}'.format(sensor.full_spectrum)) #visible & infrared light, Range: 0-2147483647 (32 bit)
            #raw_luminosity also exists: "A 2-tuple of raw sensor visible+IR and IR only light levels.  Each is a 16-bit value with no units where the higher the value the more light."
            """
            # Print out the values that should be kept to the serial port
            print("{},{},{}".format(sensor.lux, sensor.visible, sensor.infrared))
            #time.sleep(0.5) #Introduce a delay (in seconds) if you want to modify the frequency at which readings are taken

            if not Bbutton_state:  #If the BOOT button is pressed again, stop producing output/recording sensor values
                record = False
                print("Stopped")
                time.sleep(1)