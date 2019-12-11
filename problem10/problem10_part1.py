import math

with open('problem10_input.txt') as file:
    asteroid_map = file.readlines()

# strip \n's out of strings
asteroid_map = [asteroid.strip() for asteroid in asteroid_map]

max_x = len(asteroid_map[0])
max_y = len(asteroid_map)

# flip x and y's so it makes sense with coordinates
asteroid_map = [[asteroid_map[y][x]
                 for y in range(0, max_y)] for x in range(0, max_x)]

max_asteroids_seen = 0
max_asteroid = -1, -1

max_degrees = 180
increment = 1

slopes = []

for degree in range(0, max_degrees, 1):
    radians = degree * math.pi / 180

    x = math.cos(radians)
    y = math.sin(radians)

    if degree == 90:
        slopes.append('UNDEFINED')
    elif degree == 270:
        slopes.append('UNDEFINED')
    else:
        slopes.append(y / x)

print(slopes)


def search_for_asteroids(x, y):
    return 0


# for y in range(0, max_y):
    # for x in range(0, max_x):

    #     if asteroid_map[x][y] == '#':
    #         asteroids_seen = search_for_asteroids(x, y)

    #         if (asteroids_seen > max_asteroids_seen):
    #             max_asteroids = x, y


print(search_for_asteroids(0, 0))
