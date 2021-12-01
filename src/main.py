import math
from timeit import default_timer as timer
import sys

# with open('maze1.txt', 'w') as outfile:
#     outfile.write('0\n')
#     outfile.write('xxxxxxxxxxxxxxxxxxxxxx\n')
#     outfile.write('x   x   xx xx        x\n')
#     outfile.write('x     x     xxxxxxxxxx\n')
#     outfile.write('x x   xxx  xxxx xxx xx\n')
#     outfile.write('  x   x x xx   xxxx Sx\n')
#     outfile.write('x          xxx xx    x\n')
#     outfile.write('xxxxxxx x      xx  x x\n')
#     outfile.write('xxxxxxxxx  x x  xx   x\n')
#     outfile.write('x          x x  x x  x\n')
#     outfile.write('xxxxx x  x x x       x\n')
#     outfile.write('xxxxxxxxxxxxxxxxxxxxxx')
#
# with open('maze2.txt', 'w') as outfile:
#     outfile.write('0\n')
#     outfile.write('xxxxxxxxxxxxxxxxxxxxxxx\n')
#     outfile.write('  x   x   x   x   x   x\n')
#     outfile.write('x x x x x x x x x x x x\n')
#     outfile.write('x x x x x x x x x x x x\n')
#     outfile.write('x x x x x x x x x x x x\n')
#     outfile.write('x x x x x x x x x x x x\n')
#     outfile.write('x x x x x x x x x x x x\n')
#     outfile.write('x x x x x x x x x x x x\n')
#     outfile.write('x x x x x x x x x x x x\n')
#     outfile.write('x   x   x   x   x   xSx\n')
#     outfile.write('xxxxxxxxxxxxxxxxxxxxxxx')
#
# with open('maze3.txt', 'w') as outfile:
#     outfile.write('0\n')
#     outfile.write('x xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n')
#     outfile.write('x x   x   x   xx                       x\n')
#     outfile.write('x x x x x x x xx x xxxxxxxxxxxxxxxxxxx x\n')
#     outfile.write('x x x x x x x x  x x                   x\n')
#     outfile.write('x x x x x x x xx x x xxxxxxxxxxxxxxxxxxx\n')
#     outfile.write('x   x x x x x xx x x                   x\n')
#     outfile.write('x xxx   x   x     x xxxxxxxxxxxxxxxxxx x\n')
#     outfile.write('x  xxxxxxxxxxxxx xx x                  x\n')
#     outfile.write('x x    x  x    xxxx x xx  x xxxxxxxxxxxx\n')
#     outfile.write('xxx xx x  x xx      x    xx xx    x  xxx\n')
#     outfile.write('x           x x xx    xx xxx           x\n')
#     outfile.write('x  xxxxxxxxxxxxx              xxx  x   x\n')
#     outfile.write('x                xxxxxxxxxx xxx xx xx  x\n')
#     outfile.write('x xxxxxxxxxxxxxxxxx       x   x x      x\n')
#     outfile.write('x                xx xxxxx xxxxx xxxxx  x\n')
#     outfile.write('x xxxxxxxxxxxxxx  +   xxx              x\n')
#     outfile.write('x x            x  xxx xx  xxx xxxxxxxxxx\n')
#     outfile.write('x x xxxx xx xx xx xxx xxxxxxx          x\n')
#     outfile.write('x xxxxxx xx xx xx xxx       xxxxxxxxxxxx\n')
#     outfile.write('x              xx    xxxxx            Sx\n')
#     outfile.write('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n')
#
# with open('maze4.txt', 'w') as outfile:
#     outfile.write('0\n')
#     outfile.write('xxxxxxxxxxxxxxxxxxxxxxx\n')
#     outfile.write('  xS  x   x           x\n')
#     outfile.write('x xx  x x x x x x xxx x\n')
#     outfile.write('x x   x x x xxxxx   x x\n')
#     outfile.write('x x xxx x x     xxx x x\n')
#     outfile.write('x x     x   x x   x x x\n')
#     outfile.write('x xxx xxxxx x    xxxx x\n')
#     outfile.write('x x x x x   x x  x    x\n')
#     outfile.write('x x xxx xxxxxxx x x x x\n')
#     outfile.write('x                   x x\n')
#     outfile.write('xxxxxxxxxxxxxxxxxxxxxxx')
#
# with open('maze5.txt', 'w') as outfile:
#     outfile.write('0\n')
#     outfile.write('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n')
#     outfile.write('x            x   x               x      x\n')
#     outfile.write('x xx x x x x x x x x x x x x x x x x xx x\n')
#     outfile.write('x  x x x  x  x x x  x  x x x  x  x x x  x\n')
#     outfile.write('x x  x  x   x  x  x   x  x  x   x  x  x x\n')
#     outfile.write('xx  x x  x x  x x  x x  x x  x x  x x  xx\n')
#     outfile.write('x  x   x  x  x   x  x  x   x  x  x   x  x\n')
#     outfile.write('x x  x  x x x  x  x x x  x  x x x  x  x x\n')
#     outfile.write('x x x x x x x x x x x x x x x x x x x x x\n')
#     outfile.write('S x         x         x         x       x\n')
#     outfile.write('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx x')
#
# with open('maze6.txt', 'w') as outfile:
#     outfile.write('5\n')
#     outfile.write('3 12 -5\n')
#     outfile.write('2 7 -10\n')
#     outfile.write('4 3 -5\n')
#     outfile.write('9 7 -5\n')
#     outfile.write('2 2 -7\n')
#     outfile.write('xxxxxxxxxxxxxxxxxxxxxx\n')
#     outfile.write('x   x   xx xx        x\n')
#     outfile.write('x     x+    xxxxxxxxxx\n')
#     outfile.write('x x   xxx  x+ x xxx xx\n')
#     outfile.write('  x   x x xx   xxxx Sx\n')
#     outfile.write('x          xxx xx    x\n')
#     outfile.write('xxxxxxx x      xx  x x\n')
#     outfile.write('xxxxxxxxx  x x  xx   x\n')
#     outfile.write('x          x x  x x  x\n')
#     outfile.write('xxxxx x  x x x       x\n')
#     outfile.write('xxxxxxxxxxxxxxxxxxxxxx')
#
# with open('maze7.txt', 'w') as outfile:
#     outfile.write('2\n')
#     outfile.write('9 18 -10\n')
#     outfile.write('15 18 -10\n')
#     outfile.write('x xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n')
#     outfile.write('x x   x   x   xx                       x\n')
#     outfile.write('x x x x x x x xx x xxxxxxxxxxxxxxxxxxx x\n')
#     outfile.write('x x x x x x x x  x x                   x\n')
#     outfile.write('x x x x x x x xx x x xxxxxxxxxxxxxxxxxxx\n')
#     outfile.write('x   x x x x x xx x x                   x\n')
#     outfile.write('x xxx   x   x     x xxxxxxxxxxxxxxxxxx x\n')
#     outfile.write('x  xxxxxxxxxxxxx xx x                  x\n')
#     outfile.write('x x    x  x    xxxx x xx  x xxxxxxxxxxxx\n')
#     outfile.write('xxx xx x  x xx      x    xx xx    x  xxx\n')
#     outfile.write('x           x x xx    xx xxx           x\n')
#     outfile.write('x  xxxxxxxxxxxxx              xxx  x   x\n')
#     outfile.write('x                xxxxxxxxxx xxx xx xx  x\n')
#     outfile.write('x xxxxxxxxxxxxxxxxx       x   x x      x\n')
#     outfile.write('x                xx xxxxx xxxxx xxxxx  x\n')
#     outfile.write('x xxxxxxxxxxxxxx      xxx              x\n')
#     outfile.write('x x            x  xxx xx  xxx xxxxxxxxxx\n')
#     outfile.write('x x xxxx xx xx xx xxx xxxxxxx          x\n')
#     outfile.write('x xxxxxx xx xx xx xxx       xxxxxxxxxxxx\n')
#     outfile.write('x              xx    xxxxx            Sx\n')
#     outfile.write('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n')
#
# with open('maze8.txt', 'w') as outfile:
#     outfile.write('5\n')
#     outfile.write('9 18 -10\n')
#     outfile.write('15 18 -10\n')
#     outfile.write('8 8 -5\n')
#     outfile.write('7 21 -10\n')
#     outfile.write('9 35 -5\n')
#     outfile.write('x xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n')
#     outfile.write('x x   x   x   xx                       x\n')
#     outfile.write('x x x x x x x xx x xxxxxxxxxxxxxxxxxxx x\n')
#     outfile.write('x x x x x x x x  x x                   x\n')
#     outfile.write('x x x x x x x xx x x xxxxxxxxxxxxxxxxxxx\n')
#     outfile.write('x   x x x x x xx x x                   x\n')
#     outfile.write('x xxx   x   x     x xxxxxxxxxxxxxxxxxx x\n')
#     outfile.write('x  xxxxxxxxxxxxx xx x+                 x\n')
#     outfile.write('x x    x+ x    xxxx x xx  x xxxxxxxxxxxx\n')
#     outfile.write('xxx xx x  x xx    + x    xx xx    x  xxx\n')
#     outfile.write('x           x x xx    xx xxx           x\n')
#     outfile.write('x  xxxxxxxxxxxxx              xxx  x   x\n')
#     outfile.write('x                xxxxxxxxxx xxx xx xx  x\n')
#     outfile.write('x xxxxxxxxxxxxxxxxx       x   x x      x\n')
#     outfile.write('x                xx xxxxx xxxxx xxxxx  x\n')
#     outfile.write('x xxxxxxxxxxxxxx  +   xxx              x\n')
#     outfile.write('x x            x  xxx xx  xxx xxxxxxxxxx\n')
#     outfile.write('x x xxxx xx xx xx xxx xxxxxxx          x\n')
#     outfile.write('x xxxxxx xx xx xx xxx       xxxxxxxxxxxx\n')
#     outfile.write('x              xx    xxxxx            Sx\n')
#     outfile.write('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n')
#
# with open('maze9.txt', 'w') as outfile:
#     outfile.write('10\n')
#     outfile.write('9 18 -10\n')
#     outfile.write('15 18 -10\n')
#     outfile.write('1 38 -10\n')
#     outfile.write('8 5 -10\n')
#     outfile.write('19 9 -10\n')
#     outfile.write('3 33 -10\n')
#     outfile.write('6 2 -10\n')
#     outfile.write('7 21 -10\n')
#     outfile.write('13 31 -10\n')
#     outfile.write('8 28 -10\n')
#     outfile.write('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n')
#     outfile.write('  x   x   x   xx       x x            +x\n')
#     outfile.write('x x x x x x x xx x x xxxxxx x   xxxxxx x\n')
#     outfile.write('x x x x x x x x  x x   xxx   xxx + xxx x\n')
#     outfile.write('x x x x x x x xx x x x  x  x  x  x  x  x\n')
#     outfile.write('x   x x x x x xx x x xx   xxx   xxx    x\n')
#     outfile.write('x +xx   x   x     x xxxxxxxxxxxxxxxxxx x\n')
#     outfile.write('x  x xx x xx xx  xx x+                 x\n')
#     outfile.write('x x  + x xx    xxxx x xx  x +xxxxxxxxxxx\n')
#     outfile.write('xxx xx    x xx    + x    xx xx    x  xxx\n')
#     outfile.write('x           x x xx    xx xxx           x\n')
#     outfile.write('x  xxx xx xxxxxx              xxx  x   x\n')
#     outfile.write('x  x   x         xxxxxxxxxx xxx xx xx  x\n')
#     outfile.write('x xx xxxxxxxxxxxxxx       x   x+       x\n')
#     outfile.write('x                xx xxxxx xxxxx xxxxx  x\n')
#     outfile.write('xxx  xxxxxxxxxxx  +   xxx              x\n')
#     outfile.write('x                 xxx xx  xxx xxxxxxxxxx\n')
#     outfile.write('x x x xx xx  xxxx xxx xxxxxxx          x\n')
#     outfile.write('x x xxxx xx x  xx xxx       xxxxxxxxxxxx\n')
#     outfile.write('x x      +     xx    xxxxx            Sx\n')
#     outfile.write('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n')


