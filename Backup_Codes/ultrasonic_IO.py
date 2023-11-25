import RPi.GPIO as IO
import time
TRIG=23
ECHO=24
IO.setmode(IO.BCM)

while True:
    print("distance measurement in progress")
    IO.setup(TRIG,IO.OUT)
    IO.setup(ECHO,IO.IN)
    IO.output(TRIG,False)
    print("waiting for sensor to settle")
    time.sleep(0.2)
    IO.output(TRIG,True)
    time.sleep(0.00001)
    IO.output(TRIG,False)
    while IO.input(ECHO)==0:
        pulse_start=time.time()
    while IO.input(ECHO)==1:
        pulse_end=time.time()
    pulse_duration=pulse_end-pulse_start
    distance=pulse_duration*17150
    distance=round(distance,2)
    print("distance:",distance,"cm")
    time.sleep(2)
    
