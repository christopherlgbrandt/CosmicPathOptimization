# Solving the Cosmic Path Optimization Problem On Kattis
# Christopher Brandt
import sys

try:
    numReadings = input()
    numReadings =  numReadings.strip()
    
    if numReadings.isdigit():
        numReadings = int(numReadings)
    else:
        sys.exit()
except ValueError:
    sys.exit()

averageReading = 0
reading = input()
tempReadings = reading.split()
if (numReadings != len(tempReadings)):
    sys.exit()

for reading in tempReadings:
    averageReading = averageReading + int(reading)

print(averageReading//numReadings)