import matplotlib.pyplot as plot


def visualize_maze(matrix, bonus, start, end, route=None):
    """
    Args:
      1. matrix: The matrix read from the input file,
      2. bonus: The array of bonus points,
      3. start, end: The starting and ending points,
      4. route: The route from the starting point to the ending one, defined by an array of (x, y), e.g. route = [(1, 2), (1, 3), (1, 4)]
    """
    # 1. Define walls and array of direction based on the route
    walls = [(i, j) for i in range(len(matrix)) for j in range(len(matrix[0])) if matrix[i][j] == 'x']

    if route:
        direction = []
        for i in range(1, len(route)):
            if route[i][0] - route[i - 1][0] > 0:
                direction.append('v')  # ^
            elif route[i][0] - route[i - 1][0] < 0:
                direction.append('^')  # v
            elif route[i][1] - route[i - 1][1] > 0:
                direction.append('>')
            else:
                direction.append('<')

        direction.pop(0)

    # 2. Drawing the map
    ax = plot.figure(dpi=100).add_subplot(111)

    for i in ['top', 'bottom', 'right', 'left']:
        ax.spines[i].set_visible(False)

    plot.scatter([i[1] for i in walls], [-i[0] for i in walls],
                 marker='X', s=100, color='black')

    plot.scatter([i[1] for i in bonus], [-i[0] for i in bonus],
                 marker='P', s=100, color='green')

    plot.scatter(start[1], -start[0], marker='*',
                 s=100, color='gold')

    if route:
        for i in range(len(route) - 2):
            plot.scatter(route[i + 1][1], -route[i + 1][0],
                         marker=direction[i], color='silver')

    plot.text(end[1], -end[0], 'EXIT', color='red',
              horizontalalignment='center',
              verticalalignment='center')
    plot.xticks([])
    plot.yticks([])
    plot.show()

    print(f'Starting point (x, y) = {start[0], start[1]}')
    print(f'Ending point (x, y) = {end[0], end[1]}')

    for _, point in enumerate(bonus):
        print(f'Bonus point at position (x, y) = {point[0], point[1]} with point {point[2]}')


