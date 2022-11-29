def make_bank(balance):
    """Returns a bank function with a starting balance. Supports
    withdrawals and deposits.

    >>> bank = make_bank(100)
    >>> bank('withdraw', 40)    # 100 - 40
    60
    >>> bank('hello', 500)      # Invalid message passed in
    'Invalid message'
    >>> bank('deposit', 20)     # 60 + 20
    80
    >>> bank('withdraw', 90)    # 80 - 90; not enough money
    'Insufficient funds'
    >>> bank('deposit', 100)    # 80 + 100
    180
    >>> bank('goodbye', 0)      # Invalid message passed in
    'Invalid message'
    >>> bank('withdraw', 60)    # 180 - 60
    120
    """
    def bank(message, amount):
        "*** YOUR CODE HERE ***"
        nonlocal balance
        if message == 'withdraw':
            if amount > balance:
                return 'Insufficient funds'
            balance = balance - amount
            return balance
        if message == 'deposit':
            balance += amount
            return balance
        return 'Invalid message'
    return bank


# bank = make_bank(100)
# print(bank('withdraw', 40))    # 100 - 40
# print(bank('hello', 500))      # Invalid message passed in
# print(bank('deposit', 20))     # 60 + 20
# print(bank('withdraw', 90))    # 80 - 90; not enough money
# print(bank('deposit', 100))    # 80 + 100
# print(bank('goodbye', 0))      # Invalid message passed in
# print(bank('withdraw', 60))    # 180 - 60


def make_withdraw(balance, password):
    """Return a password-protected withdraw function.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> error = w(90, 'hax0r')
    >>> error
    'Insufficient funds'
    >>> error = w(25, 'hwat')
    >>> error
    'Incorrect password'
    >>> new_bal = w(25, 'hax0r')
    >>> new_bal
    50
    >>> w(75, 'a')
    'Incorrect password'
    >>> w(10, 'hax0r')
    40
    >>> w(20, 'n00b')
    'Incorrect password'
    >>> w(10, 'hax0r')
    "Frozen account. Attempts: ['hwat', 'a', 'n00b']"
    >>> w(10, 'l33t')
    "Frozen account. Attempts: ['hwat', 'a', 'n00b']"
    >>> type(w(10, 'l33t')) == str
    True
    """
    "*** YOUR CODE HERE ***"
    error_pw = []
    def bank(amount, input):
        nonlocal balance
        nonlocal password
        nonlocal error_pw
        if len(error_pw) == 3:
            return "Frozen account. Attempts: " + str(error_pw)
        if input == password:
            if amount > balance:
                return 'Insufficient funds'
            balance = balance - amount
            return balance
        error_pw.append(input)
        return 'Incorrect password'
    return bank


# w = make_withdraw(100, 'hax0r')
# w(25, 'hax0r')
# error = w(90, 'hax0r')
# print(error)
# error = w(25, 'hwat')
# print(error)
# new_bal = w(25, 'hax0r')
# print(new_bal)
# print(w(75, 'a'))
# print(w(10, 'hax0r'))
# print(w(20, 'n00b'))
# print(w(10, 'hax0r'))
# print(w(10, 'l33t'))
# print(type(w(10, 'l33t')) == str)

def repeated(t, k):
    """Return the first value in iterator T that appears K times in a row. Iterate through the items such that
    if the same iterator is passed into repeated twice, it continues in the second call at the point it left off
    in the first.

    >>> s = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> repeated(s, 2)
    9
    >>> s2 = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> repeated(s2, 3)
    8
    >>> s = iter([3, 2, 2, 2, 1, 2, 1, 4, 4, 5, 5, 5])
    >>> repeated(s, 3)
    2
    >>> repeated(s, 3)
    5
    >>> s2 = iter([4, 1, 6, 6, 7, 7, 8, 8, 2, 2, 2, 5])
    >>> repeated(s2, 3)
    2
    """
    assert k > 1
    "*** YOUR CODE HERE ***"
    a = 10000000
    count = k
    while True:
        if count == 1 : return a
        cur = next(t)
        if cur==a : 
            count -= 1
        else:
            a = cur
            count = k


# s = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
# print(repeated(s, 2)) 

# s2 = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
# print(repeated(s2, 3))

# s = iter([3, 2, 2, 2, 1, 2, 1, 4, 4, 5, 5, 5])
# print(repeated(s, 3))

# print(repeated(s, 3))

# s2 = iter([4, 1, 6, 6, 7, 7, 8, 8, 2, 2, 2, 5])
# print(repeated(s2, 3))

def double(x):
    print('***', x, '=>', 2*x, '***')
    return 2*x    
    
