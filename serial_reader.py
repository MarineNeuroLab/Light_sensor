"""
Read sensor data from a TSL2591 light sensor through a QT Py 2040 connected to your PC via USB
and save this data in a .csv file and as a plot at a specified time once per day
Note: the filename for the .csv file contains the time when that file was created,
while the filename for the plot (.png file) contains the time when the measurements *finished* saving to file

Inspired by https://makersportal.com/blog/2018/2/25/python-datalogger-reading-the-serial-output-from-arduino-to-analyze-data-using-pyserial
and
https://github.com/kavli-ntnu/wheel_tracker/blob/master/save_tracking.py
"""

####### INPUT ######################################################################
# Specify which folder to save the data in
root_folder = 'C:/DATA/Sensor_data' 

# Specify the time (in 24hr clock format) when a new file should be made (e.g. every day at midnight)
newfile_hour = 0
newfile_min = 0

# Specify the delay between measurements to be saved (in seconds) 
# NOTE: this is not precise as it doesn't take into consideration the time it takes to run the code itself
# Range: 0.5-50 seconds
delay = 1

# Speciy which port to read the data from (i.e. the USB port the QtPy is connected to)
port = 'COM10'
####################################################################################

import serial
from datetime import datetime
import time
import matplotlib.pyplot as plt
import numpy as np

ser = serial.Serial(port) #Specify which port to read from 
ser.flushInput() #This clears the serial buffer so everything is ready to go


timestart = datetime.now().strftime('%Y-%m-%d_%H:%M:%S.%f') # Get the current time (as a string)
current_file = '_'

# Main code:
while True: # While True, run the following code to record and save light intensity values in the output file specified
    # Get the current time
    now_file = datetime.now().strftime('%Y-%m-%d') # This changes only at midnight every day! 
    
    # Create a cvs file with a name based on the current time in the root folder specified 
    output_file=f'{root_folder}/{now_file}_light.csv'
    if output_file != current_file: 
        # New file name detected 
        with open(output_file,"w") as f: # Open the file and write header 
            f.write('Timestamp,Total light (lux),Visible (0-2147483647),Infrared (0-65535)\n') # Add headers to the file. Numbers in brackets are the ranges of possible values
    current_file = output_file # Prevent writing header until date changes 
        
    # Create empty lists to save measurements in (for plotting later)
    now = datetime.now().strftime('%Y-%m-%d_%H:%M:%S.%f')
    write_to_file = True
    try: 
        ser_bytes = ser.readline() #Read one line from the port
        if not ser_bytes: 
            # If nothing arrived via serial ...
            write_to_file = False 
        else: 
            decoded_bytes = ser_bytes.decode('utf-8') # Convert the read data so it's legible
            decoded_bytes_split = decoded_bytes.strip().split(',') # Strip away the prefix and suffix characters, and split the values using the comma as the separator
            lux_value = float(decoded_bytes_split[0])
            visible_value = float(decoded_bytes_split[1])
            ir_value = float(decoded_bytes_split[2])
    except: # If "ANY" error occurrs ... this can be made more specific ... 
        lux_value = np.nan
        visible_value = np.nan
        ir_value = np.nan
        
    if write_to_file:   
        with open(output_file,"a") as f: # Open the file and append values 
            f.write(f'{now},{lux_value},{visible_value},{ir_value}\n')

    # Print out the values in the terminal
    print('{} | Light: {} lux | Visible: {} | IR: {}'.format(now[0:-7],lux_value,visible_value,ir_value))