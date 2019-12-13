
program = [3,8,1005,8,338,1106,0,11,0,0,0,104,1,104,0,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,1,8,10,4,10,102,1,8,28,1,108,6,10,1,3,7,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,1,8,10,4,10,1001,8,0,58,2,5,19,10,1,1008,7,10,2,105,6,10,1,1007,7,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,0,10,4,10,101,0,8,97,1006,0,76,1,106,14,10,2,9,9,10,1006,0,74,3,8,102,-1,8,10,101,1,10,10,4,10,108,1,8,10,4,10,1002,8,1,132,1006,0,0,2,1104,15,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,0,10,4,10,1001,8,0,162,1,1005,13,10,3,8,1002,8,-1,10,101,1,10,10,4,10,108,1,8,10,4,10,101,0,8,187,1,1,15,10,2,3,9,10,1006,0,54,3,8,102,-1,8,10,101,1,10,10,4,10,108,0,8,10,4,10,102,1,8,220,1,104,5,10,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,0,10,4,10,102,1,8,247,1,5,1,10,1,1109,2,10,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,0,10,4,10,1001,8,0,277,1006,0,18,3,8,1002,8,-1,10,101,1,10,10,4,10,108,1,8,10,4,10,101,0,8,301,2,105,14,10,1,5,1,10,2,1009,6,10,1,3,0,10,101,1,9,9,1007,9,1054,10,1005,10,15,99,109,660,104,0,104,1,21101,0,47677546524,1,21101,0,355,0,1105,1,459,21102,936995299356,1,1,21101,0,366,0,1106,0,459,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21101,0,206312807515,1,21102,1,413,0,1105,1,459,21101,206253871296,0,1,21102,424,1,0,1106,0,459,3,10,104,0,104,0,3,10,104,0,104,0,21102,1,709580554600,1,21102,1,447,0,1105,1,459,21101,0,868401967464,1,21101,458,0,0,1106,0,459,99,109,2,22102,1,-1,1,21102,1,40,2,21101,0,490,3,21102,480,1,0,1106,0,523,109,-2,2105,1,0,0,1,0,0,1,109,2,3,10,204,-1,1001,485,486,501,4,0,1001,485,1,485,108,4,485,10,1006,10,517,1101,0,0,485,109,-2,2105,1,0,0,109,4,2101,0,-1,522,1207,-3,0,10,1006,10,540,21102,0,1,-3,21201,-3,0,1,21202,-2,1,2,21101,0,1,3,21101,0,559,0,1105,1,564,109,-4,2106,0,0,109,5,1207,-3,1,10,1006,10,587,2207,-4,-2,10,1006,10,587,21202,-4,1,-4,1105,1,655,21201,-4,0,1,21201,-3,-1,2,21202,-2,2,3,21102,606,1,0,1105,1,564,22102,1,1,-4,21102,1,1,-1,2207,-4,-2,10,1006,10,625,21102,1,0,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,647,22101,0,-1,1,21101,0,647,0,106,0,522,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2106,0,0]


def run_program(int_code, pc=0):

    #initial input is 0
    outputs = []
    relative_base = 0

    curr_x = 0
    curr_y = 0

    #0 == UP
    #1 == RIGHT
    #2 == DOWN
    #3 == LEFT
    direction_facing = 0

    #starting space is white
    ship_map = {(curr_x, curr_y) : 1}

    def move_robot():
        nonlocal curr_x
        nonlocal curr_y

        #this only happens the first turn
        if outputs == []:
            return ship_map[(curr_x, curr_y)]

        color_to_paint = outputs.pop(0)
        direction_to_turn = outputs.pop(0)

        # paint current space
        ship_map[(curr_x, curr_y)] = color_to_paint

        #change direction
        direction_facing = change_direction(direction_to_turn)

        #move
        curr_x, curr_y = move_direction(direction_facing)

        #return current square color
        if (curr_x, curr_y) in ship_map:
            return ship_map[(curr_x, curr_y)]
        else: 
            # we haven't visited this square so it is black
            return 0



    def change_direction(change):
        nonlocal direction_facing
        if change == 0:
            direction_facing -= 1
        else:
            direction_facing += 1

        return direction_facing % 4

    def move_direction(direction):
        nonlocal curr_x
        nonlocal curr_y

        if direction == 0:
            curr_y += 1
        
        elif direction == 1:
            curr_x += 1

        elif direction == 2:
            curr_y -= 1

        elif direction == 3:
            curr_x -= 1
        
        return curr_x, curr_y

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

            input_val = move_robot()

            int_code[store_to_index] = input_val

            increment = 2

        # 4 - print out position
        elif (op == 4):
            val = get_value(pc + 1, modes[0])

            outputs.append(val)

            increment = 2

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

        #99 - halt
        elif (op == 99):
            break

        else:
            print('you done fucked up')
            break

        pc += increment

    max_possible_x = len(ship_map.keys())
    max_possible_y = len(ship_map.keys())

    for y in range(max_possible_y, -max_possible_y, -1):
        row = ''
        for x in range(-max_possible_x, max_possible_x, 1):

            if (x, y) in ship_map:
                curr_space = ship_map[x, y]

                if curr_space == 0:
                    row += ' '
                else:
                    row += '1'
        
        if row != '':
            print(row)

run_program(program)