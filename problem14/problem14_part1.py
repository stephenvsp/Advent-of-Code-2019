with open('input.txt') as file:
    reactions = file.readlines()

reactions = [reaction.strip() for reaction in reactions]

for reaction in reactions:
    print(reaction)
