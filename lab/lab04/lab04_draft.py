def skip_add_draft(n):
    """ Takes a number n and returns n + n-2 + n-4 + n-6 + ... + 0.

    >>> skip_add(5)  # 5 + 3 + 1 + 0
    9
    >>> skip_add(10) # 10 + 8 + 6 + 4 + 2 + 0
    30
    >>> # Do not use while/for loops!
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(this_file, 'skip_add',
    ...       ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n <= 0 or n == 1:
        return n
    return n + skip_add_draft(n - 2)

# print(skip_add_draft(0))
# print(skip_add_draft(1))
# print(skip_add_draft(2))
# print(skip_add_draft(5))
# print(skip_add_draft(10))
# print(skip_add_draft(-2))

def summation_draft(n, term):

    """Return the sum of the first n terms in the sequence defined by term.
    Implement using recursion!

    >>> summation(5, lambda x: x * x * x) # 1^3 + 2^3 + 3^3 + 4^3 + 5^3
    225
    >>> summation(9, lambda x: x + 1) # 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
    54
    >>> summation(5, lambda x: 2**x) # 2^1 + 2^2 + 2^3 + 2^4 + 2^5
    62
    >>> # Do not use while/for loops!
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(this_file, 'summation',
    ...       ['While', 'For'])
    True
    """
    assert n >= 1
    "*** YOUR CODE HERE ***"
    if n == 1 : return term(1)
    return term(n) + summation_draft(n-1, term)


# print(summation_draft(5, lambda x: x * x * x))
# print(summation_draft(9, lambda x: x + 1))
# print(summation_draft(5, lambda x: 2**x))

def paths_draft(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    "*** YOUR CODE HERE ***"
    if m==1 or n==1 : return 1
    return  paths_draft(m, n-1) + paths_draft(m-1, n)

# print(paths_draft(2, 2))
# print(paths_draft(5, 7))
# print(paths_draft(3, 3))


def split(n):
    """Split a positive integer into all but its last digit and its last digit."""
    return n // 10, n % 10

def max_digit(n):
    max = 0
    while(n > 0):
        n, digit = split(n)
        if(digit > max): max = digit
    return max

# def max_subseq(n, t):
#     def split(n):
#         return n // 10, n % 10

#     def max_digit(n):
#         max = 0
#         while(n > 0):
#             n, digit = split(n)
#             if(digit > max): max = digit
#         return max
#     if t == 0: return 0
#     if t == 1: return max_digit(n)
#     seq_front = max_subseq(n // 10, t-1)
#     seq_back = n % 10
#     return seq_front * 10 + seq_back
    
    
# print(max_digit(9328238091))

# print(max_subseq(20125, 3))
# print(max_subseq(20125, 5))
# print(max_subseq(20125, 6))
# print(max_subseq(12345, 0))


def add_chars_draft(w1, w2):
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
    if len(w1) == 0 : return w2
    if w1[0] == w2[0]:
        sub_w1 = w1[1:]
        sub_w2 = w2[1:]
        return add_chars_draft(sub_w1, sub_w2)
    return w2[0] + add_chars_draft(w1, w2[1:])


# print(add_chars_draft("owl", "howl"))
# print(add_chars_draft("want", "wanton"))
# print(add_chars_draft("rat", "radiate"))
# print(add_chars_draft("a", "prepare"))
# print(add_chars_draft("resin", "recursion"))
# print(add_chars_draft("fin", "effusion"))
# print(add_chars_draft("coy", "cacophony"))
