# Solving the Cosmic Path Optimization Problem On Kattis
# Christopher Brandt
import sys

numReadings=input()
numReadings=int(numReadings)
averageReading=0
reading=input()
tempReadings=reading.split()
if (numReadings!=len(tempReadings)):
    sys.exit()

for reading in tempReadings:
    averageReading = averageReading + int(reading)

print(averageReading//numReadings)