from _collections_abc import Iterable

flatten = ([1, [9, 3, [4, 5], [2, 7], 8], 1])
# flatten = (['a', 'c', 'b'])


def outer_flat(list):
    ans = []

    def flat(list):
        for value in list:
            if not isinstance(value, Iterable):
                ans.append(value)
            else:
                flat(value)
    flat(list)
    print(ans)


outer_flat(flatten)