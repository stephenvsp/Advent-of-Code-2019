import math

# real input
io = ["io", [3, 3, 0], [0, 0, 0]]
europa = ["europa", [4, -16, 2], [0, 0, 0]]
ganymede = ["ganymede", [-10, -6, 5], [0, 0, 0]]
callisto = ["callisto", [-3, 0, -13], [0, 0, 0]]

# test input
# io = ["io", [-8, -10, 0], [0, 0, 0]]
# europa = ["europa", [5, 5, 10], [0, 0, 0]]
# ganymede = ["ganymede", [2, -7, 3], [0, 0, 0]]
# callisto = ["callisto", [9, -8, -3], [0, 0, 0]]

# moon pairs
# io/europa
# io/ganymede
# io/callisto
# europa/ganymede
# europa/callisto
# ganymede/callisto

moons = [io, europa, ganymede, callisto]


def update_moon_pair_velocity(moon1, moon2):
    for i in range(0, 3):

        # moon one's position is greater than moon two's position
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

position_map = {}


def axis_to_tuple(moon, i):
    return (moon[1][i], moon[2][i])


def moon_list_to_tuple_by_axis(i):
    moon1_tuple = axis_to_tuple(moons[0], i)
    moon2_tuple = axis_to_tuple(moons[1], i)
    moon3_tuple = axis_to_tuple(moons[2], i)
    moon4_tuple = axis_to_tuple(moons[3], i)

    return (moon1_tuple, moon2_tuple, moon3_tuple, moon4_tuple)


x_cycle_time = 0

x_position_map = {}

# calculate cycle time of LCM
while(True):

    curr_x_position = moon_list_to_tuple_by_axis(0)

    if curr_x_position in x_position_map:
        break
    else:
        x_position_map[curr_x_position] = True
        x_cycle_time += 1

    for i in range(0, len(moons) - 1):
        for j in range(i + 1, len(moons)):
            update_moon_pair_velocity(moons[i], moons[j])

    apply_velocity()

y_cycle_time = 0

y_position_map = {}

# calculate cycle time of LCM
while(True):

    curr_y_position = moon_list_to_tuple_by_axis(1)

    if curr_y_position in y_position_map:
        break
    else:
        y_position_map[curr_y_position] = True
        y_cycle_time += 1

    for i in range(0, len(moons) - 1):
        for j in range(i + 1, len(moons)):
            update_moon_pair_velocity(moons[i], moons[j])

    apply_velocity()

z_cycle_time = 0

z_position_map = {}

# calculate cycle time of LCM
while(True):

    curr_z_position = moon_list_to_tuple_by_axis(2)

    if curr_z_position in z_position_map:
        break
    else:
        z_position_map[curr_z_position] = True
        z_cycle_time += 1

    for i in range(0, len(moons) - 1):
        for j in range(i + 1, len(moons)):
            update_moon_pair_velocity(moons[i], moons[j])

    apply_velocity()


def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)


lcm = lcm(lcm(x_cycle_time, y_cycle_time), z_cycle_time)

print(lcm)