def read_file(file_name: str = 'maze.txt'):
    f = open(file_name, 'r')
    n_bonus_points = int(next(f)[:-1])
    bonus_points = []
    for i in range(n_bonus_points):
        x, y, reward = map(int, next(f)[:-1].split(' '))
        bonus_points.append((x, y, reward))

    text = f.read()
    matrix = [list(i) for i in text.splitlines()]
    f.close()

    return bonus_points, matrix


def breadth_first_search(matrix, start, end):
    frontier = [start]
    visited = [start]
    path = {}
    curr_point = None

    while len(frontier) > 0:
        curr_point = frontier.pop(0)
        if curr_point == end:
            break
        for direction in ['up', 'down', 'left', 'right']:
            if direction == 'up':
                next_point = (curr_point[0] - 1, curr_point[1])
            elif direction == 'down':
                next_point = (curr_point[0] + 1, curr_point[1])
            elif direction == 'left':
                next_point = (curr_point[0], curr_point[1] - 1)
            elif direction == 'right':
                next_point = (curr_point[0], curr_point[1] + 1)
            if next_point in visited:
                continue
            try:
                if matrix[next_point[0]][next_point[1]] != 'x':
                    frontier.append(next_point)
                    visited.append(next_point)
                    path[next_point] = curr_point
            except IndexError:
                pass

    if curr_point != end:
        return None, 0

    cost = 0

    route = []
    curr_point = end
    while curr_point != start:
        route.append(curr_point)
        curr_point = path[curr_point]
        cost += 1
    route.append(curr_point)
    return route[::-1], cost


