#real input
io = ["io", [3, 3, 0], [0, 0, 0]]
europa = ["europa", [4, -16, 2], [0, 0, 0]]
ganymede = ["ganymede", [-10, -6, 5], [0, 0, 0]]
callisto = ["callisto", [-3, 0, -13], [0, 0, 0]]

#test input
#io = ["io", [-1, 0, 2], [0, 0, 0]]
#europa = ["europa", [2, -10, -7], [0, 0, 0]]
#ganymede = ["ganymede", [4, -8, 8], [0, 0, 0]]
#callisto = ["callisto", [3, 5, -1], [0, 0, 0]]

#moon pairs
#io/europa
#io/ganymede
#io/callisto
#europa/ganymede
#europa/callisto
#ganymede/callisto

moons = [io, europa, ganymede, callisto]

def update_moon_pair_velocity(moon1, moon2):
    for i in range(0, 3):

        #moon one's position is greater than moon two's position
        if moon1[1][i] > moon2[1][i]:
            moon1[2][i] -= 1
            moon2[2][i] += 1

        elif moon1[1][i] < moon2[1][i]:
            moon1[2][i] += 1
            moon2[2][i] -= 1

def apply_velocity():
    for moon in moons:
        for i in range(0, 3):
            moon[1][i] += moon[2][i]

def calculate_energy():
    total_energy = 0

    for moon in moons:

        potential_energy = abs(moon[1][0]) + abs(moon[1][1]) + abs(moon[1][2])
        kinetic_energy = abs(moon[2][0]) + abs(moon[2][1]) + abs(moon[2][2])

        total_energy += potential_energy * kinetic_energy
    
    return total_energy


num_steps = 1000

for step in range(0, num_steps):

    for i in range(0, len(moons) - 1):
        for j in range(i + 1, len(moons)):
            update_moon_pair_velocity(moons[i], moons[j])

    apply_velocity()

print(calculate_energy())