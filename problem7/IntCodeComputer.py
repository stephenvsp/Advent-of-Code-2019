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


def runIntCode(intCode, inputs, feedbackLoop=False, pc=0):
    pc = pc
    output = 0

    while pc < len(intCode):

        secondParamMode, firstParamMode, operation = parseOpcode(intCode[pc])

        # addition
        if (operation == 1):
            val1 = getValue(intCode, intCode[pc + 1], firstParamMode)
            val2 = getValue(intCode, intCode[pc + 2], secondParamMode)
            outputPosition = intCode[pc + 3]

            intCode[outputPosition] = val1 + val2

            pc += 4

        # multiplication
        elif (operation == 2):
            val1 = getValue(intCode, intCode[pc + 1], firstParamMode)
            val2 = getValue(intCode, intCode[pc + 2], secondParamMode)
            outputPosition = intCode[pc + 3]

            intCode[outputPosition] = val1 * val2

            pc += 4

        # read from input and write to position
        elif (operation == 3):
            writeTo = intCode[pc + 1]

            val = inputs.pop(0)

            intCode[writeTo] = int(val)

            pc += 2

        # print out position
        elif (operation == 4):
            output = getValue(intCode, intCode[pc + 1], firstParamMode)

            pc += 2

            if feedbackLoop:
                return output, pc

        # jump if true
        elif (operation == 5):
            val1 = getValue(intCode, intCode[pc + 1], firstParamMode)
            val2 = getValue(intCode, intCode[pc + 2], secondParamMode)

            if (val1 != 0):
                pc = val2
            else:
                pc += 3

        # jump if false
        elif (operation == 6):
            val1 = getValue(intCode, intCode[pc + 1], firstParamMode)
            val2 = getValue(intCode, intCode[pc + 2], secondParamMode)

            if (val1 == 0):
                pc = val2
            else:
                pc += 3

        # less than
        elif (operation == 7):
            val1 = getValue(intCode, intCode[pc + 1], firstParamMode)
            val2 = getValue(intCode, intCode[pc + 2], secondParamMode)
            outputPosition = intCode[pc + 3]

            if (val1 < val2):
                intCode[outputPosition] = 1
            else:
                intCode[outputPosition] = 0

            pc += 4

        # equals
        elif (operation == 8):
            val1 = getValue(intCode, intCode[pc + 1], firstParamMode)
            val2 = getValue(intCode, intCode[pc + 2], secondParamMode)
            outputPosition = intCode[pc + 3]

            if (val1 == val2):
                intCode[outputPosition] = 1
            else:
                intCode[outputPosition] = 0

            pc += 4

        elif (operation == 99):
            if feedbackLoop:
                return output, None
            break

    return output
