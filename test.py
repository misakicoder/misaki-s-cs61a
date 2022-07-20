def cycle(f1, f2, f3):
    """Returns a function that is itself a higher-order function.

    >>> my_cycle = cycle(add1, times2, add3)
    >>> identity = my_cycle(0)
    >>> identity(5)
    5
    >>> add_one_then_double = my_cycle(2)
    >>> add_one_then_double(1)
    4
    >>> do_all_functions = my_cycle(3)
    >>> do_all_functions(2)
    9
    >>> do_more_than_a_cycle = my_cycle(4)
    >>> do_more_than_a_cycle(2)
    10
    >>> do_two_cycles = my_cycle(6)
    >>> do_two_cycles(1)
    19
    """
    "*** YOUR CODE HERE ***"
    def f(n,x):
        if n == 0:
            return x
        elif n % 3 == 1:
            return f1(f(n-1,x))
        elif n % 3 == 2:
            return f2(f(n-1,x))
        else:
            return f3(f(n-1,x))         

    def  g(n):
        def h(x):
            return f(n,x)
        return h
    return g

def add1(x):
    return x + 1
def times2(x):
    return x * 2
def add3(x):
    return x + 3
my_cycle = cycle(add1, times2, add3)
identity = my_cycle(6)
print(identity(5))