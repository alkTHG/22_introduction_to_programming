def print_sums(x):
    print(x)

    def next_sum(y):
        return print_sums(x + y)

    return next_sum


# print_sums(1)(3)(4)

def sum(x):
    return x
    def sums(y):
        return sum(x + y)

    return sums


print(sum(2)(3))
# sum(2)(3)
