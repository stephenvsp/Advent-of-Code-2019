def run_program(int_code, inputs=[]):

    output = []
    relative_base = 0
    pc = 0

    def parse_opcode(opcode):
        opcode = str(opcode)

        while (len(opcode) < 5):
            opcode = '0' + opcode

        operation = int(opcode[-2:])
        first_mode = int(opcode[2])
        second_mode = int(opcode[1])
        third_mode = int(opcode[0])

        return [first_mode, second_mode, third_mode], operation

    def get_value(pc, mode):
        return int_code[get_location(pc, mode)]

    def get_location(pc, mode):
        nonlocal int_code
        nonlocal relative_base

        new_location = 0
        # 0 for position mode
        if mode == 0:
            new_location = int_code[pc]
        # 1 for a immediate mode
        elif mode == 1:
            new_location = pc
        # 2 for relative mode
        elif mode == 2:
            new_location = int_code[pc] + relative_base

        grow_memory_if_needed(new_location)
        return new_location

    def grow_memory_if_needed(new_position):
        last_space = len(int_code) - 1

        int_code.extend(
            [0 for i in range(last_space, new_position)])

    while pc < len(int_code):

        modes, operation = parse_opcode(int_code[pc])

        # 1 - addition, 2 - multiplication
        if operation == 1 or operation == 2:
            val1 = get_value(pc + 1, modes[0])
            val2 = get_value(pc + 2, modes[1])

            output_position = get_location(pc + 3, modes[2])

            # if operation is 1 addition
            # if operation is 2 multiplication
            result = val1 + val2 if operation == 1 else val1 * val2

            int_code[output_position] = result

            increment = 4

        # 3 - read from input and write to position
        elif (operation == 3):

            location_one = get_location(pc + 1, modes[0])

            int_code[location_one] = int(inputs.pop(0))

            increment = 2

        # 4 - print out position
        elif (operation == 4):
            val1 = get_value(pc + 1, modes[0])

            output.append(val1)

            increment = 2

        # 5 - jump if true
        elif (operation == 5):
            val1 = get_value(pc + 1, modes[0])
            val2 = get_value(pc + 2, modes[1])

            if (val1 != 0):
                increment = 0
                pc = val2
            else:
                increment = 3

        # 6 - jump if false
        elif (operation == 6):

            val1 = get_value(pc + 1, modes[0])
            val2 = get_value(pc + 2, modes[1])

            if val1 == 0:
                increment = 0
                pc = val2
            else:
                increment = 3

        # 7 - less than
        elif (operation == 7):
            val1 = get_value(pc + 1, modes[0])
            val2 = get_value(pc + 2, modes[1])

            output_position = get_location(pc + 3, modes[2])

            if (val1 < val2):
                int_code[output_position] = 1
            else:
                int_code[output_position] = 0

            increment = 4

        # 8 - equals
        elif (operation == 8):
            val1 = get_value(pc + 1, modes[0])
            val2 = get_value(pc + 2, modes[1])

            output_position = get_location(pc + 3, modes[2])

            if (val1 == val2):
                int_code[output_position] = 1
            else:
                int_code[output_position] = 0

            increment = 4

        # 9 - change relative base
        elif (operation == 9):
            val1 = get_value(pc + 1, modes[0])

            relative_base += val1

            increment = 2

        #99 - halt
        elif (operation == 99):
            break

        else:
            print('you dont fucked up')
            break

        pc += increment

    return output
