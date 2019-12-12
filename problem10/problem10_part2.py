import math

# strip \n's out of strings
asteroid_map = ['###..#########.#####.', '.####.#####..####.#.#', '.###.#.#.#####.##..##', '##.####.#.###########', '###...#.####.#.#.####', '#.##..###.########...', '#.#######.##.#######.', '.#..#.#..###...####.#', '#######.##.##.###..##', '#.#......#....#.#.#..',
                '######.###.#.#.##...#', '####.#...#.#######.#.', '.######.#####.#######', '##.##.##.#####.##.#.#', '###.#######..##.#....', '###.##.##..##.#####.#', '##.########.#.#.#####', '.##....##..###.#...#.', '#..#.####.######..###', '..#.####.############', '..##...###..#########']

# test map
# asteroid_map = ['.#..##.###...#######', '##.############..##.', '.#.######.########.#', '.###.#######.####.#.', '#####.##.#.##.###.##', '..#####..#.#########', '####################', '#.####....###.#.#.##', '##.#################', '#####.##.###..####..',
#                '..######..##.#######', '####.##.####...##..#', '.#####..#.######.###', '##...#.##########...', '#.##########.#######', '.####.#.###.###.#.##', '....##.##.###..#####', '.#.#.###########.###', '#.#.#.#####.####.###', '###.##.####.##.#..##']

max_x = len(asteroid_map[0])
max_y = len(asteroid_map)

# flip x and y's so it makes sense with coordinates
asteroid_map = [[asteroid_map[y][x]
                 for y in range(0, max_y)] for x in range(0, max_x)]

positive_x_positive_y_slopes = []
positive_x_negative_y_slopes = []
negative_x_positive_y_slopes = []
negative_x_negative_y_slopes = []
slopeDict = {}

for x in range(1, max_x):
    for y in range(1, max_y):
        if (x / y) not in slopeDict.keys():
            positive_x_positive_y_slopes.append((x, y, x / y))
            positive_x_negative_y_slopes.append((x, -y, x / -y))
            negative_x_positive_y_slopes.append((-x, y, -x / y))
            negative_x_negative_y_slopes.append((-x, -y, - x / -y))
            slopeDict[x / y] = True


destroyed_asteroids = []


def search_slope(run, rise, start_x, start_y):

    curr_x = start_x + run
    curr_y = start_y + rise
    while (is_inbounds(curr_x, curr_y)):
        if asteroid_map[curr_x][curr_y] == '#':
            return (curr_x, curr_y)
        curr_x += run
        curr_y += rise

    return None


def is_inbounds(my_x, my_y):

    if (my_x < 0 or my_x >= max_x):
        return False

    if (my_y < 0 or my_y >= max_y):
        return False

    return True


def destroy_asteroid(asteroid):
    if asteroid is not None:
        asteroid_map[asteroid[0]][asteroid[1]] = '.'
        destroyed_asteroids.append((asteroid[0], asteroid[1]))


def search_for_asteroids(x, y):

    # no x, negative y
    asteroid = search_slope(0, -1, x, y)
    destroy_asteroid(asteroid)

    # positive x, negative y
    for slope in positive_x_negative_y_slopes:
        asteroid = search_slope(slope[0], slope[1], x, y)
        destroy_asteroid(asteroid)

    # positive x, no y
    asteroid = search_slope(1, 0, x, y)
    destroy_asteroid(asteroid)

    # positive x, positive y
    for slope in positive_x_positive_y_slopes:
        asteroid = search_slope(slope[0], slope[1], x, y)
        destroy_asteroid(asteroid)

    # no x, positive y
    asteroid = search_slope(0, 1, x, y)
    destroy_asteroid(asteroid)

    # negative x, positive y
    for slope in negative_x_positive_y_slopes:
        asteroid = search_slope(slope[0], slope[1], x, y)
        destroy_asteroid(asteroid)

    # negative x, no y
    asteroid = search_slope(-1, 0, x, y)
    destroy_asteroid(asteroid)

    # negative x, negative y
    for slope in negative_x_negative_y_slopes:
        asteroid = search_slope(slope[0], slope[1], x, y)
        destroy_asteroid(asteroid)


# get the slopes in the order we want to traverse them
positive_x_negative_y_slopes = sorted(
    positive_x_negative_y_slopes, key=lambda x: -x[2])
positive_x_positive_y_slopes = sorted(
    positive_x_positive_y_slopes, key=lambda x: x[2])
negative_x_positive_y_slopes = sorted(
    negative_x_positive_y_slopes, key=lambda x: -x[2])
negative_x_negative_y_slopes = sorted(
    negative_x_negative_y_slopes, key=lambda x: -x[2])

all_slopes_in_counter_counter_clockwise = [(0, -1)]
all_slopes_in_counter_counter_clockwise.extend(positive_x_negative_y_slopes)
all_slopes_in_counter_counter_clockwise.append((1, 0))
all_slopes_in_counter_counter_clockwise.extend(positive_x_positive_y_slopes)
all_slopes_in_counter_counter_clockwise.append((0, 1))
all_slopes_in_counter_counter_clockwise.extend(negative_x_positive_y_slopes)
all_slopes_in_counter_counter_clockwise.append((-1, 0))
all_slopes_in_counter_counter_clockwise.extend(negative_x_negative_y_slopes)


def asteroids_left():
    for row in asteroid_map:
        if '#' in row:
            return True

    return False


my_asteroid_x = 11
my_asteroid_y = 11
asteroid_map[my_asteroid_x][my_asteroid_y] = '.'

while(asteroids_left()):
    search_for_asteroids(my_asteroid_x, my_asteroid_y)

print(destroyed_asteroids[199])
