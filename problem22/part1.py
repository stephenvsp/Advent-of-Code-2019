deck_size = 10007

deck = list(range(0, deck_size))
shuffles = ['deal with increment 74','deal into new stack','deal with increment 67','cut 6315','deal with increment 15','cut -8049','deal with increment 69','cut 2275','deal with increment 25','cut 4811','deal with increment 47','cut -9792','deal with increment 26','cut -3014','deal with increment 47','cut -1093','deal with increment 39','cut -5322','deal with increment 14','cut -7375','deal with increment 16','cut 9627','deal into new stack','cut 1632','deal into new stack','cut -2904','deal with increment 69','cut -3328','deal with increment 60','cut 7795','deal into new stack','deal with increment 37','cut -4238','deal with increment 19','cut -3170','deal with increment 45','cut 8631','deal with increment 64','cut -2380','deal with increment 59','cut -2802','deal with increment 19','cut -3369','deal with increment 45','deal into new stack','deal with increment 71','cut 5452','deal with increment 73','cut -6609','deal with increment 33','cut 1892','deal with increment 5','cut 1395','deal into new stack','cut -8514','deal with increment 46','deal into new stack','deal with increment 15','cut 3963','deal with increment 2','cut -2965','deal into new stack','cut 640','deal with increment 13','cut 8889','deal with increment 62','cut 8331','deal with increment 49','cut 6169','deal with increment 71','deal into new stack','deal with increment 33','cut 6342','deal with increment 52','cut 2875','deal with increment 39','cut 4283','deal with increment 19','cut 4102','deal with increment 57','deal into new stack','cut -7801','deal with increment 38','cut 4273','deal with increment 58','cut -2971','deal with increment 46','deal into new stack','cut 8043','deal with increment 52','cut -7108','deal with increment 21','cut 507','deal with increment 70','cut -8658','deal with increment 64','cut 7213','deal into new stack','deal with increment 61','cut 9439',]

# deck_size = 10
# deck = list(range(0, deck_size))
# shuffles = ["deal into new stack", "cut -2", "deal with increment 7", "cut 8", "cut -4", "deal with increment 7", "cut 3", "deal with increment 9", "deal with increment 3", "cut -1"]

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

shuffled_deck = shuffle(deck, shuffles)
print(shuffled_deck.index(2019))