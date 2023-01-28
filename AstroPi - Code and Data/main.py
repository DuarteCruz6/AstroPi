#Imports the libraries needed
from sense_hat import SenseHat
from pathlib import Path
from gpiozero import MotionSensor, CPUTemperature
import time
from datetime import datetime, timedelta
from orbit import ISS
from skyfield.api import load

#Stores the current time
start_time = datetime.now()
now_time = datetime.now()

#Starts some sensors (Motion Sensor, Sense HAT)
pir = MotionSensor(4)
sense = SenseHat()
sense.clear()
cpu = CPUTemperature()

#Creates an .csv file on the location of main.py
base_folder = Path(__file__).parent.resolve()
data_file = base_folder / "data.csv"

#Some variables
i = 0                                                                                                             #Variable that lets us check what's being shown in the LED Screen
dic = ["TIME","SUNLIGHT ON THE ISS","MOTION","PRESSURE", "TEMPERATURE FROM HUMIDITY SENSOR","TEMPERATURE FROM PRESSURE SENSOR","CPU TEMPERATURE","HUMIDITY","LIGHT", "MOVEMENT X-ASSIS", "MOVEMENT Y-ASSIS", "MOVEMENT Z-ASSIS", "ACCELERATION X-ASSIS", "ACCELERATION Y-ASSIS", "ACCELERATION Z-ASSIS"]     #Which data will be shown on the LED screen
x = timedelta(hours = 2, minutes = 59, seconds = 60)                                                              #Time of the loop
loopTime = {0:15, 1:6, 2:6, 3:8, 4:18, 5:19, 6:13, 7:7, 8:11, 9:12, 10:12, 11:12, 12:13, 13:13, 14:13}            #How much it takes to each data + value to show on the LED matrix
ephemeris = load("de421.bsp")                                                                                     #Table of the position of the Earth and the Sun

#Writes an Header on the .csv file
with open (data_file, "w", buffering = 1) as f:
   f.write("TIME, SUNLIGHT ON THE ISS, MOTION (YES/NO), PRESSURE, TEMPERATURE FROM HUMIDITY SENSOR,TEMPERATURE FROM PRESSURE SENSOR,CPU TEMPERATURE, HUMIDITY,LIGHT, MOVEMENT X-ASSIS, MOVEMENT Y-ASSIS, MOVEMENT Z-ASSIS, ACCELERATION X-ASSIS, ACCELERATION Y-ASSIS, ACCELERATION Z-ASSIS")
   f.write("\n")

#Loop that runs for 3 hours      
while now_time - start_time < x :                          
    if pir.value == 1:                                   #Motion 
        m = "YES"
    elif pir.value == 0:
        m = "NO"
    p = sense.get_pressure()                             #Pressure
    t_h = sense.get_temperature()                        #Temperature in the humidity sensor
    t_p = sense.get_temperature_from_pressure()          #Temperature in the pressure sensor
    t_cpu = cpu.temperature                              #CPU Temperature
    h = sense.get_humidity()                             #Humidity
    sense.color.gain = 60                                #Sensitivity on the light sensor
    sense.color.integration_cycles = 1                   #Interval between measurameants
    l = str((sense.colour.colour)).replace(",",".")      #Light (RGBC - Red, Green, Blue, Clear (Brightness))
    orien = sense.get_orientation()                      #Movement on x,y and z assis
    x = orien["pitch"]
    y = orien["roll"]
    z = orien["yaw"]
    a = sense.get_accelerometer_raw()                    #G forces on x,y and z assis
    a_x = a["x"]
    a_y = a["y"]
    a_z = a["z"]
    time = datetime.now()                               #Time
    timescale = load.timescale()
    t = timescale.now()
    sunlight = ISS.at(t).is_sunlit(ephemeris)          #If ISS is sunlight or not
    if sunlight == "True":
        sunlight = "YES"
    else:
        sunlight = "NO"


    with open (data_file, "a", buffering = 1) as f:     #Writing the data on the .csv file
        f.write(f"{time},{sunlight}, {m}, {p}, {t_h}, {t_p}, {t_cpu}, {h}, {l}, {x}, {y}, {z}, {a_x}, {a_y}, {a_z}")
        f.write("\n")

    values = {"0": time,"1":sunlight, "2":m, "3":p, "4":t_h, "5":t_p, "6":t_cpu, "7":h, "8":l, "9":x, "10":y, "11":z, "12":a_x, "13":a_y, "14":a_z} #Values of each data 
    value = values[str(int(i))]                        #Corresponds the value to the data being shown on the LED matrix

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

    x = timedelta(hours = 2, minutes = 59, seconds = 60- loopTime[i])              #Changes the time of the loop
    sense.show_message(dic[int(i)] + " " + str(value) ,scroll_speed = 0.08)        #Shows the data on the LED screen
    
    i+= 1                                                                          #Changes the data being showed on the LED screen
    if i == 15:
            i = 0
    now_time = datetime.now()                                                      #Changes the value of now_time to the current time

