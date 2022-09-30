def make_adder(n):

    def adder(x):
        return n + x

    return adder


add10 = make_adder(10)
print(add10(10))
