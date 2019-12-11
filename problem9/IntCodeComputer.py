def run_program(int_code, inputs=[]):
    output = []
    relative_base = 0
    pc = 0

    def parse_opcode(opcode):
        opcode = str(opcode)

        while (len(opcode) < 5):
            opcode = '0' + opcode

        operation = int(opcode[-2:])
        firstParamMode = int(opcode[2])
        secondParamMode = int(opcode[1])
        thirdParamMode = int(opcode[0])

        return thirdParamMode, secondParamMode, firstParamMode, operation

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

        int_code = grow_memory_if_needed(new_location)
        return new_location

    def grow_memory_if_needed(new_position):
        last_space = len(int_code) - 1

        if (new_position > last_space):
            difference = new_position - last_space

            new_memory = [0 for i in range(0, difference)]
            int_code.extend(new_memory)

        return int_code

    while pc < len(int_code):

        third_param_mode, second_param_mode, first_param_mode, operation = parse_opcode(
            int_code[pc])

        # 1 - addition, 2 - multiplication
        if operation == 1 or operation == 2:
            location_one = get_location(pc + 1, first_param_mode)

            location_two = get_location(pc + 2, second_param_mode)

            output_position = get_location(pc + 3, third_param_mode)

            val1 = int_code[location_one]
            val2 = int_code[location_two]

            result = val1 + val2 if operation == 1 else val1 * val2

            int_code[output_position] = result

            pc += 4

        # 3 - read from input and write to position
        elif (operation == 3):

            location_one = get_location(pc + 1, first_param_mode)

            inputVal = int(inputs.pop(0))

            int_code[location_one] = inputVal

            pc += 2

        # 4 - print out position
        elif (operation == 4):
            location_one = get_location(pc + 1, first_param_mode)

            val1 = int_code[location_one]

            output.append(val1)

            pc += 2

        # 5 - jump if true
        elif (operation == 5):
            location_one = get_location(pc + 1, first_param_mode)
            location_two = get_location(pc + 2, second_param_mode)

            val1 = int_code[location_one]
            val2 = int_code[location_two]

            if (val1 != 0):
                pc = val2
            else:
                pc += 3

        # 6 - jump if false
        elif (operation == 6):
            location_one = get_location(pc + 1, first_param_mode)
            location_two = get_location(pc + 2, second_param_mode)

            val1 = int_code[location_one]
            val2 = int_code[location_two]

            if val1 == 0:
                pc = val2
            else:
                pc += 3

        # 7 - less than
        elif (operation == 7):
            location_one = get_location(pc + 1, first_param_mode)

            location_two = get_location(pc + 2, second_param_mode)

            output_position = get_location(pc + 3, third_param_mode)

            val1 = int_code[location_one]
            val2 = int_code[location_two]

            if (val1 < val2):
                int_code[output_position] = 1
            else:
                int_code[output_position] = 0

            pc += 4

        # 8 - equals
        elif (operation == 8):
            location_one = get_location(pc + 1, first_param_mode)

            location_two = get_location(pc + 2, second_param_mode)

            output_position = get_location(pc + 3, third_param_mode)

            val1 = int_code[location_one]
            val2 = int_code[location_two]

            if (val1 == val2):
                int_code[output_position] = 1
            else:
                int_code[output_position] = 0

            pc += 4

        # 9 - change relative base
        elif (operation == 9):
            location_one = get_location(pc + 1, first_param_mode)

            val1 = int_code[location_one]

            relative_base += val1

            pc += 2

        # if operation is 99 no need to anything just exit
        if (operation == 99):
            break

    return output