def depth_first_search(matrix, start, end):
    frontier = [start]
    visited = [start]
    path = {}
    curr_point = None

    while len(frontier) > 0:
        curr_point = frontier.pop()
        if curr_point == end:
            break
        for direction in ['up', 'down', 'left', 'right']:
            if direction == 'up':
                next_point = (curr_point[0] - 1, curr_point[1])
            elif direction == 'down':
                next_point = (curr_point[0] + 1, curr_point[1])
            elif direction == 'left':
                next_point = (curr_point[0], curr_point[1] - 1)
            elif direction == 'right':
                next_point = (curr_point[0], curr_point[1] + 1)
            if next_point in visited:
                continue
            try:
                if matrix[next_point[0]][next_point[1]] != 'x':
                    frontier.append(next_point)
                    visited.append(next_point)
                    path[next_point] = curr_point
            except IndexError:
                pass

    if curr_point != end:
        return None, 0

    cost = 0

    route = []
    curr_point = end
    while curr_point != start:
        route.append(curr_point)
        curr_point = path[curr_point]
        cost += 1
    route.append(curr_point)
    return route[::-1], cost


def heuristic_1(curr_point, end):
    return abs(curr_point[0] - end[0]) + abs(curr_point[1] - end[1])


def heuristic_2(curr_point, end):
    return math.sqrt((curr_point[0] - end[0]) ** 2 + (curr_point[1] - end[1]) ** 2)


