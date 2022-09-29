# Author: Javier Izquierdo and Toni L. Mari
# Date: 29/09/2022
# Goal: This program tries to emulate an analog output for a led 

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.OUT)

pwm = GPIO.PWM(11,100)

pwm.start(50)

pwm.ChangeDutyCycle(100)

pwm.ChangeFrequency(1000)

input("Ejecutando hasta pulsar una tecla...")

pwm.stop()

GPIO.cleanup()
