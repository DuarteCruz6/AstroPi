## MISSION SPACE LAB REQUIREMENTS
- Needs to use the LED matrix
- Needs to use at least one sensor
- Can't record videos and can't also take photos
- Can't communicate with the Earth
- The program needs to close after 3 hours
- Can only use the ISS's libraries
- Needs to be in a ZIP File

## HARDWARE
- Raspberry Pi 4 4GB
- Sense HAT
- Passive Infrared (PIR) Sensor
- Tall header pins
- 3x F-F jumper wires (to connect the PIR Sensor to the Raspberry Pi)
- 3D-printed flight case
- Power Supply unit
- 16GB microSD card
- HDMI Cable

  #### NOTES:
  The Sense HAT contains many different sensors such as:
    - Gyroscope
    - Accelerometer
    - Magnetometer
    - Temperature
    - Barometric Pressure
    - Humidity
    - Colour and brightness
    It also contains a 8x8 RGB LED matrix and a five-button joystick

## SOFTWARE
- Special version of the Raspberry Pi Desktop OS (Bullseye 32 bit) that contains the same programs and libraries as the Astro Pis aboard the ISS (International Space Station)
- Thonny IDE

## LIBRARIES
- SenseHat (from [sense_hat](https://pythonhosted.org/sense-hat/))
- Path (from [pathlib](https://docs.python.org/3/library/pathlib.html))
- MotionSensor, CPUTemperature (from [gpiozero](https://gpiozero.readthedocs.io/en/stable/))
- [time](https://docs.python.org/3/library/time.html)
- datetime, timedelta (from [datetime](https://docs.python.org/3/library/datetime.html))
- ISS (from [orbit](https://orbit-ml.readthedocs.io/en/latest/))
- load (from [skyfield.api](https://rhodesmill.org/skyfield/))

## EVALUATION CRITERIA
- Does it have scientific use?
- Can you understand the code?
- Is the code doccumented?
- Is the code well structured?
- Is it copied from other sources?
- Is it easily reproduced?
- Is the data usable/interesting?

### NOTES:
- Make sure to download [de4221.bsp](https://github.com/DuarteCruz6/AstroPi/blob/main/AstroPi%20-%20Code%20and%20Data/de421.bsp)
- Make sure to save all [files](https://github.com/DuarteCruz6/AstroPi/tree/main/AstroPi%20-%20Code%20and%20Data) in the same location (create a paste with all, for instance)
