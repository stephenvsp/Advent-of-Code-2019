lowerLimit = 367479
upperLimit = 893698


def containsTwoAdjacentDigits(input):
    input = str(input)

    for i in range(0, len(input) - 1):
        if (input[i] == input[i + 1]):
            return True
    return False


def ascendingNumber(input):
    input = str(input)
    for i in range(0, len(input) - 1):
        if (input[i] > input[i + 1]):
            return False

    return True


count = 0

# for i in range(lowerLimit, upperLimit):
#    if (containsTwoAdjacentDigits(i) and ascendingNumber(i)):
#        count += 1

print(containsTwoAdjacentDigits(123444))
print(containsTwoAdjacentDigits(111122))
