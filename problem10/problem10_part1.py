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

slopes = []
slopeDict = {}

for x in range(1, max_x):
    for y in range(1, max_y):
        if (x / y) not in slopeDict.keys():
            slopes.append((x, y))
            slopes.append((-x, y))
            slopeDict[x / y] = True


def is_inbounds(my_x, my_y):

    if (my_x < 0 or my_x >= max_x):
        return False

    if (my_y < 0 or my_y >= max_y):
        return False

    return True


def search_for_asteroids(x, y):
    count = 0

    # up
    curr_x = x
    curr_y = y + 1
    while (is_inbounds(curr_x, curr_y)):
        if asteroid_map[curr_x][curr_y] == '#':
            count += 1
            break
        curr_y += 1

    # down
    curr_x = x
    curr_y = y - 1
    while (is_inbounds(curr_x, curr_y)):
        if asteroid_map[curr_x][curr_y] == '#':
            count += 1
            break
        curr_y -= 1

    # left
    curr_x = x - 1
    curr_y = y
    while (is_inbounds(curr_x, curr_y)):
        if asteroid_map[curr_x][curr_y] == '#':
            count += 1
            break
        curr_x -= 1

    # right
    curr_x = x + 1
    curr_y = y
    while (is_inbounds(curr_x, curr_y)):
        if asteroid_map[curr_x][curr_y] == '#':
            count += 1
            break
        curr_x += 1

    for slope in slopes:
        run = slope[0]
        rise = slope[1]

        # slope is positive
        if rise / run > 0:

            # go up the slope
            curr_x = x + run
            curr_y = y + rise

            while(is_inbounds(curr_x, curr_y)):
                if asteroid_map[curr_x][curr_y] == '#':
                    count += 1
                    break
                curr_x += run
                curr_y += rise

            # go down the slope
            curr_x = x - run
            curr_y = y - rise

            while(is_inbounds(curr_x, curr_y)):
                if asteroid_map[curr_x][curr_y] == '#':
                    count += 1
                    break
                curr_x -= run
                curr_y -= rise

        # slope is negative
        else:
            # go up the slope
            curr_x = x + run
            curr_y = y + rise

            while(is_inbounds(curr_x, curr_y)):
                if asteroid_map[curr_x][curr_y] == '#':
                    count += 1
                    break
                curr_x += run
                curr_y += rise

            # go down the slope
            curr_x = x - run
            curr_y = y - rise

            while(is_inbounds(curr_x, curr_y)):
                if asteroid_map[curr_x][curr_y] == '#':
                    count += 1
                    break
                curr_x -= run
                curr_y -= rise

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
