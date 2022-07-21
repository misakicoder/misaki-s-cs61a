def max_subseq(n, t):
    """
    Return the maximum subsequence of length at most t that can be found in the given number n.
    For example, for n = 20125 and t = 3, we have that the subsequences are
        2
        0
        1
        2
        5
        20
        21
        22
        25
        01
        02
        05
        12
        15
        25
        201
        202
        205
        212
        215
        225
        012
        015
        025
        125
    and of these, the maxumum number is 225, so our answer is 225.

    >>> max_subseq(20125, 3)
    225
    >>> max_subseq(20125, 5)
    20125
    >>> max_subseq(20125, 6) # note that 20125 == 020125
    20125
    >>> max_subseq(12345, 3)
    345
    >>> max_subseq(12345, 0) # 0 is of length 0
    0
    >>> max_subseq(12345, 1)
    5
    """
    "*** YOUR CODE HERE ***"
    if n == 0:
        return 0
    elif t == 0:
        return 0
    else:
        return max(10*max_subseq(n // 10,t-1)+ n % 10,max_subseq(n // 10,t))


print(max_subseq(54321,3))
