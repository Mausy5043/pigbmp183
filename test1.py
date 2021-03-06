#!/usr/bin/env python

import pigpio
import time

"""
This Python script tests the pigpio low-level calls
"""
pi = pigpio.pi()

if pi.connected:
  print("TEST 1")
  hndl = pi.spi_open(0, 34000)

  # THIS WORKS:
  print("Reading value stored at 0xAA")
  (cnt, rxd) = pi.spi_xfer(hndl, [0xAA, 0, 0])
  if cnt > 0:
    AA = (rxd[1] << 8) + rxd[2]
    print("     Value stored at 0xAA : {0}".format(AA))

  # THIS DOESN'T WORK:
  print("Writing value 0x2E into address 0xF4")
  pi.spi_write(hndl, [0x74, 0x2E, 0])
  # Wait
  time.sleep(0.045)
  print("Reading value stored at 0xF6")
  (cnt, rxd) = pi.spi_xfer(hndl, [0xF6, 0, 0])
  if cnt > 0:
    F6 = (rxd[1] << 8) + rxd[2]
    print("     Value stored at 0xF6 : {0}".format(F6))

  # THIS DOESN'T WORK:
  print("Writing value 0x34 into address 0xF4")
  pi.spi_write(hndl, [0x74, 0x34, 0])
  # Wait
  time.sleep(0.045)
  print("Reading value stored at 0xF6")
  (cnt, rxd) = pi.spi_xfer(hndl, [0xF6, 0, 0])
  if cnt > 0:
    F6 = (rxd[1] << 8) + rxd[2]
    print("     Value stored at 0xF6 : {0}".format(F6))

  pi.spi_close(hndl)

pi.stop()
