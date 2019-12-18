import math

# strip \n's out of strings
asteroid_map = ['###..#########.#####.', '.####.#####..####.#.#', '.###.#.#.#####.##..##', '##.####.#.###########', '###...#.####.#.#.####', '#.##..###.########...', '#.#######.##.#######.', '.#..#.#..###...####.#', '#######.##.##.###..##', '#.#......#....#.#.#..',
                '######.###.#.#.##...#', '####.#...#.#######.#.', '.######.#####.#######', '##.##.##.#####.##.#.#', '###.#######..##.#....', '###.##.##..##.#####.#', '##.########.#.#.#####', '.##....##..###.#...#.', '#..#.####.######..###', '..#.####.############', '..##...###..#########']

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
            positive_x_positive_y_slopes.append([(x, y), True])
            positive_x_negative_y_slopes.append([(x, -y), True])
            negative_x_positive_y_slopes.append([(-x, y), True])
            negative_x_negative_y_slopes.append([(-x, -y), True])
            slopeDict[x / y] = True


start_x = 11
start_y = 11

asteroid_map[start_x][start_y] = '.'


def search_slope(run, rise):

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


destroyed_asteroids = []


def search_for_asteroids(x, y):

    for slope in all_slopes:
        asteroid = search_slope(slope[0][0], slope[0][1])

        if asteroid is None:
            slope[1] = False
        else:
            asteroid_map[asteroid[0]][asteroid[1]] = '.'
            destroyed_asteroids.append((asteroid[0], asteroid[1]))


# get the slopes in the order we want to traverse them
positive_x_negative_y_slopes = sorted(
    positive_x_negative_y_slopes, key=lambda x: -(x[0][0] / x[0][1]))
positive_x_positive_y_slopes = sorted(
    positive_x_positive_y_slopes, key=lambda x: (x[0][0] / x[0][1]))
negative_x_positive_y_slopes = sorted(
    negative_x_positive_y_slopes, key=lambda x: -(x[0][0] / x[0][1]))
negative_x_negative_y_slopes = sorted(
    negative_x_negative_y_slopes, key=lambda x: -(x[0][0] / x[0][1]))


# put them all in one list in the order needed to travers
# down, quad 4, right, quad 1, up, quad 2, left, quad 3
all_slopes = [[(0, -1, None), True]]
all_slopes.extend(positive_x_negative_y_slopes)
all_slopes.append([(1, 0, None), True])
all_slopes.extend(positive_x_positive_y_slopes)
all_slopes.append([(0, 1, None), True])
all_slopes.extend(negative_x_positive_y_slopes)
all_slopes.append([(-1, 0, None), True])
all_slopes.extend(negative_x_negative_y_slopes)


def asteroids_left():
    for row in asteroid_map:
        if '#' in row:
            return True
    return False


while(asteroids_left()):
    search_for_asteroids(x, y)
    all_slopes = [slope for slope in all_slopes if slope[1] is True]

print(destroyed_asteroids[199])
