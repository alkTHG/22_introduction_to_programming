# not sure return does not work???
# def sum_of_factorials(n):
#     sum = 1
#
#     def factorial(n, sum):
#         if n > 0:
#             sum = n * sum
#             n -= 1
#             factorial(n, sum)
#         else:
#             print("the sum is", sum)
#             return sum
#
#     factorial(n, sum)

def sum_of_factorials(n):
    sum = 1
    while n > 0:
        sum *= n
        n -= 1
    else:
        return sum


def sum_digits(n):
    sum = 0
    while n != 0:
        sum = sum + (n % 10)
        n = n // 10
    return sum


print(sum_digits(sum_of_factorials(100)))


