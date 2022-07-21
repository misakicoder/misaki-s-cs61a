def add_chars(w1, w2):
    """
    Return a string containing the characters you need to add to w1 to get w2.

    You may assume that w1 is a subsequence of w2.

    >>> add_chars("owl", "howl")
    'h'
    >>> add_chars("want", "wanton")
    'on'
    >>> add_chars("rat", "radiate")
    'diae'
    >>> add_chars("a", "prepare")
    'prepre'
    >>> add_chars("resin", "recursion")
    'curo'
    >>> add_chars("fin", "effusion")
    'efuso'
    >>> add_chars("coy", "cacophony")
    'acphon'
    >>> from construct_check import check
    >>> # ban iteration and sets
    >>> check(LAB_SOURCE_FILE, 'add_chars',
    ...       ['For', 'While', 'Set', 'SetComp']) # Must use recursion
    True
    """
    "*** YOUR CODE HERE ***"
    def process(w1,w2,index1,index2):
        if index2 >= len(w2):
            return ""
        elif w1 != None and index1 >= len(w1):
            return str(process(None,w2,index1,index2))
        else:
            if w1 != None and w1[index1] == w2[index2]:
                return str(process(w1,w2,index1 + 1,index2 + 1))
            if w1 == None or w1[index1] != w2[index2]:
                return str(w2[index2]) + str(process(w1,w2,index1,index2 + 1))
    return process(w1,w2,0,0)

print(add_chars("fin", "effusion"))