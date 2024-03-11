#!/bin/bash

# flash firmware
esptool.py --chip esp32 --port /dev/ttyUSB0 erase_flash && esptool.py --chip esp32 --port /dev/ttyUSB0 --baud 460800 write_flash -z 0x1000 firmware/ESP32_GENERIC-20240222-v1.22.2.bin
