import RPi.GPIO as io
import time

# Currently able to reach about 500-700 jumps

time.sleep(1)

io.setmode(io.BCM)
solenoid = 25
io.setup(solenoid, io.OUT)

io.output(solenoid, 1)
time.sleep(0.05)
io.output(solenoid, 0)
time.sleep(1)

timing = 0.60
tricky = False
try:
    for jump in range(1, 1000):
        print jump
        io.output(solenoid, 1)
        time.sleep(0.05)
        io.output(solenoid, 0)
   
        if jump == 20:
            timing = 0.489
        elif jump == 49:
            timing = 0.415
        elif jump == 99:
            timing = 0.382
        elif jump == 199:
            timing = 0.298
	    tricky = True
        elif jump == 299:
            timing = 0.350

        time.sleep(timing)

        if jump in range(201, 298):
	    if tricky == True:
                time.sleep(0.07)
		tricky = False
	    else:
		tricky = True
except:
    io.cleanup()