def greedy_search(matrix, bonus_points, start, end):
    open = [(0, start)]
    closed = []
    path = {}
    curr_point = None
    curr = None

    while len(open) > 0:
        curr = open.pop(0)
        curr_point = curr[1]
        closed.append(curr_point)
        if curr_point == end:
            break
        for direction in ['up', 'down', 'left', 'right']:
            if direction == 'up':
                next_point = (curr_point[0] - 1, curr_point[1])
            elif direction == 'down':
                next_point = (curr_point[0] + 1, curr_point[1])
            elif direction == 'left':
                next_point = (curr_point[0], curr_point[1] - 1)
            elif direction == 'right':
                next_point = (curr_point[0], curr_point[1] + 1)
            if next_point in closed:
                continue
            try:
                if matrix[next_point[0]][next_point[1]] != 'x':
                    weight = 0
                    for bonus_point in bonus_points:
                        if next_point[0] == bonus_point[0] and next_point[1] == bonus_point[1]:
                            weight = bonus_point[2]
                            break
                    f = weight + heuristic_1(curr_point, end)
                    for point in open:
                        if point[1] == next_point:
                            if point[0] <= f:
                                raise IndexError
                    open.append((f, next_point))
                    path[next_point] = curr_point
                    open.sort()
            except IndexError:
                pass

    if curr_point != end:
        return None, 0

    cost = 0

    route = []
    curr_point = end
    while curr_point != start:
        route.append(curr_point)
        curr_point = path[curr_point]
        weight = 1
        for bonus_point in bonus_points:
            if curr_point[0] == bonus_point[0] and curr_point[1] == bonus_point[1]:
                weight = bonus_point[2]
                break
        cost += weight
    route.append(curr_point)
    return route[::-1], cost


