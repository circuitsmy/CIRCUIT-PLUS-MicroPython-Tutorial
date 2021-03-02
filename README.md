# Circuit Plus - MicroPython Tutorial

![circuit plus](https://user-images.githubusercontent.com/60383798/109620336-b8b19280-7b74-11eb-85ed-6b7aab0c17b6.png)


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

## Clean ESP32 Firmware

You need to clean the firmware by erasing everything unrelated to make the ESP32 firmware in a clean state. For this action, you must connect your Circuit Plus Board to your computer.

Go to your cmd and type this following command:
	
	`<esptool.py --chip esp32 erase_flash>` 

![erase flash (2)](https://user-images.githubusercontent.com/60383798/109601652-3caa5100-7b5a-11eb-8f3c-c038dc2e38d4.jpg)
	
You will see the command will connect to the board and access the chip and completely erase the flash. 

## ESP32 Serial Port Configuration

Serial Port number have been assigned to the Circuit Plus Board when you connect the board to the computer. To check the assigned serial number, you have to go to your computer Device Manager.

1. Go to search Window and type Device Manager and click the Device Manager Application.
2. Click down the Ports and see the list of ports connected to your computer. By referring to the list, you should be able to see the serial port number for the Circuit Plus Board.

![port (2)](https://user-images.githubusercontent.com/60383798/109602672-83e51180-7b5b-11eb-86d0-27728afe80f8.png)

If you unsure which one is the port that your board connected to, try connect and disconnect the board from your computer. You will see it on the device manager.

3. Then, Navigate your Micropython firmware address. Since I downloaded the firmware and stored in the Download folder then I shall use this location link.

You can get it by right click the Download Folder. Download Properties > Location 

![dwld (2)](https://user-images.githubusercontent.com/60383798/109602731-a24b0d00-7b5b-11eb-841f-236e7e7d3b97.png)

	`<C:\Users\PC1\Downloads>` 

Copy the location address and paste it to your command prompt.

![cmd (2)](https://user-images.githubusercontent.com/60383798/109602835-d6263280-7b5b-11eb-8f9c-f0e81b338a41.png)

4. Next, type this following command. 

	`<esptool.py --chip esp32 --port [serial_port] write_flash -z 0x1000 [firmwareName.bin]>` 

In the command, replace the serial port number with the serial number that you get before. Also, change the firmware name to the name you have save before and run the command. 

![scmd (2)](https://user-images.githubusercontent.com/60383798/109602921-01a91d00-7b5c-11eb-917b-b8e2158fbbdd.png)

The result should be like this:

![whatever](https://user-images.githubusercontent.com/60383798/109603069-459c2200-7b5c-11eb-890c-25fcadde8cf6.jpg)

## Configure MicroPython with Thonny IDE

1. Download Thonny IDE and complete the installation.

![thonny](https://user-images.githubusercontent.com/60383798/109602447-0f11d780-7b5b-11eb-865b-8eb7c758483c.png)

2. Open your Thonny Ide and setup the Intrepreter and the port options and save.

	*Go to Tools > Option > Intrepreter > MicroPython (Generic)*
	
3. Setup the port

	*Port > [Current Circuit Plus Port]*

![option (4)](https://user-images.githubusercontent.com/60383798/109603447-c0fdd380-7b5c-11eb-9cf1-e878319ba8e6.png)

## Circuit Plus :  ESP32 – CONFIGURATION

For your information, the Circuits Plus board has embedded ESP32 chips which are called System on Chip (SoC) that enable the board to connect to the Wi-Fi and Bluetooth. So, before we start using the ESP32 mode, we need to install the ESP32 Package Board.

  ![circuit plus](https://user-images.githubusercontent.com/60383798/109613628-61a7bf80-7b6c-11eb-9412-456e704d92fe.png)


1. Install the ESP32 library.  *Go to File-> Preferences*

![preference](https://user-images.githubusercontent.com/60383798/109612718-1e991c80-7b6b-11eb-9595-ad0fad73a013.png)

2. Enter https://dl.espressif.com/dl/package_esp32_index.json into the “Additional Board Manager URLs” field as shown in the figure below. Then, click the “OK” button:

![setup](https://user-images.githubusercontent.com/60383798/109612768-31abec80-7b6b-11eb-96c9-58678d34d3e0.png)

3. Install the ESP32 library. *Go to Tools -> Manage Library*

4. Arduino’s Library Manager will appear, then type “ ESP32 ” in the provided search space.

![lib](https://user-images.githubusercontent.com/60383798/109612871-51431500-7b6b-11eb-941b-b5241723a265.png)

5. Install the ESP32 library

6. Check the installation, open the Boards Manager. *Go to Tools -> Board -> Boards Manager ->  ESP32 Arduino -> ESP32 Dev Module* 

![board](https://user-images.githubusercontent.com/60383798/109612902-6029c780-7b6b-11eb-91d5-e755e3943628.png)

Installation is successful if you manage to found the  board.

7. Connect the Circuits IO board to your PC. Make sure that you have set switch mode to ESP32 first.

8. Next we have to configure the port for the ESP32. *Go to Tools -> Port*

9. Select the Port (if you don’t see the COM Port in your Arduino IDE, you need to install the CH34X Driver.

![ports](https://user-images.githubusercontent.com/60383798/109613007-8bacb200-7b6b-11eb-9458-298ca83a23d7.png)

Install CH34X from here : 

10. If you can see the available port then you have finished the ESP32 configuration. Next part we will test the connection of ESP32 with Wi-Fi.

![com](https://user-images.githubusercontent.com/60383798/109613113-af6ff800-7b6b-11eb-9674-b0f4bedda0cf.png)











