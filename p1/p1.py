import math

inputFile = open("p1_input.py", "r")
outputFile = open("p1_output.py", "w")

sum = 0

for i in inputFile:
    mass = int(i)
    fuel = (math.floor(mass / 3)) - 2
    sum += fuel

outputFile.write(str(sum))

inputFile.close()
outputFile.close()
