# example 1
if sqrt(square(a) + square(b)) > 1:
    x = x + sqrt(square(a) + square(b))

# avoid repeating, might be better written as:

hypotenuse = sqrt(square(a) + square(b))
if hypotenuse > 1:
    x = x + hypotenuse

# example 2

def c(x0, y0, x1, y1):
    return 2 * pi * sqrt((x0 - x1) * (x0 - x1) + (y0 - y1) * (y0 - y1))

# better to use descriptive names:

def circumference(x0, y0, x1, y1):
    x_leg = x0 - x1
    y_leg = y0 - y1
    radius = sqrt(x_leg ** 2 + y_leg ** 2)
    return 2 * pi * radius


# n, k, i - Usually integers x, y, z - Usually real numbers f, g, h - Usually functions