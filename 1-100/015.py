width = 20
height = 20
routes = {}


def lattice(x, y):
    paths = 0

    if (x, y) in routes:
        return routes[(x, y)]

    if x == width and y == height:
        paths += 1
        return paths

    if x != width:
        paths += lattice(x + 1, y)
    if y != height:
        paths += lattice(x, y + 1)

    routes[(x, y)] = paths

    return paths


print(lattice(0, 0))
