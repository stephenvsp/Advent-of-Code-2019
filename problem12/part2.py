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


def find_cycle_time_for_axis(axis):
    cycle_time = 0

    position_map = {}

    # calculate cycle time of LCM
    while(True):

        position = moon_list_to_tuple_by_axis(axis)

        if position in position_map:
            return cycle_time
        else:
            position_map[position] = True
            cycle_time += 1

        for i in range(0, len(moons) - 1):
            for j in range(i + 1, len(moons)):
                update_moon_pair_velocity(moons[i], moons[j])

        apply_velocity()


# because each axis is independent need to find the time it takes for one axis to go back to its original state
x_cycle_time = find_cycle_time_for_axis(0)
y_cycle_time = find_cycle_time_for_axis(1)
z_cycle_time = find_cycle_time_for_axis(2)

print(x_cycle_time)
print(y_cycle_time)
print(z_cycle_time)


def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)


# lcm of all these numbers is the time it takes for it to go back to an original state
lcm = lcm(lcm(x_cycle_time, y_cycle_time), z_cycle_time)

print(lcm)
