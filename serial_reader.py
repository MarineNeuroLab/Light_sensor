"""
Read sensor data from a TSL2591 light sensor through a QT Py 2040 connected to your PC via USB

Inspired by https://makersportal.com/blog/2018/2/25/python-datalogger-reading-the-serial-output-from-arduino-to-analyze-data-using-pyserial
and
https://github.com/kavli-ntnu/wheel_tracker/blob/master/save_tracking.py
"""

import serial
import keyboard
from datetime import datetime

ser = serial.Serial('COM3') #The port to read from (i.e. the USB port the QT Py is connected to)
ser.flushInput() #This clears the serial buffer so everything is ready to go

# Specify which folder to save the data in
root_folder = 'C:/DATA/Sensor_data' 

# Get the current time
now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

# Create a cvs file with a name based on the current time in the root folder specified 
output_file='{}/{}_light.csv'.format(root_folder, now)

# While this variable is True, values will be recorded
record = True

#If the key under keyboard.add_hotkey is pressed, this function is invoked and record is set to False
def stop_recording(): 
    global record #Make this variable global
    record=False
keyboard.add_hotkey('s', stop_recording) #Specify which key to press to stop recording values (default = s)

# Main code:
f = open(output_file,"a") #Open the csv file
f.write('Timestamp,Total light (lux),Visible (0-2147483647),Infrared (0-65535)\n') #Add headers to the file. Numbers in brackets are the ranges of possible values

while record: #While record = True, run the following code to record and save light values in output_file

    ser_bytes = ser.readline() #Read one line from the port
    decoded_bytes = ser_bytes.decode('utf-8') #Convert the read data so it's legible
    decoded_bytes_split = decoded_bytes.strip().split(',') #Strip away the prefix and suffix characters, and split the values using the comma as the separator
    
    # Extract the different light values and convert them to floats
    lux_value = float(decoded_bytes_split[0])
    visible_value = float(decoded_bytes_split[1])
    ir_value = float(decoded_bytes_split[2])

    # Get the current time
    now = datetime.now().strftime('%Y-%m-%d_%H:%M:%S.%f')
    
    # Print out the values in the terminal
    print('{} | Light: {} lux | Visible: {} | IR: {}'.format(now[0:-7],lux_value,visible_value,ir_value))
    
    # Save the values in the csv file
    f.write('{},{},{},{}\n'.format(now,lux_value,visible_value,ir_value))

f.close() #Close the file when record is no longer True
print('Finished saving light values')