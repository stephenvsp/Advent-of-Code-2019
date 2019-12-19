from IntCodeComputer import run_program

program = [109,424,203,1,21101,0,11,0,1105,1,282,21101,18,0,0,1105,1,259,2101,0,1,221,203,1,21101,31,0,0,1105,1,282,21102,38,1,0,1106,0,259,20101,0,23,2,21201,1,0,3,21101,1,0,1,21101,0,57,0,1105,1,303,2101,0,1,222,21001,221,0,3,21001,221,0,2,21101,259,0,1,21101,0,80,0,1106,0,225,21102,117,1,2,21102,91,1,0,1105,1,303,2101,0,1,223,20102,1,222,4,21102,1,259,3,21101,0,225,2,21102,1,225,1,21101,0,118,0,1105,1,225,21001,222,0,3,21102,1,77,2,21102,133,1,0,1105,1,303,21202,1,-1,1,22001,223,1,1,21102,1,148,0,1105,1,259,2102,1,1,223,21002,221,1,4,20101,0,222,3,21102,20,1,2,1001,132,-2,224,1002,224,2,224,1001,224,3,224,1002,132,-1,132,1,224,132,224,21001,224,1,1,21102,195,1,0,106,0,109,20207,1,223,2,20102,1,23,1,21101,0,-1,3,21101,0,214,0,1106,0,303,22101,1,1,1,204,1,99,0,0,0,0,109,5,1202,-4,1,249,21201,-3,0,1,21201,-2,0,2,22101,0,-1,3,21102,250,1,0,1106,0,225,22101,0,1,-4,109,-5,2105,1,0,109,3,22107,0,-2,-1,21202,-1,2,-1,21201,-1,-1,-1,22202,-1,-2,-2,109,-3,2106,0,0,109,3,21207,-2,0,-1,1206,-1,294,104,0,99,21202,-2,1,-2,109,-3,2105,1,0,109,5,22207,-3,-4,-1,1206,-1,346,22201,-4,-3,-4,21202,-3,-1,-1,22201,-4,-1,2,21202,2,-1,-1,22201,-4,-1,1,21202,-2,1,3,21102,1,343,0,1105,1,303,1106,0,415,22207,-2,-3,-1,1206,-1,387,22201,-3,-2,-3,21202,-2,-1,-1,22201,-3,-1,3,21202,3,-1,-1,22201,-3,-1,2,21202,-4,1,1,21102,384,1,0,1106,0,303,1105,1,415,21202,-4,-1,-4,22201,-4,-3,-4,22202,-3,-2,-2,22202,-2,-4,-4,22202,-3,-2,-3,21202,-4,-1,-2,22201,-3,-2,1,22101,0,1,-4,109,-5,2105,1,0]

x = 0
y = 0

def check_coord(x, y):
    program_copy = program.copy()

    return run_program(program_copy, [x, y])


while not check_coord(x + 99, y):
    y += 1

    if not check_coord(x, y + 99):
        x += 1


print(x*10000 + y)


