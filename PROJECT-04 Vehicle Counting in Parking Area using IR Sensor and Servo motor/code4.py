import RPi.GPIO as IO   # calling for header file for GPIO’s of PI 
import time             # calling for time to provide delays in program 
IO.setwarnings(False)   # do not show any warnings 
IO.setmode (IO.BCM)  # programming the GPIO by BCM pin numbers.(like PIN29 as‘GPIO5’) 
IO.setup(14,IO.IN)      #GPIO 14 -> IR sensor as input 
IO.setup(25,IO.OUT)     # initialize GPIO19 as an output 
Count=0 
p = IO.PWM(25,50)       # GPIO19 as PWM output, with 50Hz frequency 
p.start(7.5)            # generate PWM signal with 7.5% duty cycle 
while 1:                # execute loop forever                                     
   if(IO.input(14)==False):                              #object is near 
         p.ChangeDutyCycle(7.5)                          #servo position to 90º 
         time.sleep(3)                                   # sleep for 3 second 
         count=count+1 
         print(‘count’) 
         print(‘Vehicle present in the parking area’) 
         p.ChangeDutyCycle(2.5)                          #servo position to 0º
         time.sleep(1)                                   # sleep for 1 second 
