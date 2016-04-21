import RPi.GPIO as io
import time

# Currently able to reach about 500-700 jumps

time.sleep(1)

# setup GPIO
io.setmode(io.BCM)
solenoid = 25
io.setup(solenoid, io.OUT)

# start the game
io.output(solenoid, 1)
time.sleep(0.05)
io.output(solenoid, 0)
time.sleep(1)

# initial jump interval of .60 seconds
timing = 0.60
# Tricky variable is for every other jump in the "double tap" jumps of 200-300
tricky = False

try:
    for jump in range(1, 1000):
        print jump
        # push the solenoid 
        io.output(solenoid, 1)
        time.sleep(0.05)
        # pull the solenoid
        io.output(solenoid, 0)

        # adjust the timing for the current jump
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

        # For the tricky "double tap" tricky jumps between 200-300
        if jump in range(201, 298):
	    if tricky == True:
                time.sleep(0.07)
		tricky = False
	    else:
		tricky = True
except:
    io.cleanup()
