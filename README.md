# Light_sensor
Save sensor data from a [TSL2591 light sensor](https://learn.adafruit.com/adafruit-tsl2591/) ([instructions](https://learn.adafruit.com/adafruit-tsl2591/python-circuitpython)) connected to a [QT Py RP2040](https://www.adafruit.com/product/4900)

## How it works
When the 'boot' button on the QT Py is pressed, it sends data from the light sensor through a USB cable to a computer that saves the data in a csv file until the 'boot' button is pressed again.

## Requirements
You need to have the python package [serial](https://pythonhosted.org/pyserial/) installed in your environment.

## Setup

After you have set up the QT Py according to these [instructions](https://learn.adafruit.com/adafruit-qt-py-2040/circuitpython), copy over the following to the "lib" folder on your CIRCUITPY (D:) drive from one of the [CircuitPython library bundles](https://circuitpython.org/libraries):
#### Files:
- adafruit_tsl2591.mpy
- neopixel.mpy

#### Folders:
- adafruit_bus_device
- adafruit_circuitplayground

Then copy the contents of the "code.py" file in this repository into the "code.py" file on your CIRCUITPY (D:) drive.

