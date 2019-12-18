import math

# strip \n's out of strings
asteroid_map = ['###..#########.#####.', '.####.#####..####.#.#', '.###.#.#.#####.##..##', '##.####.#.###########', '###...#.####.#.#.####', '#.##..###.########...', '#.#######.##.#######.', '.#..#.#..###...####.#', '#######.##.##.###..##', '#.#......#....#.#.#..',
                '######.###.#.#.##...#', '####.#...#.#######.#.', '.######.#####.#######', '##.##.##.#####.##.#.#', '###.#######..##.#....', '###.##.##..##.#####.#', '##.########.#.#.#####', '.##....##..###.#...#.', '#..#.####.######..###', '..#.####.############', '..##...###..#########']

# asteroid_map = ['.#..#', '.....', '#####', '....#', '...##']

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
            positive_x_positive_y_slopes.append((x, y))
            positive_x_negative_y_slopes.append((x, -y))
            negative_x_positive_y_slopes.append((-x, y))
            negative_x_negative_y_slopes.append((-x, -y))
            slopeDict[x / y] = True


def search_slope(run, rise, start_x, start_y):

    curr_x = start_x + run
    curr_y = start_y + rise
    while (is_inbounds(curr_x, curr_y)):
        if asteroid_map[curr_x][curr_y] == '#':
            return 1
        curr_x += run
        curr_y += rise

    return 0


def is_inbounds(my_x, my_y):

    if (my_x < 0 or my_x >= max_x):
        return False

    if (my_y < 0 or my_y >= max_y):
        return False

    return True


def search_for_asteroids(x, y):
    count = 0

    # up
    count += search_slope(0, 1, x, y)

    # down
    count += search_slope(0, -1, x, y)

    # left
    count += search_slope(-1, 0, x, y)

    # right
    count += search_slope(1, 0, x, y)

    for slope in positive_x_positive_y_slopes:
        count += search_slope(slope[0], slope[1], x, y)

    for slope in positive_x_negative_y_slopes:
        count += search_slope(slope[0], slope[1], x, y)

    for slope in negative_x_positive_y_slopes:
        count += search_slope(slope[0], slope[1], x, y)

    for slope in negative_x_negative_y_slopes:
        count += search_slope(slope[0], slope[1], x, y)

    return count


max_asteroids_seen = 0
max_asteroid = -1, -1

for y in range(0, max_y):
    for x in range(0, max_x):

        if asteroid_map[x][y] == '#':
            asteroids_seen = search_for_asteroids(x, y)

            if (asteroids_seen > max_asteroids_seen):
                max_asteroids_seen = asteroids_seen
                max_asteroid = x, y

print(max_asteroids_seen)
print(max_asteroid)
