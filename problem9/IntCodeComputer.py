def parse_opcode(opcode):
    opcode = str(opcode)

    while (len(opcode) < 5):
        opcode = '0' + opcode

    operation = int(opcode[-2:])
    firstParamMode = int(opcode[2])
    secondParamMode = int(opcode[1])
    thirdParamMode = int(opcode[0])

    return thirdParamMode, secondParamMode, firstParamMode, operation


def get_value_location(int_code, pc, mode, relative_base):

    # 0 for position mode
    if mode == 0:
        return int_code[pc]
    # 1 for a immediate mode
    elif mode == 1:
        return pc
    # 2 for relative mode
    if mode == 2:
        return int_code[pc] + relative_base


def grow_memory_if_needed(int_code, new_position):
    last_space = len(int_code) - 1

    if (new_position > last_space):
        difference = new_position - last_space

        new_memory = [0 for i in range(0, difference)]
        int_code.extend(new_memory)

    return int_code


def run_program(int_code, inputs=[], feedback_loop=False, pc=0, debug=False):
    pc = pc
    output = []

    relative_base = 0

    while pc < len(int_code):

        third_param_mode, second_param_mode, first_param_mode, operation = parse_opcode(
            int_code[pc])

        # if operation is 99 no need to anything just exit
        if (operation == 99):
            if feedback_loop:
                return output, None
            break

        if debug:
            print(
                f"idx: {pc} - current opcode: {int_code[pc]}, {third_param_mode}{second_param_mode}{first_param_mode}")

        # 1 - addition, 2 - multiplication
        if operation == 1 or operation == 2:
            location_one = get_value_location(
                int_code, pc + 1, first_param_mode, relative_base)

            location_two = get_value_location(
                int_code, pc + 2, second_param_mode, relative_base)

            output_position = int_code[pc + 3]

            int_code = grow_memory_if_needed(int_code, location_one)
            int_code = grow_memory_if_needed(int_code, location_two)
            int_code = grow_memory_if_needed(int_code, output_position)

            val1 = int_code[location_one]
            val2 = int_code[location_two]

            result = val1 + val2 if operation == 1 else val1 * val2

            int_code[output_position] = result

            pc += 4

        # 3 - read from input and write to position
        elif (operation == 3):
            if (int_code[pc] == 203):
                hello = 0

            location_one = get_value_location(
                int_code, pc + 1, first_param_mode, relative_base)

            inputVal = int(inputs.pop(0))

            print(
                f"Opcode {int_code[pc]}: idx{pc}: Altered {int_code[location_one]} at {location_one} to {inputVal}"
            )
            int_code[location_one] = inputVal

            pc += 2

        # 4 - print out position
        elif (operation == 4):
            location_one = get_value_location(
                int_code, pc + 1, first_param_mode, relative_base)

            int_code = grow_memory_if_needed(int_code, location_one)

            val1 = int_code[location_one]

            if debug:
                print(f"Opcode {int_code}: Output is {val1}")

            output.append(val1)

            pc += 2

            if feedback_loop:
                return output, pc

        # 5 - jump if true
        elif (operation == 5):
            location_one = get_value_location(
                int_code, pc + 1, first_param_mode, relative_base)
            location_two = get_value_location(
                int_code, pc + 2, second_param_mode, relative_base)

            int_code = grow_memory_if_needed(int_code, location_one)
            int_code = grow_memory_if_needed(int_code, location_two)

            val1 = int_code[location_one]
            val2 = int_code[location_two]

            if (val1 != 0):
                if debug:
                    print(
                        f"Opcode {int_code[pc]}: {val1} != 0. idx from {pc} to {val2}")
                pc = val2
            else:
                if debug:
                    print(f"Opcode {int_code[pc]}: {val1} == 0. noop")
                pc += 3

        # 6 - jump if false
        elif (operation == 6):
            location_one = get_value_location(
                int_code, pc + 1, first_param_mode, relative_base)
            location_two = get_value_location(
                int_code, pc + 2, second_param_mode, relative_base)

            int_code = grow_memory_if_needed(int_code, location_one)
            int_code = grow_memory_if_needed(int_code, location_two)

            val1 = int_code[location_one]
            val2 = int_code[location_two]

            if (val1 == 0):
                if debug:
                    print(f"Opcode {int_code[pc]}: idx from {pc} to {val2}")
                pc = val2
            else:
                pc += 3

        # 7 - less than
        elif (operation == 7):
            location_one = get_value_location(
                int_code, pc + 1, first_param_mode, relative_base)

            location_two = get_value_location(
                int_code, pc + 2, second_param_mode, relative_base)

            output_position = int_code[pc + 3]

            int_code = grow_memory_if_needed(int_code, location_one)
            int_code = grow_memory_if_needed(int_code, location_two)
            int_code = grow_memory_if_needed(int_code, output_position)

            val1 = int_code[location_one]
            val2 = int_code[location_two]

            if (val1 < val2):
                if debug:
                    print(
                        f"Opcode {int_code[pc]}: {val1} < {val2}, loc {output_position} from {int_code[output_position]} to 1")
                int_code[output_position] = 1
            else:
                if debug:
                    print(
                        f"Opcode {int_code}: {val1} !< {val2}, loc {output_position} from {int_code[output_position]} to 0")
                int_code[output_position] = 0

            pc += 4

        # 8 - equals
        elif (operation == 8):
            location_one = get_value_location(
                int_code, pc + 1, first_param_mode, relative_base)

            location_two = get_value_location(
                int_code, pc + 2, second_param_mode, relative_base)

            output_position = int_code[pc + 3]

            int_code = grow_memory_if_needed(int_code, location_one)
            int_code = grow_memory_if_needed(int_code, location_two)
            int_code = grow_memory_if_needed(int_code, output_position)

            val1 = int_code[location_one]
            val2 = int_code[location_two]

            if (val1 == val2):
                if debug:
                    print(
                        f"Opcode {int_code}: {val1} == {val2}, loc {output_position} from {int_code[output_position]} to 1")
                int_code[output_position] = 1
            else:
                if debug:
                    print(
                        f"Opcode {int_code}: {val1} != {val2}, loc {output_position} from {int_code[output_position]} to 0")
                int_code[output_position] = 0

            pc += 4

        # 9 - change relative base
        elif (operation == 9):
            location_one = get_value_location(
                int_code, pc + 1, first_param_mode, relative_base)

            int_code = grow_memory_if_needed(int_code, location_one)

            val1 = int_code[location_one]
            if debug:
                print(f'opcode 9, mode = {first_param_mode}, value = {val1}')
            relative_base += val1
            if debug:
                print(f"Relative Base now {relative_base}")

            pc += 2

    return output
