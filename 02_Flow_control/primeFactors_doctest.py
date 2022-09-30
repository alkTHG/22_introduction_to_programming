# terminal commands below for doctest
# python3 -m doctest primeFactors_doctest.py

def checkprime(num):
    """prints the prime numbers of num

    >>> checkprime(24)
    2 is a prime factor
    2 is a prime factor
    2 is a prime factor
    3 is a prime factor
    >>> checkprime(11)
    11 is a prime factor
    """
    div = 2
    while div <= num:
        if num % div == 0:
            print(div, "is a prime factor")
            num = num / div
        else:
            div = div + 1


checkprime(24)


