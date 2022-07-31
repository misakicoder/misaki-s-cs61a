

def tree(root_label,branches = []):
    for branch in branches:
        assert is_tree(branch),"branches must be trees"
    return [root_label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

def fib_tree(n):
    if n == 0 or n == 1:
        return tree(n)
    else:
        left,right = fib_tree(n-2) ,fib_tree(n-1)
        fib_n = label(left) + label(right)
        return tree(fib_n,[left,right])

def partition_tree(n,m):
    if n == 0:
        return tree(True)
    elif n < 0 or m == 0:
        return tree(False)
    else:
        left = partition_tree(n-m,m)
        right = partition_tree(n,m-1)
        return tree(m,[left,right])

def print_parts(tree,partition = []):
    if is_leaf(tree):
        if label(tree):
            print(' + ' + partition)
        else:
            left,right = branches(tree)
            m = str(label(tree))
            print_parts(left,partition + [m])
            print_parts(right,partition)

def berry_finder(t):
    """Returns True if t contains a node with the value 'berry' and 
    False otherwise.

    >>> scrat = tree('berry')
    >>> berry_finder(scrat)
    True
    >>> sproul = tree('roots', [tree('branch1', [tree('leaf'), tree('berry')]), tree('branch2')])
    >>> berry_finder(sproul)
    True
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> berry_finder(numbers)
    False
    >>> t = tree(1, [tree('berry',[tree('not berry')])])
    >>> berry_finder(t)
    True
    """
    "*** YOUR CODE HERE ***"
    if not is_tree(t):
        return False
    else:
        if t[0] == 'berry':
            return True
        else:
            return berry_finder(t[1:]) or berry_finder(t[0])

def sprout_leaves(t, leaves):
    """Sprout new leaves containing the data in leaves at each leaf in
    the original tree t and return the resulting tree.

    >>> t1 = tree(1, [tree(2), tree(3)])
    >>> print_tree(t1)
    1
      2
      3
    >>> new1 = sprout_leaves(t1, [4, 5])
    >>> print_tree(new1)
    1
      2
        4
        5
      3
        4
        5

    >>> t2 = tree(1, [tree(2, [tree(3)])])
    >>> print_tree(t2)
    1
      2
        3
    >>> new2 = sprout_leaves(t2, [6, 1, 2])
    >>> print_tree(new2)
    1
      2
        3
          6
          1
          2
    """
    "*** YOUR CODE HERE ***"
    for branch in branches(t):
        if is_leaf(branch):
            for leave in leaves:
                branch.append(tree(leave))
        else:
            sprout_leaves(branch,leaves)
    return t

print(tree(3,[tree(2,[tree(3,[tree(2)])])]))
