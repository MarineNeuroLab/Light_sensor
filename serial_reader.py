"""
Read sensor data from a TSL2591 light sensor through a QT Py 2040 connected to your PC via USB

Inspired by https://makersportal.com/blog/2018/2/25/python-datalogger-reading-the-serial-output-from-arduino-to-analyze-data-using-pyserial
and
https://github.com/kavli-ntnu/wheel_tracker/blob/master/save_tracking.py
"""

import serial
from datetime import datetime

ser = serial.Serial('COM3') #The port to read from (i.e. the USB port the QT Py is connected to)
ser.flushInput() #This clears the serial buffer so everything is ready to go

# Specify which folder to save the data in
root_folder = 'C:/DATA/Sensor_data' 

# Get the current time
now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

# Create a cvs file with a name based on the current time in the root folder specified 
output_file='{}/{}_light.csv'.format(root_folder, now)

# Main code:
with open(output_file,"a") as f: #Open the csv file
    f.write('Timestamp,Total light (lux),Visible (0-2147483647),Infrared (0-65535)\n') #Add headers to the file. Numbers in brackets are the ranges of possible values

    print("Ready") #Print out a message in the terminal to indicate that the program is ready to go

    while True: #If the BOOT button on the QT Py is pressed, the following code is executed:
            ser_bytes = ser.readline() #Read one line from the port
            decoded_bytes = ser_bytes.decode('utf-8') #Convert the read data so it's legible
            decoded_bytes_split = decoded_bytes.strip().split(',') #Strip away the prefix and suffix characters, and split the values using the comma as the separator
            
            if "Stop" in decoded_bytes: #If one of the lines contains the word "stop", this indicates that the BOOT button on the QT Py has been pressed again and the program should be terminated
                print("Stopped")
                f.close() #Close the file
                break

            else: #Until the BOOT button is pressed a second time, do the following:
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
