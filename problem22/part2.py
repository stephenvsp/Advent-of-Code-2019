
def shuffle(deck_size, sequence, offset = 0, increment = 1): 

    for shuffle in sequence:
        if "deal into new stack" in shuffle:
            increment *= -1
            offset += increment

        elif "deal with increment" in shuffle:
            new_increment = int(shuffle.split()[-1])

            increment *= mod_inverse(new_increment, deck_size)

        elif "cut" in shuffle:
            amount = int(shuffle.split()[-1])

            offset += increment * amount

        offset = pow(offset, 1, deck_size)
        increment = pow(increment, 1, deck_size)

    return (offset, increment)

def mod_inverse(n, m):
    return pow(n, m - 2, m)