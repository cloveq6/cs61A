############
# Nonlocal #
############

def make_withdraw(balance):
    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            return "Insufficient funds"
        balance = balance - amount
        return balance
    return withdraw

##########
# Growth #
##########

total = 0

def count(f):
    """ Returns a version of f that counts the number of calls to that 
    function, and stores the value in the global variable total.

    You do not need to understand this implementation, and do not use the global
    keyword in your own code.

    Usage example: fact = count(fact). Calling fact after this will add the number
    of recursive calls to fact to the value of the total variable.
    """

    def counted_f(*args):
        global total
        total += 1
        return f(*args)
    return counted_f

def fact(n):
    if n <= 1:
        return 1
    return n * fact(n - 1)

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)
    
def fib_iter(n):
    """ An iterative version of fib that adds the number of times we go through
    the while loop to the total variable in the global frame
    """
    global total
    curr, nxt, i = 0, 1, 0
    while i < n:
        curr, nxt = nxt, curr + nxt
        i += 1
        total += 1
    return curr

memo = []

def memoized_fib(n):
    if n <= 1:
        return n
    if n > len(memo):
        memo.extend([-1 for _ in range(n + 1 - len(memo))])
    if memo[n] == -1:
        total = memoized_fib(n - 1) + memoized_fib(n - 2)
        memo[n] = total
    return memo[n]



# withdraw = make_withdraw(100)
# print(withdraw(25))
# print(withdraw(25))
# print(withdraw(60))
# print(withdraw(15))


# def make_withdraw2(balance):
#     def withdraw(balance, amount):
#         if amount > balance:
#             return "Insufficient funds"
#         balance = balance - amount
#         return balance
#     return lambda amount : withdraw(balance, amount)
            


# withdraw = make_withdraw2(100)
# print(withdraw(25))
# print(withdraw(25))
# print(withdraw(60))
# print(withdraw(15))

def make_adder_inc(a):
    """
    >>> adder1 = make_adder_inc(5)
    >>> adder2 = make_adder_inc(6)
    >>> adder1(2)
    7
    >>> adder1(2) # 5 + 2 + 1
    8
    >>> adder1(10) # 5 + 10 + 2
    17
    >>> [adder1(x) for x in [1, 2, 3]]
    [9, 11, 13]
    >>> adder2(5)
    11
    """
    "*** YOUR CODE HERE ***"
    def add(num):
        nonlocal a
        res = num + a
        a += 1
        return res 
    return add


# adder1 = make_adder_inc(5)
# adder2 = make_adder_inc(6)
# print(adder1(2))

# print(adder1(2)) # 5 + 2 + 1

# print(adder1(10)) # 5 + 10 + 2

# [print(adder1(x)) for x in [1, 2, 3]]

# print(adder2(5))

def make_fib():
    """Returns a function that returns the next Fibonacci number
    every time it is called.

    >>> fib = make_fib()
    >>> fib()
    0
    >>> fib()
    1
    >>> fib()
    1
    >>> fib()
    2
    >>> fib()
    3
    >>> fib2 = make_fib()
    >>> fib() + sum([fib2() for _ in range(5)])
    12
    >>> from construct_check import check
    >>> # Do not use lists in your implementation
    >>> check(this_file, 'make_fib', ['List'])
    True
    """
    "*** YOUR CODE HERE ***"
    a = 0
    b = 1
    count = 0
    def funny():
        nonlocal a
        nonlocal b
        nonlocal count
        count += 1
        if count == 1:
            return a
        if count == 2:
            return b
        sum = a + b
        a = b
        b = sum
        return sum
    return funny


# fib = make_fib()
# for i in range(10):
#     print(fib())


def insert_items(lst, entry, elem):
    """
    >>> test_lst = [1, 5, 8, 5, 2, 3]
    >>> new_lst = insert_items(test_lst, 5, 7)
    >>> new_lst
    [1, 5, 7, 8, 5, 7, 2, 3]
    >>> large_lst = [1, 4, 8]
    >>> large_lst2 = insert_items(large_lst, 4, 4)
    >>> large_lst2
    [1, 4, 4, 8]
    >>> large_lst3 = insert_items(large_lst2, 4, 6)
    >>> large_lst3
    [1, 4, 6, 4, 6, 8]
    >>> large_lst3 is large_lst
    True
    """
    "*** YOUR CODE HERE ***"
    index = []
    for i in range(len(lst)):
        if lst[i] == entry:
            index.append(i + len(index))   
    for j in index:
        j += 1
        lst.insert(j, elem)
    return lst

test_lst = [1, 5, 8, 5, 2, 3]
new_lst = insert_items(test_lst, 5, 7)
print(new_lst)

large_lst = [1, 4, 8]
large_lst2 = insert_items(large_lst, 4, 4)
print(large_lst2)
large_lst3 = insert_items(large_lst2, 4, 6)
print(large_lst3)
print(large_lst3 is large_lst)
