# pigbmp183
**Python class for Raspberry Pi for Bosch BMP183 pressure and temperature sensor with SPI interface using pigpio (no `sudo` required)**

## Description
This repository provides a Python class that can be used to read the temperature and pressure of a BMP183 using the SPI interface. The repository leans on [pigpio](https://github.com/joan2937/pigpio), which must be installed and running (obviously). This way the Python script can be exectued by any user **without** the use of `sudo`.

## Installation

## Execution
Running:
`python measure.py`

For continuous measurement run:
`watch -n 5 python measure.py`

Expected result looks similar to this:
```
Temperature:  18.9 deg C
Pressure:  1013.39  hPa
```

## Raspberry Pi I/O
Connecting the sensor as follows:
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
