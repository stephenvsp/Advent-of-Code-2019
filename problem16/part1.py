initial_sequence = '59773419794631560412886746550049210714854107066028081032096591759575145680294995770741204955183395640103527371801225795364363411455113236683168088750631442993123053909358252440339859092431844641600092736006758954422097244486920945182483159023820538645717611051770509314159895220529097322723261391627686997403783043710213655074108451646685558064317469095295303320622883691266307865809481566214524686422834824930414730886697237161697731339757655485312568793531202988525963494119232351266908405705634244498096660057021101738706453735025060225814133166491989584616948876879383198021336484629381888934600383957019607807995278899293254143523702000576897358'

#test input
#ans = 24176176 after 100 phases
test_input1 = '80871224585914546619083218645595'

#test input 2
#ans = 73745418 after 100 phases
test_input2 = '19617804207202209144916044189917'

#test input 3 
#ans = 52432133 after 100 phases
test_input3 = '69317163492948606335995924319873'

#test input 4
#ans = 48226158 after 1 phases
#ans = 34040438 after 2 phases
test_input4 = '12345678'



def generate_pattern(i, sequence):
    #first generate pattern for phase number
    base_pattern = [1] * (i + 1)
    base_pattern.extend([0] * (i + 1))
    base_pattern.extend([-1] * (i + 1))
    base_pattern.extend([0] * (i + 1))

    padding = [0] * i

    pattern = padding

    while len(pattern) < len(sequence):
        pattern += base_pattern

    return pattern[:len(sequence)] 

num_phases = 100

sequence = initial_sequence

for i in range(0, num_phases):

    new_sequence = ''
    for j in range(0, len(sequence)):
        
        pattern = generate_pattern(j, sequence)

        multiply_lists = [int(a) * b for a, b in zip(sequence, pattern)]

        value_at_index = sum(multiply_lists)

        value_at_index = abs(value_at_index) % 10

        new_sequence += str(value_at_index)

    sequence = new_sequence

print(sequence[:8])
    
