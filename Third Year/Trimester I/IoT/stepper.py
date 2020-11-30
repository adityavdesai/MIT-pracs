from RPi.GPIO import setmode, setwarnings, setup, output, BCM, HIGH, LOW, OUT, cleanup
from time import sleep

pins = [17, 27, 22, 23]

setmode(BCM)
setwarnings(False)

for i in pins:
    setup(i, OUT)
    output(i, 0)

c = [
    [1,0,0,0],
    [1,1,0,0],
    [0,1,0,0],
    [0,1,1,0],
    [0,0,1,0],
    [0,0,1,1],
    [0,0,0,1],
    [1,0,0,1]
]
try:
    for i in range(512):
        for i in range(8):

            for j in range(4):
                output(pins[j], c[i][j])

            sleep(0.01)

except KeyboardInterrupt:
    cleanup()
