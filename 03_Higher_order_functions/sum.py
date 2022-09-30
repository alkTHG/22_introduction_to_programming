def pi_sum(start, finish):
    total = 0
    n = start
    while n <= finish:
        total = total + 8 / ((4 * n + 1) * (4 * n + 3))
        n += 1
    return total


print(pi_sum(4, 30))
