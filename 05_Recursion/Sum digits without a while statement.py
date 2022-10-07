def split(n):
    """Split positive n into all but its last digit and its last digit
    """

    return n // 10, n % 10


def sum_of_digits(n):
    """Sum the decimal digits of positive integer n
    >>> sum_of_digits(12345)
    15
    """

    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return sum_of_digits(all_but_last) + last


print(sum_of_digits(13))

# sum of nested lists of integers