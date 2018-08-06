# playing-with-micropython

I purchased [this $8](https://www.amazon.com/gp/product/B010O1G1ES/ref=oh_aui_detailpage_o02_s00?ie=UTF8&psc=1) ESP8266 development board from Amazon and loaded [Micropython](http://docs.micropython.org/en/latest/esp8266/index.html) onto it.

Purpose
=======

I'll use this repo to document as I learn...

* [How to blink a LED](0_blink_led.py)

Setup
=====

* install some drivers if using on a MacOs machine

        http://www.ftdichip.com/Drivers/VCP.htm
        https://www.silabs.com/products/development-tools/software/usb-to-uart-bridge-vcp-drivers

* Install the [serial bootloader utility](https://github.com/espressif/esptool/)

        pip install esptool

* [Download](http://micropython.org/download/#esp8266) the latest MicroPython ESP8266 firmware file.

* Put the ESP8266 into its firmware flashing mode. Basically get it ready to erase everything.

    * Hold the GPIO0 button down (or connect the line to ground) and while still holding GPIO0 to ground press and release the RESET button (or connect and release the line from ground), then release GPIO0.

* See if the proper serial port - `/dev/cu.SLAB_USBtoUART` - is being picked up

        ls /dev/cu*

* Flash the board

        esptool.py --port /dev/cu.SLAB_USBtoUART erase_flash

    * Desired output is:

            esptool.py v2.5.0
            Serial port /dev/cu.SLAB_USBtoUART
            Connecting........_
            Detecting chip type... ESP8266
            Chip is ESP8266EX
            Features: WiFi
            MAC: 38:2b:78:03:7e:29
            Uploading stub...
            Running stub...
            Stub running...
            Erasing flash (this may take a while)...
            Chip erase completed successfully in 7.6s
            Hard resetting via RTS pin...

* Put the ESP8266 back into firmware flashing mode and run the following command to load the downloaded firmware file

        esptool.py --port /dev/cu.SLAB_USBtoUART --baud 460800 write_flash --flash_size=detect 0 ~/Desktop/esp8266-20180511-v1.9.4.bin

    * Desired output is:

            esptool.py v2.5.0
            Serial port /dev/cu.SLAB_USBtoUART
            Connecting....
            Detecting chip type... ESP8266
            Chip is ESP8266EX
            Features: WiFi
            MAC: 38:2b:78:03:7e:29
            Uploading stub...
            Running stub...
            Stub running...
            Changing baud rate to 460800
            Changed.
            Configuring flash size...
            Auto-detected Flash size: 4MB
            Flash params set to 0x0040
            Compressed 604872 bytes to 394893...
            Wrote 604872 bytes (394893 compressed) at 0x00000000 in 9.2 seconds (effective 525.2 kbit/s)...
            Hash of data verified.

            Leaving...
            Hard resetting via RTS pin...

* On Linux or Mac OSX the screen command can be used to connect to the serial port.  Run the following command to connect at 115200 baud:

        screen /dev/cu.SLAB_USBtoUART 115200

* Setup WebREPL access

        import webrepl_setup

    * Follow the on-screen instructions and prompts. To make any changes active, you will need to reboot your device.
