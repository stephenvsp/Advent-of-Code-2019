def run_program(int_code, inputs=[], loop=False, pc=0, rb=0):

    outputs = []
    inputs = inputs
    pc = pc
    relative_base = rb

    def parse_opcode(opcode):
        opcode = str(opcode)

        while (len(opcode) < 5):
            opcode = '0' + opcode

        return int(opcode[3:]), [int(opcode[2]), int(opcode[1]), int(opcode[0])]

    def get_value(pc, mode):
        return int_code[get_location(pc, mode)]

    def get_location(pc, mode):
        nonlocal int_code
        nonlocal relative_base

        # 0 for position mode
        if mode == 0:
            new_location = int_code[pc]
        # 1 for a immediate mode
        elif mode == 1:
            new_location = pc
        # 2 for relative mode
        elif mode == 2:
            new_location = int_code[pc] + relative_base

        get_more_memory_if_needed(new_location)
        return new_location

    def get_more_memory_if_needed(new_position):
        last_space = len(int_code) - 1

        int_code.extend(
            [0 for i in range(last_space, new_position)])

    while pc < len(int_code):

        op, modes = parse_opcode(int_code[pc])

        # 1 - addition
        if op == 1 or op == 2:
            val1 = get_value(pc + 1, modes[0])
            val2 = get_value(pc + 2, modes[1])
            output_position = get_location(pc + 3, modes[2])

            int_code[output_position] = val1 + val2 if op == 1 else val1 * val2

            increment = 4

        # 3 - read from input and write to position
        elif (op == 3):
            store_to_index = get_location(pc + 1, modes[0])

            int_code[store_to_index] = inputs.pop(0)

            increment = 2

        # 4 - print out position
        elif (op == 4):
            output_val = get_value(pc + 1, modes[0])

            outputs.append(output_val)

            increment = 2

            if loop:
                return outputs, pc + increment, relative_base

        # 5 - jump if true
        elif (op == 5):
            val1 = get_value(pc + 1, modes[0])
            val2 = get_value(pc + 2, modes[1])

            if (val1 != 0):
                increment = 0
                pc = val2
            else:
                increment = 3

        # 6 - jump if false
        elif (op == 6):
            val1 = get_value(pc + 1, modes[0])
            val2 = get_value(pc + 2, modes[1])

            if val1 == 0:
                increment = 0
                pc = val2
            else:
                increment = 3

        # 7 - less than
        elif (op == 7):
            val1 = get_value(pc + 1, modes[0])
            val2 = get_value(pc + 2, modes[1])
            output_position = get_location(pc + 3, modes[2])

            int_code[output_position] = 1 if val1 < val2 else 0

            increment = 4

        # 8 - equals
        elif (op == 8):
            val1 = get_value(pc + 1, modes[0])
            val2 = get_value(pc + 2, modes[1])
            output_position = get_location(pc + 3, modes[2])

            int_code[output_position] = 1 if val1 == val2 else 0

            increment = 4

        # 9 - change relative base
        elif (op == 9):
            relative_base += get_value(pc + 1, modes[0])

            increment = 2

        # 99 - halt
        elif (op == 99):
            if loop:
                return outputs, None, None
            else:
                return outputs

        else:
            print('you done fucked up')
            break

        pc += increment

    if loop:
        return outputs, None, None
    else: 
        return outputs
