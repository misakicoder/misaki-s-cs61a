def test():
    yield 1
    yield 2

m = test()
print(next(m))
print(next(m))