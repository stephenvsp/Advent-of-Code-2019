import math


def calculateFuel(mass):
    return (math.floor(mass / 3)) - 2


inputFile = open("p1_input.py", "r")
outputFile = open("p1_output.py", "w")

sum = 0

for i in inputFile:
    mass = int(i)
    fuel = calculateFuel(mass)
    fuelTotal = fuel

    while(fuel > 0):
        fuel = calculateFuel(fuel)
        if (fuel > 0):
            fuelTotal += fuel

    sum += fuelTotal


outputFile.write(str(sum))

inputFile.close()
outputFile.close()
