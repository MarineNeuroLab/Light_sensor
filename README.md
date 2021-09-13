# Light_sensor
Save data from a [TSL2591 light sensor](https://learn.adafruit.com/adafruit-tsl2591/) ([instructions](https://learn.adafruit.com/adafruit-tsl2591/python-circuitpython)) connected to a [QT Py RP2040](https://www.adafruit.com/product/4900)

## How it works
When the 'boot' button on the QT Py is pressed, it continuously saves data from the light sensor in a csv file until the 'boot' button is pressed again.

<img src="QTPy_with_lightsensor.jpg" alt="QT Py with light sensor in front of a screen that displays the light values being printed out" width="400"/>

## Requirements
You need to have the python package [serial](https://pythonhosted.org/pyserial/) installed in your environment.

## Setup

- Configure the QT Py according to [these instructions](https://learn.adafruit.com/adafruit-qt-py-2040/circuitpython) if you have not already done so
- Copy over the following to the "lib" folder on your CIRCUITPY (D:) drive from one of the [CircuitPython library bundles](https://circuitpython.org/libraries):

  **Files:**
  - adafruit_tsl2591.mpy
  - neopixel.mpy

  **Folders:**
  - adafruit_bus_device
  - adafruit_circuitplayground

- Copy the contents of the *code.py* file in this repository into the *code.py* file on your CIRCUITPY (D:) drive
- Specify which folder the csv file should be saved in on your PC by modifying the 'root_folder' variable within *serial_reader.py* (default location: C:/DATA/Sensor_data)
- Run the *serial_reader.py* file in your terminal
- When the word 'Ready' is shown, press the 'boot' button on the QT Py to start recording light values. These will also be printed out in your terminal. The LED on the QT Py will turn off to indicate that the recording is in progress
- Press the 'boot' button again to stop recording values
- A csv file with the recorded values and timestamps can now be found in the location you specified

