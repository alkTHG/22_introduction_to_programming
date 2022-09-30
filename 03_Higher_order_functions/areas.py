from math import pi, sqrt
from operator import add, mul, truediv


def area_square(side):
    return calc(side, 1)


def area_circle(radius):
    return calc(radius,pi)


def area_regular_triangle(side):
    return calc(side, (sqrt(3) / 4))


def area_regular_pentagon(side):
    return calc(side,truediv(sqrt(mul(5,(add(5,mul(2,sqrt(5)))))), 4))


def calc(side, const):
    return side ** 2 * const


print(area_square(4), area_circle(4), area_regular_triangle(4), area_regular_pentagon(4))