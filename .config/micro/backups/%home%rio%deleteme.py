


























%%sim_magic_preloaded -Cp -b Coloured_bands -x 100 -y 700

# Program to create a square

# We need a delay in the loop...
from time import sleep

# Setup the colour sensor
colorLeft = ColorSensor(INPUT_2)

# Start the robot moving
tank_drive.on(SpeedPercent(30), SpeedPercent(30))

# Loop until we reach the line
while colorLeft.rgb != [0, 0, 255]:
    # We need some delay in the loop
    # or the program will hang
    sleep(0.1)

# Stop
tank_drive.off()
