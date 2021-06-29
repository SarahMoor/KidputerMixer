import RPi.GPIO as gpio
import time

'''
This script should control 4 motors in the forward direction.

The GPIO pins for the motors are as follows:
motor 1     17  22
motor 2     23  24
motor 3     5   6
motor 4     13  29


'''
    
def init():
	gpio.setmode(gpio.BCM)
	gpio.setup(17, gpio.OUT)
	gpio.setup(22, gpio.OUT)
	gpio.setup(23, gpio.OUT)
	gpio.setup(24, gpio.OUT)
	gpio.setup(5, gpio.OUT)
	gpio.setup(6, gpio.OUT)
	gpio.setup(13, gpio.OUT)
	gpio.setup(29, gpio.OUT)
	return 0
	
def motor1(sec_1):
    gpio.output(17, True)
    gpio.output(22, False)
    print("Motor 1 is on for {} seconds".format(sec_1))
    time.sleep(sec_1)
    
    gpio.output(17, False)
    gpio.output(22, False)
    
    time.sleep(0.1) #Sleep to let everything come to a rest


def motor2(sec_2):
    gpio.output(23, True)
    gpio.output(24, False)
    print("Motor 2 is on for {} seconds".format(sec_2))
    time.sleep(sec_2)
    
    gpio.output(23, False)
    gpio.output(24, False)
    
    time.sleep(0.1) #Sleep to let everything come to a rest

def motor3(sec_3):
    gpio.output(5, True)
    gpio.output(6, False)
    print("Motor 3 is on for {} seconds".format(sec_3))
    time.sleep(sec_3)
    
    gpio.output(5, False)
    gpio.output(6, False)
    
    time.sleep(0.1) #Sleep to let everything come to a rest

def motor4(sec_4):
    gpio.output(13, True)
    gpio.output(29, False)
    print("Motor 4 is on for {} seconds".format(sec_4))
    time.sleep(sec_4)
    
    gpio.output(13, False)
    gpio.output(29, False)
    
    time.sleep(0.1) #Sleep to let everything come to a rest



if __name__ == "__main__":
    print("START")
    init() #Initialize GPIO pins
    
    
    sec_1 = 5 #Number of seconds to power motor 1
    sec_2 = 30 #Number of seconds to power motor 2
    sec_3 = 0 #Number of seconds to power motor 3
    sec_4 = 2 #Number of seconds to power motor 4
    

    motor1(sec_1) #Power motor 1
    motor2(sec_2) #Power motor 2
    motor3(sec_3) #Power motor 3
    motor4(sec_4) #Power motor 4

    time.sleep(0.1) #Sleep for a tenth of a second to let everything chill tfo
    
    gpio.cleanup() #Let python sort out those GPIO pin states
    
    print("DONE")
