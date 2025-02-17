# Code for AstroPi 2022/2023 - Project Hercules [^1]
[^1]: This project was made for [Mission Space Lab](https://astro-pi.org/mission-space-lab/) 

Our proposal aims create a analog mission to study the human performance on long space travel or long stays in a space station. We also want to study ways to mitigate these problems.

In recent years, some space agencies and private companies are making plans to travel to other planets or building new space stations. Some private companies already started to sell tickets to space or around the moon. This means that space is no longer the domain of professional astronauts, but is share with common people, with little training.

Because these non-professional astronauts will stay several days or even months on space, we want to study if the human performance in a space station or space travel has any implications in mission success or safety problems and if there is, how can we mitigate these problem.

Our team is a blend of students from the Art, Psychology and IT department. We will use the Astro PI's sensors on board of ISS to collect temperature, light, pressure and humidity data. This data will be user to build a full size replica of the Columbus Module on-board of the ISS, by the students from the Art Department. The replica will have environmental controls to simulate ISS environment.

According to the WHO, safe and healthy working environments are fundamental to minimize tension and conflicts at work and improve staff retention, work performance and productivity. At work, we currently realize that the risks to mental health may be related to job content or work schedule and the specific characteristics of the workplace. Therefore, we are planning to develop a number of experiments, inside the replica of the Columbus module, by a group of student volunteers to understand how the confined environments with limited social interactions can negatively impact work performance and mental health. 

The results will be publish in graphical comprehensive detail with public access.

We plan to gather the maximum sensors data. The data will be saved in a .CSV file, processed and organized by type. As a backup, raw data from the sensors, with time stamp will also be saved.


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
