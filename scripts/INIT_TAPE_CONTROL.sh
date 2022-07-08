#!/bin/sh
# Updated for foof H'53 cxf@meh feature
#
# GPIO numbers should be from this list
# 0, 1, 4, 7, 8, 9, 10, 11, 14, 15, 17, 18, 21, 22, 23, 24, 25

# Note that the GPIO numbers that you program here refer to the pins
# of the BCM2835 and *not* the numbers on the pin header. 
# So, if you want to activate GPIO7 on the header you should be 
# using GPIO4 in this script. Likewise if you want to activate GPIO0
# on the header you should be using GPIO17 here.

# Set up GPIO 18 and set to output - STOP
sudo echo "18" > /sys/class/gpio/export
sudo echo "out" > /sys/class/gpio/gpio18/direction

# Set up GPIO 23 and set to output - PLAY
sudo echo "23" > /sys/class/gpio/export
sudo echo "out" > /sys/class/gpio/gpio23/direction


# Set up GPIO 7 and set to input
# echo "7" > /sys/class/gpio/export
# echo "in" > /sys/class/gpio/gpio7/direction

# Write output
# sudo echo "1" > /sys/class/gpio/gpio23/value

# wait 1s
# sleep 1 

# sudo echo "0" > /sys/class/gpio/gpio23/value

# Read from input
# cat /sys/class/gpio/gpio7/value 

# Clean up
# sudo echo "18" > /sys/class/gpio/unexport
# echo "7" > /sys/class/gpio/unexport

