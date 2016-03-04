#!/usr/bin/env python
# to use with Pi Traffic Light

import RPi.GPIO as GPIO
import psutil

GREEN = 26
YELLOW = 13
RED = 19

# Pin Setup:
GPIO.setmode(GPIO.BCM)   # Broadcom pin-numbering scheme.
GPIO.setwarnings(False)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(YELLOW, GPIO.OUT)
GPIO.setup(RED, GPIO.OUT)

try:
   while (1):
      cpu_pc = psutil.cpu_percent(interval=2)
      print 'CPU: %d%%' % (cpu_pc)
      if cpu_pc <= 50:
         GPIO.output(RED, False)
         GPIO.output(YELLOW, False)
         GPIO.output(GREEN, True)
      if 50 < cpu_pc < 90:
         GPIO.output(GREEN, False)
         GPIO.output(RED, False)
         GPIO.output(YELLOW, True)
      if cpu_pc >=90 :
         GPIO.output(GREEN, False)
         GPIO.output(YELLOW, False)
         GPIO.output(RED, True)
except KeyboardInterrupt:
    print "Good bye"
    GPIO.output(GREEN, False)
    GPIO.output(YELLOW, False)
    GPIO.output(RED, False)

