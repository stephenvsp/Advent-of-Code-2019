lowerLimit = 367479
upperLimit = 893698


def containsTwoAdjacentDigits(input):
    input = str(input)

    numDict = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}

    for c in input:
        numDict[c] = numDict[c] + 1

    for item in numDict.items():
        key, value = item

        if (value == 2):
            return True
    
    return False
    


def ascendingNumber(input):
    input = str(input)
    for i in range(0, len(input) - 1):
        if (input[i] > input[i + 1]):
            return False

    return True


count = 0

for i in range(lowerLimit, upperLimit):
    if (containsTwoAdjacentDigits(i) and ascendingNumber(i)):
        count += 1

print(count)