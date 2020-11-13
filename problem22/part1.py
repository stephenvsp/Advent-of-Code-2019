
def shuffle(deck, sequence): 

    deck_size = len(deck)

    def deal_into_new_stack(deck):
        deck.reverse()
        return deck

    def deal_with_increment(deck, increment):
        new_deck = [None] * deck_size
        pos = 0
        for i in range(0, deck_size):
            new_deck[pos % deck_size] = deck[i]

            pos = pos + increment
        return new_deck

    def cut(deck, amount):
        cut = deck[:amount]
        rest = deck[amount:]
        return rest + cut

    for shuffle in sequence:
        if "deal into new stack" in shuffle:
            deck = deal_into_new_stack(deck)
        
        elif "deal with increment" in shuffle:
            increment = int(shuffle.split()[-1])
            deck = deal_with_increment(deck, increment)

        elif "cut" in shuffle:
            amount = int(shuffle.split()[-1])
            deck = cut(deck, amount)
    
    return deck
