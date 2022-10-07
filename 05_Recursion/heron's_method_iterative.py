def herons(num, guess, limit):
    count = 0
    while abs(guess ** 2 - num) > limit:
        count += 1
        print("guess", count, ":", guess)
        guess = (guess + (num / guess)) / 2

    else:
        print("final guess", guess)
        print("total guesses", count + 1)


herons(25, 600, 0.00001)

