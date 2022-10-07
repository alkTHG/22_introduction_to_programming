def trace1(f):
    def traced(x):
        # 4. traced body executed
        print("calling", f, "with argument", x)
        return f(x)
    # 2. traced(x) returned
    return traced

# 1. executes trace1(f)
@trace1
def square(n):
    return n * n

# @trace1 decorator equivalent to:
# square = trace1(square)

# 3. execution triggers returned traced(9)
print(square(9))




