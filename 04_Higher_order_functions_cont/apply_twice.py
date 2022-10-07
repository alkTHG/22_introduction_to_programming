# Higher-order function: A function that takes a function as an argument
# value or a function that returns a function as a return value

def apply_twice(f, x):
    return f(f(x))


def square(x):
    return x * x


print(apply_twice(square, 2))
