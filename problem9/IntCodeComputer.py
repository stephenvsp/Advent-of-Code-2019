def parseOpcode(opcode):
    opcode = str(opcode)

    while (len(opcode) < 5):
        opcode = '0' + opcode

    operation = int(opcode[-2:])
    firstParamMode = int(opcode[2])
    secondParamMode = int(opcode[1])

    return secondParamMode, firstParamMode, operation


def get_value(intCode, param, mode, relative_base):

    # 0 for position mode
    if mode == 0:
        return intCode[param]
    # 1 for immediate mode
    elif mode == 1:
        return param
    else:
        return intCode[param + relative_base]

        # if feedback loops is enabled then we want to return None


def run_program(intCode, inputs=[], feedbackLoop=False, pc=0):
    pc = pc
    output = 0

    relative_base = 0

    while pc < len(intCode):

        secondParamMode, firstParamMode, operation = parseOpcode(intCode[pc])

        #1 - addition, 2 - multiplication
        if operation == 1 or operation == 2:
            val1 = get_value(
                intCode, intCode[pc + 1], firstParamMode, relative_base)
            val2 = get_value(
                intCode, intCode[pc + 2], secondParamMode, relative_base)
            outputPosition = intCode[pc + 3]

            intCode[outputPosition] = val1 + \
                val2 if operation == 1 else val1 * val2

            pc += 4

        # 3 - read from input and write to position
        elif (operation == 3):
            writeTo = intCode[pc + 1]

            val = inputs.pop(0)

            if (writeTo > len(intCode) - 1):
                neededSpace = writeTo - len(intCode) - 1

                extraSpace = [0 for i in range(0, neededSpace)]

                intCode.extend(extraSpace)

            intCode[writeTo] = int(val)

            pc += 2

        # 4 - print out position
        elif (operation == 4):
            output = get_value(
                intCode, intCode[pc + 1], firstParamMode, relative_base)

            pc += 2

            if feedbackLoop:
                return output, pc

        # 5 - jump if true
        elif (operation == 5):
            val1 = get_value(
                intCode, intCode[pc + 1], firstParamMode, relative_base)
            val2 = get_value(
                intCode, intCode[pc + 2], secondParamMode, relative_base)

            if (val1 != 0):
                pc = val2
            else:
                pc += 3

        # 6 - jump if false
        elif (operation == 6):
            val1 = get_value(
                intCode, intCode[pc + 1], firstParamMode, relative_base)
            val2 = get_value(
                intCode, intCode[pc + 2], secondParamMode, relative_base)

            if (val1 == 0):
                pc = val2
            else:
                pc += 3

        # 7 - less than
        elif (operation == 7):
            val1 = get_value(
                intCode, intCode[pc + 1], firstParamMode, relative_base)
            val2 = get_value(
                intCode, intCode[pc + 2], secondParamMode, relative_base)
            outputPosition = intCode[pc + 3]

            if (val1 < val2):
                intCode[outputPosition] = 1
            else:
                intCode[outputPosition] = 0

            pc += 4

        #8 - equals
        elif (operation == 8):
            val1 = get_value(
                intCode, intCode[pc + 1], firstParamMode, relative_base)
            val2 = get_value(
                intCode, intCode[pc + 2], secondParamMode, relative_base)
            outputPosition = intCode[pc + 3]

            if (val1 == val2):
                intCode[outputPosition] = 1
            else:
                intCode[outputPosition] = 0

            pc += 4

        # 9 - change relative base
        elif (operation == 9):
            val1 = get_value(
                intCode, intCode[pc + 1], firstParamMode, relative_base)

            relative_base += val1

            pc += 2

        # 99 - halt program
        elif (operation == 99):
            if feedbackLoop:
                return output, None
            break

    return output
