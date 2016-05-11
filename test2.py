#!/usr/bin/env python

from bmp183 import bmp183
import time

bmp = bmp183()

print("")
print("TEST 2")

# THIS WORKS:
print("Reading value stored at 0xAA")
AA = bmp.read_word(0xAA)
print("     Value stored at 0xAA : {0}".format(AA))

# THIS *ALSO* WORKS:
print("Writing value 0x2E into address 0xF4")
bmp.write_byte(0xF4, 0x2E)
# Wait
time.sleep(0.045)
print("Reading value stored at 0xF6")
F6 = bmp.read_word(0xF6)
print("     Value stored at 0xF6 : {0}".format(F6))


# THIS *ALSO* WORKS:
print("Writing value 0x34 into address 0xF4")
bmp.write_byte(0xF4, 0x34)
# Wait
time.sleep(0.045)
print("Reading value stored at 0xF6")
F6 = bmp.read_word(0xF6)
print("     Value stored at 0xF6 : {0}".format(F6))
