import math

route = [(1, 0), (1, 1), (2, 1)]


def distance(list):
    travel = 0
    index = 0
    while index < len(list) - 1:
        a = list[index][0] - list[index + 1][0]
        b = list[index][1] - list[index + 1][1]
        c = a ** 2 + b ** 2
        travel += math.sqrt(c)
        index += 1
    print(travel)


distance(route) # => 2

