#!/usr/bin/env python

import bmp183
import time

bmp = bmp183()

print("TEST2")

# THIS WORKS:
AA = bmp.spi_transfer(0xAA, 0, 1, 8)
print("Value stored at 0xAA : {0}".format(AA))

# THIS *ALSO* WORKS:
print("writing value 0x2E into address 0xF4")
bmp.write_byte(0xF4, 0x2E)
# Wait
time.sleep(0.045)
# Read uncmpensated temperature
print("Reading value stored at 0xF6")
F6 = bmp.read_word(0xF6)
print("Value stored at 0xF6 : {0}".format(F6))
