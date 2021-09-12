# Read sensor data from a TSL2591 light sensory being recorded by QT Py 2040

# Inspired by https://makersportal.com/blog/2018/2/25/python-datalogger-reading-the-serial-output-from-arduino-to-analyze-data-using-pyserial
# and
# https://github.com/kavli-ntnu/wheel_tracker/blob/master/save_tracking.py

import serial
from datetime import datetime

ser = serial.Serial('COM3') #The port to read from (this is a USB port on my laptop)
ser.flushInput() #"This tells the serial port to clear the queue so that data doesn't overlap and create erroneous data points"

root_folder = 'C:/DATA/Sensor_data' #Specify which folder to save the data in

# Get the current time
now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
output_file='{}/{}_light.csv'.format(root_folder, now)

# Create a csv file to store the data in
with open(output_file,"a") as f:
    f.write('Timestamp,Total light (lux),Visible (0-2147483647),Infrared (0-65535)\n') #Add headers to the file

    print("Ready")

    while True:
            ser_bytes = ser.readline() #Read one line from the port
            decoded_bytes = ser_bytes.decode('utf-8') #Convert data for some reason
            decoded_bytes_split = decoded_bytes.strip().split(',') #Strip away the prefix and suffix characters, and split the values using the comma as the separator
            
            if "Stop" in decoded_bytes:
                print("Stopped")
                f.close() #Close the file
                break

            else:
                # Extract the different light values and convert them to floats
                lux_value = float(decoded_bytes_split[0])
                visible_value = float(decoded_bytes_split[1])
                ir_value = float(decoded_bytes_split[2])

                # Get the current time
                now = datetime.now().strftime('%Y-%m-%d_%H:%M:%S.%f')
                
                # Print out the values
                print('{} | Light: {} lux | Visible: {} | IR: {}'.format(now[0:-7],lux_value,visible_value,ir_value))
                #print(f'{now[0:-7]} | Light: {lux_value} lux | Visible: {visible_value} | IR: {ir_value}')
                #print('{:} | Light: {:.10} lux | Visible: {:.10} | IR: {:.10}'.format(now[0:-7],lux_value,visible_value,ir_value))
                
                # Save the values
                f.write('{},{},{},{}\n'.format(now,lux_value,visible_value,ir_value))