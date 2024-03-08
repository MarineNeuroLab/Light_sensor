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

# Specify the time (in 24hr clock format) when a new file should be made (e.g. every day at midnight would be 0)
newfile_hour = 7
newfile_min = 0

# Speciy which port to read the data from (i.e. the USB port the QtPy is connected to)
port = 'COM10'
####################################################################################

import serial
from datetime import datetime
import time
import matplotlib.pyplot as plt
import numpy as np

ser = serial.Serial(port) #Specify which port to read from 

# Main code:
while True: #While True, run the following code to record and save temperature values in  the output file specified
    # Get the current time
    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    
    # Create a cvs file with a name based on the current time in the root folder specified 
    output_file='{}/{}_light.csv'.format(root_folder, now)

    #Create empty lists to save measurements in (for plotting later)
    timevec=[]
    luxvec=[]

    with open(output_file,"a") as f: #Open the file
        f.write('Timestamp,Total light (lux),Visible (0-2147483647),Infrared (0-65535)\n') #Add headers to the file. Numbers in brackets are the ranges of possible values
    
    timestart = datetime.now().strftime('%Y-%m-%d_%H:%M:%S.%f') #Save the current time as a string, just before measurements start being saved
    timenow = datetime.now() #Save the current time, which will refresh regularly through the script

    ser.flushInput() #This clears the serial buffer so everything is ready to go

    # While the current time is NOT the set newfile_hour/min time, continuously save data to the file
    while timenow.hour != newfile_hour or timenow.minute != newfile_min:
        write_to_file = True

        try: #This section can be error prone, hence why it's in a 'try' clause
            ser_bytes = ser.readline() #Read one line from the port
        
            if not ser_bytes: #If nothing arrived via serial, then do not write to file
                    write_to_file = False
            else: #Otherwise continue
                decoded_bytes = ser_bytes.decode('utf-8') #Convert the read data so it's legible
                decoded_bytes_split = decoded_bytes.strip().split(',') #Strip away the prefix and suffix characters, and split the values using the comma as the separator
            
            # Attempt to extract the temperature value and convert it to a float (if that can't be done then this indicates the received value corrupted and cannot be saved properly)
            lux_value = float(decoded_bytes_split[0])
            visible_value = float(decoded_bytes_split[1])
            ir_value = float(decoded_bytes_split[2])

        except: #If there is an error (i.e. values above cannot be converted to float), make it a NaN instead
            lux_value = np.nan
            visible_value = np.nan
            ir_value = np.nan
            now = datetime.now().strftime('%Y-%m-%d_%H:%M:%S.%f') #Get the current time (as a string)
            print('{} Error occured, measurements will be saved as NaNs'.format(now[0:-7]))

        if write_to_file: #If this value is true, then write to file 
            now = datetime.now().strftime('%Y-%m-%d_%H:%M:%S.%f') # Get the current time (as a string)
        
            # Append the values to the existing csv file and to the lists
            with open(output_file,"a") as f:
                f.write('{},{},{},{}\n'.format(now[0:-4],lux_value,visible_value,ir_value))
            
            timevec.append(now[0:-4])
            luxvec.append(lux_value) 

            # Print out the values in the terminal
            print('{} | Light: {} lux | Visible: {} | IR: {}'.format(now[0:-7],lux_value,visible_value,ir_value))
          
            # Get the current time so the while loop can be evaluated again (is it appropriate to stay in the loop or exit it?)
            timenow = datetime.now()
        
    # Once the while loop has been exited, print a status update in the terminal
    timeend = datetime.now().strftime('%Y-%m-%d_%H-%M-%S.%f') # Get the current time (as a string)
    print('Light measurements started saving just after {}, finished saving at {}'.format(timestart[0:-7],timeend[0:-7]))
    
    # Create and save a plot of the values collected
    figure = plt.figure() #Create a plot
    ax = figure.add_subplot(111)
    ax.plot(timevec, luxvec,'-')   

    plt.xticks([0, np.floor(len(timevec)/2),len(timevec)-1])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    plt.xlabel("Time")
    plt.ylabel("Total light (lux)")
    plt.savefig('{}/{}_light.png'.format(root_folder,timeend[0:-7]),dpi=300)
    print('Plot of measurements has been saved')
    
    # Include a break to avoid making unnecessary new files when the specified delay is shorter than a minute
    print('Recording will continue in about 1 minute \n \n')
    time.sleep(61)