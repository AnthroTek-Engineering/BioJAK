BioJAK
======
AnthroTek BioJAK Code.

Arduino code does not include necessary libraries.

All required dependancies and full system are on the RPi Image. 

Contact john.hogg@anthrotek.ca for Trial Image. Or compile your own system with provided code.

Plug and Play Instructions:

1. Copy RPi image (.dmg) to 8gb micro SD card

  1.1 If using windows convert file to .iso and follow these instructions
  http://www.raspberrypi.org/documentation/installation/installing-images/windows.md
  
  1.2 If using mac follow these instructions       
  http://www.raspberrypi.org/documentation/installation/installing-images/mac.md
 
  1.3 If using Linux follow these Instructions
  http://www.raspberrypi.org/documentation/installation/installing-images/linux.md

2. Boot Raspberry Pi connected to display keyboard and mouse

3. Configure WIFI to phones LTE and home WIFI networks
   http://www.raspberrypi.org/documentation/configuration/wireless/README.md

4. Enter terminal or CLI Emulator and enter 'sudo nano /etc/rc.local'

5. Remove '#' before the /Home/pi/BioJAK/proto_v1.1/init.d
  5.1 ctrl-x to exit
  5.2 enter y, then enter to save

6. Unplug raspberry pi and all peripherals

7. Hook up, ANT+ USB, Arduino, Wifi Module, and GPS to the USB ports

8. Plug in headphones/embedded speakers

9. Complile and run webserver code on desired platform (Django recomended)
 9.1 Note that RTMP (Video Stream) may require configuration to your own settings
 9.2 Contact AnthroTek support for additional help

11. Power up Pi and wait for voice prompts 

12. Enjoy project, branch and edit as desired
