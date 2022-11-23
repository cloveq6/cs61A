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


s = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
print(repeated(s, 2)) 

s2 = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
print(repeated(s2, 3))

s = iter([3, 2, 2, 2, 1, 2, 1, 4, 4, 5, 5, 5])
print(repeated(s, 3))

print(repeated(s, 3))

s2 = iter([4, 1, 6, 6, 7, 7, 8, 8, 2, 2, 2, 5])
print(repeated(s2, 3))

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