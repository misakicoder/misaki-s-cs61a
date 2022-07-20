from audioop import add
from os import times


def add1(x):
    return x + 1

def times2(x):
    return x * 2

f = lambda x : add1(f(x))

def f(x):
    return add1(f(x))