def a_star_search(matrix, bonus_points, start, end):
    open = [(0, start)]
    closed = []
    path = {}
    curr_point = None
    curr = None

    while len(open) > 0:
        curr = open.pop(0)
        curr_point = curr[1]
        for bonus_point in bonus_points:
            if curr_point[0] == bonus_point[0] and curr_point[1] == bonus_point[1]:
                break
        closed.append(curr_point)
        if curr_point == end:
            break
        for direction in ['up', 'down', 'left', 'right']:
            if direction == 'up':
                next_point = (curr_point[0] - 1, curr_point[1])
            elif direction == 'down':
                next_point = (curr_point[0] + 1, curr_point[1])
            elif direction == 'left':
                next_point = (curr_point[0], curr_point[1] - 1)
            elif direction == 'right':
                next_point = (curr_point[0], curr_point[1] + 1)
            if next_point in closed:
                continue
            try:
                if matrix[next_point[0]][next_point[1]] != 'x':
                    weight = 0
                    for bonus_point in bonus_points:
                        if next_point[0] == bonus_point[0] and next_point[1] == bonus_point[1]:
                            weight = bonus_point[2]
                            break
                    if curr_point == start:
                        f = 1 + heuristic_1(next_point, end)
                    else:
                        f = weight + curr[0] - heuristic_1(curr_point, end) + 1 + heuristic_1(next_point, end)
                    for point in open:
                        if point[1] == next_point:
                            if point[0] <= f:
                                raise IndexError
                    open.append((f, next_point))
                    path[next_point] = curr_point
                    open.sort()
            except IndexError:
                pass

    if curr_point != end:
        return None, 0

    cost = 0

    route = []
    curr_point = end
    while curr_point != start:
        route.append(curr_point)
        curr_point = path[curr_point]
        weight = 1
        for bonus_point in bonus_points:
            if curr_point[0] == bonus_point[0] and curr_point[1] == bonus_point[1]:
                weight = bonus_point[2]
                break
        cost += weight
    route.append(curr_point)
    return route[::-1], cost

def a_star_search_2(matrix, bonus_points, start, end):
    open = [(0, start)]
    closed = []
    path = {}
    curr_point = None
    curr = None

    while len(open) > 0:
        curr = open.pop(0)
        curr_point = curr[1]
        for bonus_point in bonus_points:
            if curr_point[0] == bonus_point[0] and curr_point[1] == bonus_point[1]:
                break
        closed.append(curr_point)
        if curr_point == end:
            break
        for direction in ['up', 'down', 'left', 'right']:
            if direction == 'up':
                next_point = (curr_point[0] - 1, curr_point[1])
            elif direction == 'down':
                next_point = (curr_point[0] + 1, curr_point[1])
            elif direction == 'left':
                next_point = (curr_point[0], curr_point[1] - 1)
            elif direction == 'right':
                next_point = (curr_point[0], curr_point[1] + 1)
            if next_point in closed:
                continue
            try:
                if matrix[next_point[0]][next_point[1]] != 'x':
                    weight = 0
                    for bonus_point in bonus_points:
                        if next_point[0] == bonus_point[0] and next_point[1] == bonus_point[1]:
                            weight = bonus_point[2]
                            break
                    if curr_point == start:
                        f = 1 + heuristic_2(next_point, end)
                    else:
                        f = weight + curr[0] - heuristic_2(curr_point, end) + 1 + heuristic_2(next_point, end)
                    for point in open:
                        if point[1] == next_point:
                            if point[0] <= f:
                                raise IndexError
                    open.append((f, next_point))
                    path[next_point] = curr_point
                    open.sort()
            except IndexError:
                pass

    if curr_point != end:
        return None, 0

    cost = 0

    route = []
    curr_point = end
    while curr_point != start:
        route.append(curr_point)
        curr_point = path[curr_point]
        weight = 1
        for bonus_point in bonus_points:
            if curr_point[0] == bonus_point[0] and curr_point[1] == bonus_point[1]:
                weight = bonus_point[2]
                break
        cost += weight
    route.append(curr_point)
    return route[::-1], cost

