# recursive version
def factr(n):
    if n == 0:
        return 1
    else:
        return n * factr(n - 1)


# iterative version
def facti(n):
    total, k = 1, 1
    while k <= n:
        total, k = total * k, k + 1
    return total


print(factr(4))
print(facti(4))