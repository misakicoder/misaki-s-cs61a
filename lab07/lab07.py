def naturals():
    """A generator function that yields the infinite sequence of natural
    numbers, starting at 1.

    >>> m = naturals()
    >>> type(m)
    <class 'generator'>
    >>> [next(m) for _ in range(10)]
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    i = 1
    while True:
        yield i
        i += 1


def scale(it, multiplier):
    """Yield elements of the iterable it scaled by a number multiplier.

    >>> m = scale([1, 5, 2], 5)
    >>> type(m)
    <class 'generator'>
    >>> list(m)
    [5, 25, 10]

    >>> m = scale(naturals(), 2)
    >>> [next(m) for _ in range(5)]
    [2, 4, 6, 8, 10]
    """
    "*** YOUR CODE HERE ***"
    if type(it) == list:
        i = 0
        while i < len(it):
            yield it[i] * multiplier
            i += 1
    else:
        while True:
            yield next(it) * multiplier


def hailstone(n):
    """
    >>> for num in hailstone(10):
    ...     print(num)
    ...
    10
    5
    16
    8
    4
    2
    1
    """
    "*** YOUR CODE HERE ***" 
    yield n
    if n == 1:
        pass
    else:
        if n % 2 == 0:
            # yield from hailstone(n // 2)
            # print(list(hailstone(n//2)))
            for elem in hailstone(n // 2):
                yield elem
        else:
            yield from hailstone(3 * n + 1)

