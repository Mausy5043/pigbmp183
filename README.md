# pigbmp183
**Python class for Raspberry Pi for Bosch BMP183 pressure and temperature sensor with SPI interface using pigpio (no `sudo` required)**

## Description
This repository provides a Python class that can be used to read the temperature and pressure sensors of a BMP183 [(as sold by Adafruit)](https://www.adafruit.com/product/1900) using the SPI interface. The repository leans on [pigpio](https://github.com/joan2937/pigpio), which must be installed and the `pigpiod` daemon must be running (obviously). This way the Python script can be executed by any user **without** the use of `sudo`.

## Requirements
- Raspberry Pi
- Raspbian with kernel version >= 4.4.8 (confirmed working on: 4.4.8+ #880 Fri Apr 22 21:27:42 BST 2016 armv6l GNU/Linux)
- Packages:
  - `git`
  - `python2.7` and/or `python3`
  - `python-numpy`
- Clone and install the GitHub repository `pigpio` from here: https://github.com/joan2937/pigpio
- Clone and install the GitHub repository `pigbmp183` (this one) as described below.

## Installation
```
git clone https://github.com/Mausy5043/pigbmp183.git
cd pigbmp183/
chmod +x update.sh
./update.sh
```

## Execution
Running:
`python pigmeasure.py`

Use `pigmeasure.py` as an example for your own use case.

For continuous measurement run:
`watch -n 12 python pigmeasure.py`

Expected result looks similar to this:
```
Temperature: 26.5 degC
Pressure   : 999.75 hPa
```

## Raspberry Pi I/O
Connect the BMP183 [(as sold by Adafruit)](https://www.adafruit.com/product/1900) as shown below to a **Raspberry Pi 1 B+**. Other hardware versions will work too, but were not tested by me. So, you'll have to figure out the correct pins.
```
BMP pin : RPi pin
========:====================
VIN     : 17  (3v3)
3vo     : N/C
GND     : 25  (GND)
SCLK    : 23  (GPIO11)
SDO     : 21  (GPIO09; MISO)
SDI     : 19  (GPIO10; MOSI)
CS      : 24  (GPIO08; CE0)
```

# Attribution
Part of the code in this repository is based on previous work by Przemo Firszt. See https://github.com/PrzemoF/bmp183
