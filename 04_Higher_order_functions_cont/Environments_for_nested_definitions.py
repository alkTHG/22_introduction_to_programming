def make_adder(n):
    """return a function which adds N to its argument"""

    def adder(x):
        return n + x

    return adder


# executed fist, n is set to 3 in parent frame
add_three = make_adder(3)

# executed second, retuns adder in child frame, uses n=3 from parent frame
print(add_three(4))
