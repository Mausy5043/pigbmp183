#!/usr/bin/env python

import pigpio
import time

pi = pigpio.pi()

if pi.connected:
  print "Connected to pigpio daemon."
  hndl = pi.spi_open(0, 1000000)
  
  ### THIS WORKS:
  (cnt, rxd) = pi.spi_xfer(hndl, [0xAA, 0, 0])
  if cnt > 0:
    AA = (rxd[1] << 8) + rxd[2]
    print AA
   
  ## THIS DOESN'T WORK:
  pi.spi_write(hndl, [0xF4, 0x2E, 0])
  time.sleep(0.045)

  (cnt, rxd) = pi.spi_xfer(hndl, [0xF6,0,0])
  if cnt > 0:
    for i in rx_data:
      print i

  time.sleep(0.5)
  pi.spi_close(hndl)

pi.stop()
