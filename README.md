## ESP32 MicroPython Tutorial

## Getting Started – Installation
Before we start our Micropython tutorial, we need to install some software as prerequisite of this tutorial.

## Prerequisite
* Python 37x or latest - https://www.python.org/downloads/
* Arduino IDE - https://www.arduino.cc/en/software
* Thonny IDE - https://thonny.org/
* MicroPython Firmware - https://thonny.org/

## Installing Micropython Firmware

The MicroPython firmware are available for many microcontroller-ESP based built. You will see several firmware on the list.
The correct installer that you have to download the installer as shown below:

![firmware](https://user-images.githubusercontent.com/60383798/109600424-0f5ca380-7b58-11eb-9ab5-652e7478e719.PNG)
	
When downloading the file, you will need to rename the file. Since the filename is long and it will be hard for you to type the long name. Rename it simpler as ESP32.

## Installing esptool.py
1. On your search windows, type in cmd and click the Command Prompt Application.
2. Type the following command and pressed Enter.

	`<pip install esptool>` 

![pipinstall (2)](https://user-images.githubusercontent.com/60383798/109600864-db35b280-7b58-11eb-98c9-157813b2f5dc.png)

You will see some file are being downloaded to complete the esptool installation. To check the esptool is successfully downloaded, you can type in **esptool.py** and run. Then, the cmd terminal will run your command. Otherwise, it will be error.

## Clean the Firmware

You need to clean the firmware by erasing everything unrelated to make the ESP32 firmware in a clean state. For this action, you must connect your Circuit Plus Board to your computer.

Go to your cmd and type this following command:

`<esptool.py --chip esp32 erase_flash>` 

	

