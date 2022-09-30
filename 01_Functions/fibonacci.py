def fibonacci(a):
    # function is defined not executed here
    def fibonacci_recursive(a, b, c):
        if a == 0:
            # b is returned, recursion completed
            return b
        else:
            # second and all subsequent executions here until a == 0
            return fibonacci_recursive(a - 1, b + c, b)
    # function is executed here first
    return fibonacci_recursive(a, 0, 1)


print(fibonacci(6))
