def sum_nums(n):
    if n < 1:
        return n
    else:
        return n + sum_nums(n - 1)


print(sum_nums(4))