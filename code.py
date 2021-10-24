# Description: https://learn.adafruit.com/adafruit-tsl2591/python-circuitpython

#import time
import board
import busio
import adafruit_tsl2591
import neopixel

i2c = busio.I2C(board.SCL1, board.SDA1)  # Create sensor object
sensor = adafruit_tsl2591.TSL2591(i2c)  # Initialise the sensor
pixels = neopixel.NeoPixel(board.NEOPIXEL, 1) # Instantiate neopixel LED

### SETTINGS #########################################################

### Choose which sensor gain to use
sensor.gain = adafruit_tsl2591.GAIN_LOW # 1x gain (for bright light)
#sensor.gain = adafruit_tsl2591.GAIN_MED  # 25x gain
#sensor.gain = adafruit_tsl2591.GAIN_HIGH # 428x gain
#sensor.gain = adafruit_tsl2591.GAIN_MAX # 9876x gain (for dim light)

### Choose which sensor integration time to use
sensor.integration_time = adafruit_tsl2591.INTEGRATIONTIME_100MS
# sensor.integration_time = adafruit_tsl2591.INTEGRATIONTIME_200MS
# sensor.integration_time = adafruit_tsl2591.INTEGRATIONTIME_300MS
# sensor.integration_time = adafruit_tsl2591.INTEGRATIONTIME_400MS
# sensor.integration_time = adafruit_tsl2591.INTEGRATIONTIME_500MS
#sensor.integration_time = adafruit_tsl2591.INTEGRATIONTIME_600MS

######################################################################

# Main code
while True: #Do the following continuously:

    pixels[0] = (0, 0, 0)  #Turn off the QT Py neopixel to indicate that the code is running

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
    #time.sleep(0.5) #Introduce a delay if you want readings to be taken at a set rate
