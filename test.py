#!/usr/bin/env python

import pigpio

pi = pigpio.pi()

if pi.connected:
   print("Connected to pigpio daemon.")
   hndl = pi.spi_open(0, 32000)
   (count, rx_data) = pi.spi_xfer(hndl, [0xAA, 0, 0])
   # pi.spi_write(hndl, [0xAA])
   # time.sleep(0.1)
   # (count, rx_data) = pi.spi_read(hndl, 3)
   pi.spi_close(hndl)
   if count > 0:
     AA = (rx_data[1] << 8) + rx_data[2]
     print AA

pi.stop()
