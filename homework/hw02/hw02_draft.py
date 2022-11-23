def num_eights(x):
    """Returns the number of times 8 appears as a digit of x.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    if x == 8 : return 1
    if x < 10 : return 0
    if x % 10 == 8 : return num_eights(x // 10) + 1
    return num_eights(x // 10)

# print(num_eights(3))
# print(num_eights(8))
# print(num_eights(88888888))
# print(num_eights(2568))
# print(num_eights(86380))
# print(num_eights(12345))



def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(8)
    8
    >>> pingpong(10)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    -2
    >>> pingpong(30)
    -2
    >>> pingpong(68)
    0
    >>> pingpong(69)
    -1
    >>> pingpong(80)
    0
    >>> pingpong(81)
    1
    >>> pingpong(82)
    0
    >>> pingpong(100)
    -6
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    sum = 0
    flag = True
    for i in range(1, n+1):
        if flag : sum += 1 
        else: sum -= 1
        if num_eights(i) > 0 or i%8 == 0: flag = not flag
    return sum

# print(pingpong(69))  -1
# print(pingpong(70))  -2
# print(pingpong(79))  1
# print(pingpong(80))  0
# print(pingpong(81))  1
    
# def pingpong_recursion(n):
#     def condition(n):
#         if n==0 : return 0
#         temp = 0
#         for i in range(1, n):
#             if num_eights(i) > 0 or i%8 == 0:
#                 temp += 1
#         return temp
#     if n <= 8 : return n
#     if condition(n)%2 : return pingpong_recursion(n - 1) - 1
#     return pingpong_recursion(n - 1) + 1


# def pingpong_recursion(n):
#     def condition(n):
#         if n <= 1 : return [True]
#         flag = True
#         if num_eights(n) > 0 or n%8 == 0:
#             flag = not flag
#         return condition(n-1).append(flag)
    
#     if condition(n)[n] : return pingpong_recursion(n - 1) - 1
#     return pingpong_recursion(n - 1) + 1  

# print(pingpong_recursion(8))
# print(pingpong_recursion(9))


# for i in range(1, 73):
#     print(pingpong_recursion(i))
# print("*****************")

# for i in range(1, 100):
#     print(i)
#     assert(pingpong(i), pingpong_recursion(i))
    # print(pingpong(i))





def condition(n):
    return num_eights(n) > 0 or n%8 == 0

def process(n, state): 
    if n <= 8 : return state     
    if condition(n-1):
        return process(n-1, not state)
    return process(n-1, state)

def pingpong_recursion(n):
    if n <= 8 : return n
    if process(n , False): return pingpong_recursion(n-1) - 1
    return pingpong_recursion(n-1) + 1



# print(process(9, False))
# print(process(17, False))
# print(process(18, False))
# print(process(19, False))



    # if n <= 8 : return n
    # # print(condition(n))
    # if state:
    #         return process(n-1, state) + 1
    # else:
    #     return process(n-1, state) - 1
    
# def pingpong_recursion(n):
    
    
    
    
#     if n <= 8 : return n
#     if condition(n)%2 : return pingpong_recursion(n - 1) - 1
#     return pingpong_recursion(n - 1) + 1

# assert语法
# for i in range(1, 101):
#     assert pingpong(i) == pingpong_recursion(i)
    # print(pingpong_recursion(i))


# print(pingpong_recursion(72))
# print(pingpong(72))


# def missing_digits(n):
#     """Given a number a that is in sorted, increasing order,
#     return the number of missing digits in n. A missing digit is
#     a number between the first and last digit of a that is not in n.
#     >>> missing_digits(1248) # 3, 5, 6, 7
#     4
#     >>> missing_digits(1122) # No missing numbers
#     0
#     >>> missing_digits(123456) # No missing numbers
#     0
#     >>> missing_digits(3558) # 4, 6, 7
#     3
#     >>> missing_digits(35578) # 4, 6
#     2
#     >>> missing_digits(12456) # 3
#     1
#     >>> missing_digits(16789) # 2, 3, 4, 5
#     4
#     >>> missing_digits(19) # 2, 3, 4, 5, 6, 7, 8
#     7
#     >>> missing_digits(4) # No missing numbers between 4 and 4
#     0
#     >>> from construct_check import check
#     >>> # ban while or for loops
#     >>> check(HW_SOURCE_FILE, 'missing_digits', ['While', 'For'])
#     True
#     """
#     "*** YOUR CODE HERE ***"
    
#     if(n < 10) : return 0
#     n_pre, tail1, tail2 = n//10, n%10, n//10%10
#     # print(n_pre, tail1, tail2)
#     diff = tail1 - tail2 
#     if(diff <= 1) :return missing_digits(n_pre)
#     return missing_digits(n_pre) + diff - 1
    
    
# print(missing_digits(1248))
# print(missing_digits(1122))

def next_largest_coin(coin):
    """Return the next coin. 
    >>> next_largest_coin(1)
    5
    >>> next_largest_coin(5)
    10
    >>> next_largest_coin(10)
    25
    >>> next_largest_coin(2) # Other values return None
    """
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25
    
    
    



def count_coins(total):
    """Return the number of ways to make change for total using coins of value of 1, 5, 10, 25.
    >>> count_coins(15)
    6
    >>> count_coins(10)
    4
    >>> count_coins(20)
    9
    >>> count_coins(100) # How many ways to make change for a dollar?
    242
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_coins', ['While', 'For'])                                          
    True
    """
    "*** YOUR CODE HERE ***"
    def next_smallest_coin(coin):
        if coin == 25:
            return 10
        elif coin == 10:
            return 5
        elif coin == 5:
            return 1
    def helper(total, coin):
        if total<0 : return 0
        if total==0 : return 1
        if coin==1 : return 1
        return helper(total-coin, coin) + helper(total, next_smallest_coin(coin))
    if total <= 0: return 0
    if total < 5 : return 1
    if total < 10 : return helper(total, 5)
    if total < 25 : return helper(total, 10) 
    return helper(total, 25)
        



print(count_coins(15))
print(count_coins(10))
print(count_coins(20))
print(count_coins(100))