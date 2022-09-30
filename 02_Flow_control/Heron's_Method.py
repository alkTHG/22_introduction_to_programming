# herons method for zeroing in on square root of x
# solution uses recursion
def herons(num, guess, limit):
    count = 0

    def guessing(guess, count, limit):
        if abs(guess ** 2 - num) > limit:
            count += 1
            print("guess", count, ":", guess)
            guessing((guess + (num / guess)) / 2, count, limit)
        else:
            print("final guess", guess)
            print("total guesses", count + 1)

    return guessing(guess, count, limit)


herons(25, 600, 0.00001)
