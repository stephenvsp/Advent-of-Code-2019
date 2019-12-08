def parseOpcode(opcode):
    opcode = str(opcode)

    while (len(opcode) < 5):
        opcode = '0' + opcode

    operation = int(opcode[-2:])
    firstParamMode = int(opcode[2])
    secondParamMode = int(opcode[1])

    return secondParamMode, firstParamMode, operation


def getValue(intCode, param, mode):

    # 0 for position mode
    if(mode == 0):
        return intCode[param]
    # 1 for immediate mode
    else:
        return param


def runIntCode(intCode, inputs):
    numInputToRead = 0
    i = 0

    while(intCode[i] != 99):

        secondParamMode, firstParamMode, operation = parseOpcode(intCode[i])

        # addition
        if (operation == 1):
            val1 = getValue(intCode, intCode[i + 1], firstParamMode)
            val2 = getValue(intCode, intCode[i + 2], secondParamMode)
            outputPosition = intCode[i + 3]

            intCode[outputPosition] = val1 + val2

            i += 4

        # multiplication
        elif (operation == 2):
            val1 = getValue(intCode, intCode[i + 1], firstParamMode)
            val2 = getValue(intCode, intCode[i + 2], secondParamMode)
            outputPosition = intCode[i + 3]

            intCode[outputPosition] = val1 * val2

            i += 4

        # read from input and write to position
        elif (operation == 3):
            writeTo = intCode[i + 1]

            val = inputs[numInputToRead]
            numInputToRead += 1

            intCode[writeTo] = int(val)

            i += 2

        # print out position
        elif (operation == 4):
            val1 = getValue(intCode, intCode[i + 1], firstParamMode)
            return val1

        # jump if true
        elif (operation == 5):
            val1 = getValue(intCode, intCode[i + 1], firstParamMode)
            val2 = getValue(intCode, intCode[i + 2], secondParamMode)

            if (val1 != 0):
                i = val2
            else:
                i += 3

        # jump if false
        elif (operation == 6):
            val1 = getValue(intCode, intCode[i + 1], firstParamMode)
            val2 = getValue(intCode, intCode[i + 2], secondParamMode)

            if (val1 == 0):
                i = val2
            else:
                i += 3

        # less than
        elif (operation == 7):
            val1 = getValue(intCode, intCode[i + 1], firstParamMode)
            val2 = getValue(intCode, intCode[i + 2], secondParamMode)
            outputPosition = intCode[i + 3]

            if (val1 < val2):
                intCode[outputPosition] = 1
            else:
                intCode[outputPosition] = 0

            i += 4

        # equals
        elif (operation == 8):
            val1 = getValue(intCode, intCode[i + 1], firstParamMode)
            val2 = getValue(intCode, intCode[i + 2], secondParamMode)
            outputPosition = intCode[i + 3]

            if (val1 == val2):
                intCode[outputPosition] = 1
            else:
                intCode[outputPosition] = 0

            i += 4
