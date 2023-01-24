#Imports the libraries needed
from sense_hat import SenseHat
from pathlib import Path
import pandas as pd
from gpiozero import MotionSensor
import time
from datetime import datetime, timedelta


#Stores the current time
start_time = datetime.now()
now_time = datetime.now()

#Starts some sensors (Motion Sensor, Sense HAT)
pir = MotionSensor(4)
sense = SenseHat()
sense.clear()

#Creates an .csv file on the location of main.py
base_folder = Path(__file__).parent.resolve()
data_file = base_folder / "data.csv"

#Variable that lets us check what's beijng shown in the LED Screen
i = 0
dic = ["TIME","MOTION","PRESSURE", "TEMPERATURE FROM HUMIDITY SENSOR","TEMPERATURE FROM PRESSURE SENSOR","HUMIDITY","LIGHT", "MOVIMENT X-ASSIS", "MOVIMENT Y-ASSIS", "MOVIMENT Z-ASSIS", "ACCELERATION X-ASSIS", "ACCELERATION Y-ASSIS", "ACCELERATION Z-ASSIS"]

#Writes an Header on the .csv file
with open (data_file, "w", buffering = 1) as f:
   f.write("TIME, MOTION (YES/NO), PRESSURE, TEMPERATURE FROM HUMIDITY SENSOR,TEMPERATURE FROM PRESSURE SENSOR,HUMIDITY,LIGHT, MOVIMENT X-ASSIS, MOVIMENT Y-ASSIS, MOVIMENT Z-ASSIS, ACCELERATION X-ASSIS, ACCELERATION Y-ASSIS, ACCELERATION Z-ASSIS")
   f.write("\n")

#Loop that runs for 3 hours      
while now_time - start_time < timedelta(hours = 2, minutes = 59, seconds = 42) : 
    time = datetime.now()
    def show():                                        #Function that changes the data on the LED screen if the astronaut presses the joystick
        global i
        i+= 0.5
        if i == 13:
            i = 0

    if pir.value == 1:                                   #Motion
        m = "YES"
    elif pir.value == 0:
        m = "NO"
    p = sense.get_pressure()                             #Pressure
    t_h = sense.get_temperature()                        #Temperature in the humidity sensor
    t_p = sense.get_temperature_from_pressure()          #Temperature in the pressure sensor
    h = sense.get_humidity()                             #Humidity
    sense.color.gain = 60                                #Light
    sense.color.integration_cycles = 64                  #Light
    l = str((sense.colour.colour)).replace(",",".")
    orien = sense.get_orientation()                      #Movement on x,y and z assis
    x = orien["pitch"]
    y = orien["roll"]
    z = orien["yaw"]
    a = sense.get_accelerometer_raw()                    #G forces on x,y and z assis
    a_x = a["x"]
    a_y = a["y"]
    a_z = a["z"]
    time = datetime.now()                                #Time
                                           
    with open (data_file, "a", buffering = 1) as f:     #Writing the data on the .csv file
        
        f.write(f"{time},{m}, {p}, {t_h}, {t_p}, {h}, {l}, {x}, {y}, {z}, {a_x}, {a_y}, {a_z}")
        f.write("\n")
    
    sense.stick.direction_any = show                    #If the astronaut moves the joystick, he wants to check some value on the LED's
    values = {"0": time, "1":m, "2":p, "3":t_h, "4":t_p,"5":h,"6":l, "7":x,"8":y,"9":z,"10":a_x,"11":a_y,"12":a_z}
    value = values[str(int(i))]                        #Corresponds the data to the joystick
    
    if type(value) == float:
        value = round(value,1)
   
    if round(a_x,0) == -1:                             #Gets the orientation of the Astro Pi so that the text is always displayed correctly
        sense.set_rotation(90)
    elif round(a_y,0) == 1:
        sense.set_rotation(0)
    elif round(a_y,0) == -1:
        sense.set_rotation(180)
    else:
        sense.set_rotation(270)
    
    sense.show_message(dic[int(i)] + " " + str(value) ,scroll_speed = 0.08)        #Shows the data on the LED screen

    now_time = datetime.now()
    
