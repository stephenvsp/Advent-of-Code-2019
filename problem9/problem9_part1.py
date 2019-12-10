from IntCodeComputer import run_program

# should output itself
test1_program = [109, 1, 204, -1, 1001, 100, 1,
                 100, 1008, 100, 16, 101, 1006, 101, 0, 99]

# should output a large 16 digit number
test2_program = [1102, 34915192, 34915192, 7, 4, 7, 99, 0]

# should output number in middle
test3_program = [104, 1125899906842624, 99]

print(run_program(test1_program))
