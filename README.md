# Light_sensor
Save data from a [TSL2591 light sensor](https://learn.adafruit.com/adafruit-tsl2591/) ([instructions](https://learn.adafruit.com/adafruit-tsl2591/python-circuitpython)) connected to a [QT Py RP2040](https://www.adafruit.com/product/4900) with a [STEMMA QT cable](https://www.adafruit.com/product/4399) and your PC via USB and save this data in a .csv file and as a plot at a specified time once per day

## How it works
When the serial_reader.py file is run, it continuously saves data from the light sensor in a csv file on your computer until a user-defined time of day has been reached. It then closes the .csv file, creates and saves a plot of the saved data, and then creates a new .csv file to repeat the process. I.e. measurements are automatically saved once a day.

<img src="QTPy_with_lightsensor.jpg" alt="QT Py with light sensor in front of a screen that displays the light values being printed out" width="400"/>

## Requirements
You need to have the python packages [serial](https://pythonhosted.org/pyserial/) installed in your environment.

## Setup and use instructions

- Connect the QT Py to your computer via USB
- Configure the QT Py according to [these instructions](https://learn.adafruit.com/adafruit-qt-py-2040/circuitpython) if you have not already done so
- Copy over the following to the "lib" folder on your CIRCUITPY (D:) drive from one of the [CircuitPython library bundles](https://circuitpython.org/libraries):

  **Files:**
  - adafruit_tsl2591.mpy
  - neopixel.mpy

  **Folders:**
  - adafruit_bus_device
  - adafruit_circuitplayground

- Connect the light sensor to the QT Py with the STEMMA QT cable
- Copy the contents of the *code.py* file in this repository into the *code.py* file on your CIRCUITPY (D:) drive. The LED on the QT Py will turn off to indicate that the code is running
- Specify which USB port the QT Py is connected to by modifying the 'ser' variable within *serial_reader.py* (default port: COM3)
- Specify the required values in the 'INPUT' section in *serial_reader.py*
- Run the *serial_reader.py* file in your terminal to start recording light values. These will also be printed out in your terminal
- A .csv file with the recorded values and timestamps, plus a plot with the same information, will be saved in the location you specified within *serial_reader.py* once the time you specified has been reached

**Tip:** you can modify the gain and integration time of the light sensor, and set the frequency at which measurements should be collected, under 'SETTINGS' in the *code.py* file.