def built_in_demo():
    """Using built-in sequence functions.

    >>> bcd = ['b', 'c', 'd']
    >>> [x.upper() for x in bcd]
    ['B', 'C', 'D']
    >>> caps = map(lambda x: x.upper(), bcd)
    >>> next(caps)
    'B'
    >>> next(caps)
    'C'
    >>> s = range(3, 7)
    >>> doubled = map(double, s)
    >>> next(doubled)
    *** 3 => 6 ***
    6
    >>> next(doubled)
    *** 4 => 8 ***
    8
    >>> list(doubled)
    *** 5 => 10 ***
    *** 6 => 12 ***
    [10, 12]
    >>> f = lambda x: x < 10
    >>> a = filter(f, map(double, reversed(s)))
    >>> list(a)
    *** 6 => 12 ***
    *** 5 => 10 ***
    *** 4 => 8 ***
    *** 3 => 6 ***
    [8, 6]
    >>> t = [1, 2, 3, 2, 1]
    >>> reversed(t) == t
    False
    >>> list(reversed(t)) == t
    True
    >>> d = {'a': 1, 'b': 2, 'c': 3}
    >>> items = iter(zip(d.keys(), d.values())) # Call next(items)
    """
    
    
def plus_minus(x):
    """Yield x and -x.

    >>> t = plus_minus(3)
    >>> next(t)
    3
    >>> next(t)
    -3
    >>> list(plus_minus(5))
    [5, -5]
    >>> list(map(abs, plus_minus(7)))
    [7, 7]
    """
    yield x
    yield -x

def evens(start, end):
    """A generator function that returns even numbers.

    >>> list(evens(2, 10))
    [2, 4, 6, 8]
    >>> list(evens(1, 10))
    [2, 4, 6, 8]
    """
    even = start + (start % 2)
    while even < end:
        yield even
        even += 2
                
def a_then_b_for(a, b):
    """The elements of a followed by those of b.

    >>> list(a_then_b_for([3, 4], [5, 6]))
    [3, 4, 5, 6]
    """
    for x in a:
        yield x
    for x in b:
        yield x
        
def a_then_b(a, b):
    """The elements of a followed by those of b.

    >>> list(a_then_b([3, 4], [5, 6]))
    [3, 4, 5, 6]
    """
    yield from a
    yield from b
    
def countdown(k):
    """Count down to zero.

    >>> list(countdown(5))
    [5, 4, 3, 2, 1]
    """
    if k > 0:
        yield k
        yield from countdown(k-1)
        
        
def prefixes(s):
    """Yield all prefixes of s.

    >>> list(prefixes('both'))
    ['b', 'bo', 'bot', 'both']
    """
    if s:
        yield from prefixes(s[:-1])
        yield s
        
        
def substrings(s):
    """Yield all substrings of s.

    >>> list(substrings('tops'))
    ['t', 'to', 'top', 'tops', 'o', 'op', 'ops', 'p', 'ps', 's']
    """
    if s:
        yield from prefixes(s)
        yield from substrings(s[1:])
        
        
def permutations(seq):
    """Generates all permutations of the given sequence. Each permutation is a
    list of the elements in SEQ in a different order. The permutations may be
    yielded in any order.

    >>> perms = permutations([100])
    >>> type(perms)
    <class 'generator'>
    >>> next(perms)
    [100]
    >>> try: #this piece of code prints "No more permutations!" if calling next would cause an error
    ...     next(perms)
    ... except StopIteration:
    ...     print('No more permutations!')
    No more permutations!
    >>> sorted(permutations([1, 2, 3])) # Returns a sorted list containing elements of the generator
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    >>> sorted(permutations((10, 20, 30)))
    [[10, 20, 30], [10, 30, 20], [20, 10, 30], [20, 30, 10], [30, 10, 20], [30, 20, 10]]
    >>> sorted(permutations("ab"))
    [['a', 'b'], ['b', 'a']]
    """
    "*** YOUR CODE HERE ***"
    if len(seq) == 1: yield list(seq)
    else:
        for i in range(len(seq)):
            part = seq[i+1:] + seq[:i]
            part_seq = sorted(permutations(part))
            for j in part_seq:
                yield [seq[i]] + j
        
    # if seq:
    #     part = seq[i+1:] + seq[:i]
    #     part_seq = sorted(permutations(part))
    #     yield [seq[0]] + part_seq
        # for i in part_seq:
        #     yield i

    # for i in range(len(seq)):
    #     part = seq[i+1:] + seq[:i]
    #     print(part)
        # ll = permutations(part)
        # yield [seq[i]] + list(ll)
        
print(sorted(permutations([1, 2, 3])))
print(sorted(permutations((10, 20, 30))))
print(sorted(permutations("abc")))

# permutations([1, 2])


# def fun():
#     part = [3, 4]
#     yield part + [1, 2]
    
# print(list(fun()))