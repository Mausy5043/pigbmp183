#!/usr/bin/env python

import bmp183

bmp = bmp183()
bmp.measure_pressure()

# print("CALIBRATION DATA BMP183 (version {0}):".format(bmp.VER))
# print("AC1        : {0}".format(bmp.AC1))
# print("AC2        : {0}".format(bmp.AC2))
# print("AC3        : {0}".format(bmp.AC3))
# print("AC4        : {0}".format(bmp.AC4))
# print("AC5        : {0}".format(bmp.AC5))
# print("")
# print("B1         :  {0}".format(bmp.B1))
# print("B2         :  {0}".format(bmp.B2))
# print("")
# print("MB         :  {0}".format(bmp.MB))
# print("MC         :  {0}".format(bmp.MC))
# print("MD         :  {0}".format(bmp.MD))
# print("")
# print("")
# print("ID         :  {0} (must be 85)".format(bmp.ID))
# print("")
# print("")
print("Temperature: {0} degC".format(bmp.temperature))
print("Pressure   : {0} hPa ".format(bmp.pressure / 100.0))

if (bmp.ID != 85):
  print("Communication error!")
  print("Measurement may not be reliable. Chip ID is incorrect.")