def dijkstra_algorithm(matrix, bonus_points, start, end):
    open = [(0, start)]
    visited = []
    path = {}
    curr_point = None
    curr = None

    while len(open) > 0:
        curr = open.pop(0)
        curr_point = curr[1]
        for bonus_point in bonus_points:
            if curr_point[0] == bonus_point[0] and curr_point[1] == bonus_point[1]:
                break
        visited.append(curr_point)
        if curr_point == end:
            break
        for direction in ['up', 'down', 'left', 'right']:
            if direction == 'up':
                next_point = (curr_point[0] - 1, curr_point[1])
            elif direction == 'down':
                next_point = (curr_point[0] + 1, curr_point[1])
            elif direction == 'left':
                next_point = (curr_point[0], curr_point[1] - 1)
            elif direction == 'right':
                next_point = (curr_point[0], curr_point[1] + 1)
            if next_point in visited:
                continue
            try:
                if matrix[next_point[0]][next_point[1]] != 'x':
                    cost = 1
                    for bonus_point in bonus_points:
                        if next_point[0] == bonus_point[0] and next_point[1] == bonus_point[1]:
                            cost = bonus_point[2]
                            break
                    d = curr[0] + cost
                    for i in range(len(open)):
                        if open[i][1] == next_point:
                            if open[i][0] > d:
                                open.pop(i)
                                break
                    open.append((d, next_point))
                    path[next_point] = curr_point
                    open.sort()
            except IndexError:
                pass

    if curr_point != end:
        return None, 0

    cost = 0

    route = []
    curr_point = end
    while curr_point != start:
        route.append(curr_point)
        curr_point = path[curr_point]
        weight = 1
        for bonus_point in bonus_points:
            if curr_point[0] == bonus_point[0] and curr_point[1] == bonus_point[1]:
                weight = bonus_point[2]
                break
        cost += weight
    route.append(curr_point)
    return route[::-1], cost

fileName = None

if len(sys.argv) < 2:
    fileName = '../test/maze1.txt'
else:
    fileName = sys.argv[1]

bonus_points, matrix = read_file(fileName)
print(f'The height of the matrix: {len(matrix)}')
print(f'The width of the matrix: {len(matrix[0])}')

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == 'S':
            start = (i, j)

        elif matrix[i][j] == ' ':
            if (i == 0) or (i == len(matrix) - 1) or (j == 0) or (j == len(matrix[0]) - 1):
                end = (i, j)

        else:
            pass

print('-> Breadth First Search')

start_time = timer()
route, cost = breadth_first_search(matrix, start, end)
end_time = timer()
if route is None:
    print('No solution could be found')
else:
    print(f'Cost: {cost}')
    print(f'Time: {end_time - start_time}')
visualize_maze(matrix, bonus_points, start, end, route)

print('-> Depth First Search')

start_time = timer()
route, cost = depth_first_search(matrix, start, end)
end_time = timer()
if route is None:
    print('No solution could be found')
else:
    print(f'Cost: {cost}')
    print(f'Time: {end_time - start_time}')
visualize_maze(matrix, bonus_points, start, end, route)

print('-> Greedy Best First Search')

start_time = timer()
route, cost = greedy_search(matrix, bonus_points, start, end)
end_time = timer()
if route is None:
    print('No solution could be found')
else:
    print(f'Cost: {cost}')
    print(f'Time: {end_time - start_time}')
visualize_maze(matrix, bonus_points, start, end, route)

print('-> A* Search')

start_time = timer()
route, cost = a_star_search(matrix, bonus_points, start, end)
end_time = timer()
if route is None:
    print('No solution could be found')
else:
    print(f'Cost: {cost}')
    print(f'Time: {end_time - start_time}')
visualize_maze(matrix, bonus_points, start, end, route)

# Heuristic 2 A* Algorithm

# start_time = timer()
# route, cost = a_star_search_2(matrix, bonus_points, start, end)
# end_time = timer()
# if route is None:
#     print('No solution could be found')
# else:
#     print(f'Cost: {cost}')
#     print(f'Time: {end_time - start_time}')
# visualize_maze(matrix, bonus_points, start, end, route)

print('-> Dijkstra Algorithm')

start_time = timer()
route, cost = dijkstra_algorithm(matrix, bonus_points, start, end)
end_time = timer()
if route is None:
    print('No solution could be found')
else:
    print(f'Cost: {cost}')
    print(f'Time: {end_time - start_time}')
visualize_maze(matrix, bonus_points, start, end, route)
