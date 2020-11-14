
def shuffle(deck_size, sequence, offset = 0, increment = 1): 

    def mod_inverse(n):
        return pow(n, deck_size - 2, deck_size)

    for shuffle in sequence:
        if "deal into new stack" in shuffle:
            increment *= -1
            offset += increment

        elif "deal with increment" in shuffle:
            new_increment = int(shuffle.split()[-1])

            inverse = mod_inverse(new_increment)

            increment *= inverse

        elif "cut" in shuffle:
            amount = int(shuffle.split()[-1])

            offset += increment * amount

        offset = pow(offset, 1, deck_size)
        increment = pow(increment, 1, deck_size)

    return (offset, increment)

