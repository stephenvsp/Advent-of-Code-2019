import math

# strip \n's out of strings
# asteroid_map = ['###..#########.#####.', '.####.#####..####.#.#', '.###.#.#.#####.##..##', '##.####.#.###########', '###...#.####.#.#.####', '#.##..###.########...', '#.#######.##.#######.', '.#..#.#..###...####.#', '#######.##.##.###..##', '#.#......#....#.#.#..','######.###.#.#.##...#', '####.#...#.#######.#.', '.######.#####.#######', '##.##.##.#####.##.#.#', '###.#######..##.#....', '###.##.##..##.#####.#', '##.########.#.#.#####', '.##....##..###.#...#.', '#..#.####.######..###', '..#.####.############', '..##...###..#########']

# test map
asteroid_map = ['.#..##.###...#######', '##.############..##.', '.#.######.########.#', '.###.#######.####.#.', '#####.##.#.##.###.##', '..#####..#.#########', '####################', '#.####....###.#.#.##', '##.#################', '#####.##.###..####..',
                '..######..##.#######', '####.##.####...##..#', '.#####..#.######.###', '##...#.##########...', '#.##########.#######', '.####.#.###.###.#.##', '....##.##.###..#####', '.#.#.###########.###', '#.#.#.#####.####.###', '###.##.####.##.#..##']

max_x = len(asteroid_map[0])
max_y = len(asteroid_map)

# flip x and y's so it makes sense with coordinates
asteroid_map = [[asteroid_map[y][x]
                 for y in range(0, max_y)] for x in range(0, max_x)]

slopes = []
slopeDict = {}

for x in range(1, max_x):
    for y in range(1, max_y):
        if (y / x) not in slopeDict.keys():
            slopes.append((x, y, y / x))
            slopes.append((-x, y, -y / x))
            slopeDict[y / x] = True


slopes.append((1, 0, 0))

# the order of slopes the astroid destroyer will go through
slopes = sorted(slopes, key=lambda x: -x[2])


def is_inbounds(my_x, my_y):

    if (my_x < 0 or my_x >= max_x):
        return False

    if (my_y < 0 or my_y >= max_y):
        return False

    return True


def asteroids_left(asteroid_map):
    for row in asteroid_map:
        if '#' in row:
            return True

    return False


destroyed_asteroids = []

x = 11
y = 13

while(asteroids_left(asteroid_map)):
    # GO UP
    curr_x = x
    curr_y = y + 1
    while (is_inbounds(curr_x, curr_y)):
        if asteroid_map[curr_x][curr_y] == '#':
            destroyed_asteroids.append((curr_x, curr_y))
            asteroid_map[curr_x][curr_y] = '.'
            break
        curr_y += 1

    # go through slopes
    # right side of map
    for slope in slopes:
        run = slope[0]
        rise = slope[1]

        if slope[2] > 0:
            # go up positive slopes
            curr_x = x + run
            curr_y = y + rise

            while(is_inbounds(curr_x, curr_y)):
                if asteroid_map[curr_x][curr_y] == '#':
                    destroyed_asteroids.append((curr_x, curr_y))
                    asteroid_map[curr_x][curr_y] = '.'
                    break
                curr_x += run
                curr_y += rise

        elif slope[2] == 0:
            # go right
            curr_x = x + 1
            curr_y = y

            while (is_inbounds(curr_x, curr_y)):
                if asteroid_map[curr_x][curr_y] == '#':
                    destroyed_asteroids.append((curr_x, curr_y))
                    asteroid_map[curr_x][curr_y] = '.'
                    break
                curr_x += 1

        elif slope[2] < 0:
            # go down the negative slopes
            curr_x = x - run
            curr_y = y - rise

            while(is_inbounds(curr_x, curr_y)):
                if asteroid_map[curr_x][curr_y] == '#':
                    destroyed_asteroids.append((curr_x, curr_y))
                    asteroid_map[curr_x][curr_y] = '.'
                    break
                curr_x -= run
                curr_y -= rise

    # go down
    curr_x = x
    curr_y = y - 1
    while (is_inbounds(curr_x, curr_y)):
        if asteroid_map[curr_x][curr_y] == '#':
            destroyed_asteroids.append((curr_x, curr_y))
            asteroid_map[curr_x][curr_y] = '.'
            break
        curr_y -= 1

    # left side of map
    for slope in slopes:
        run = slope[0]
        rise = slope[1]

        if (slope[2] > 0):
            # go down positive ones
            curr_x = x - run
            curr_y = y - rise

            while(is_inbounds(curr_x, curr_y)):
                if asteroid_map[curr_x][curr_y] == '#':
                    destroyed_asteroids.append((curr_x, curr_y))
                    asteroid_map[curr_x][curr_y] = '.'
                    break
                curr_x -= run
                curr_y -= rise

        elif (slope[2] == 0):
            # go left
            curr_x = x - 1
            curr_y = y
            while (is_inbounds(curr_x, curr_y)):
                if asteroid_map[curr_x][curr_y] == '#':
                    destroyed_asteroids.append((curr_x, curr_y))
                    asteroid_map[curr_x][curr_y] = '.'
                    break
                curr_x -= 1

        elif (slope[2] < 0):
            # go up negative slopes
            curr_x = x + run
            curr_y = y + rise

            while(is_inbounds(curr_x, curr_y)):
                if asteroid_map[curr_x][curr_y] == '#':
                    destroyed_asteroids.append((curr_x, curr_y))
                    asteroid_map[curr_x][curr_y] = '.'
                    break
                curr_x += run
                curr_y += rise

print(destroyed_asteroids[199])
