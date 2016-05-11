#!/usr/bin/env python

import pigpio
import time

pi = pigpio.pi()

if pi.connected:
  print("TEST1: Connected to pigpio daemon.")
  hndl = pi.spi_open(0, 1000000)

  # THIS WORKS:
  (cnt, rxd) = pi.spi_xfer(hndl, [0xAA, 0, 0])
  if cnt > 0:
    AA = (rxd[1] << 8) + rxd[2]
    print("Value stored at 0xAA : {0}".format(AA))

  # THIS DOESN'T WORK:
  print("writing value 0x2E into address 0xF4")
  pi.spi_write(hndl, [0xF4, 0x2E, 0])
  # Wait
  time.sleep(0.045)
  print("Reading value stored at 0xF6")
  (cnt, rxd) = pi.spi_xfer(hndl, [0xF6, 0, 0])
  if cnt > 0:
    F6 = (rxd[1] << 8) + rxd[2]
    print "Value stored at 0xF6 : {0}".format(F6)

  pi.spi_close(hndl)

pi.stop()
