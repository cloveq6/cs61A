from operator import add, mul, mod


#问题一 lambda_curry2 draft
# def lambda_curry2(func):
#     """
#     Returns a Curried version of a two-argument function FUNC.
#     >>> from operator import add, mul, mod
#     >>> curried_add = lambda_curry2(add)
#     >>> add_three = curried_add(3)
#     >>> add_three(5)
#     8
#     >>> curried_mul = lambda_curry2(mul)
#     >>> mul_5 = curried_mul(5)
#     >>> mul_5(42)
#     210
#     >>> lambda_curry2(mod)(123)(10)
#     3
#     """
#     "*** YOUR CODE HERE ***"
#     return lambda x: lambda y : func(x, y)

# curried_add = lambda_curry2(add)
# add_three = curried_add(3)
# res = add_three(5)
# print(res)

# curried_mul = lambda_curry2(mul)
# mul_5 = curried_mul(5)
# print(mul_5(42))

# print(lambda_curry2(mod)(123)(10))


# def curried_pow(x):
#         def h(y):
#             return pow(x, y)
#         return h
    
# def curried_pow(x):
#         return lambda y: pow(x, y)
    
    
# def curried_pow:
#         return lambda x: lambda y: pow(x, y)

# curried_add = lambda_curry2(add)
# x = curried_add(5, 6)
# print(x)

# func_g = curried_pow(5)
# y = func_g(2)
# print(y)


 
# 问题2 count_cond dratf

# def count_factors(n):
#     """Return the number of positive factors that n has.
#     >>> count_factors(6)
#     4   # 1, 2, 3, 6
#     >>> count_factors(4)
#     3   # 1, 2, 4
#     """
#     i, count = 1, 0
#     while i <= n:
#         if n % i == 0:
#             count += 1
#         i += 1
#     return count

# def count_primes(n):
#     """Return the number of prime numbers up to and including n.
#     >>> count_primes(6)
#     3   # 2, 3, 5
#     >>> count_primes(13)
#     6   # 2, 3, 5, 7, 11, 13
#     """
#     i, count = 1, 0
#     while i <= n:
#         if is_prime(i):
#             count += 1
#         i += 1
#     return count

# def is_prime(n):
#     return count_factors(n) == 2 # only factors are 1 and n


# def count_cond(condition):
#     """Returns a function with one parameter N that counts all the numbers from
#     1 to N that satisfy the two-argument predicate function Condition, where
#     the first argument for Condition is N and the second argument is the
#     number from 1 to N.

#     >>> count_factors = count_cond(lambda n, i: n % i == 0)
#     >>> count_factors(2)   # 1, 2
#     2
#     >>> count_factors(4)   # 1, 2, 4
#     3
#     >>> count_factors(12)  # 1, 2, 3, 4, 6, 12
#     6

#     >>> is_prime = lambda n, i: count_factors(i) == 2
#     >>> count_primes = count_cond(is_prime)
#     >>> count_primes(2)    # 2
#     1
#     >>> count_primes(3)    # 2, 3
#     2
#     >>> count_primes(4)    # 2, 3
#     2
#     >>> count_primes(5)    # 2, 3, 5
#     3
#     >>> count_primes(20)   # 2, 3, 5, 7, 11, 13, 17, 19
#     8
#     """
#     "*** YOUR CODE HERE ***"



# 本来需要写一大堆函数，现在简化太多。
# def count_cond(condition):
#     def silly(n):
#         i, count = 1, 0
#         while i <= n:
#             if condition(n, i):
#                 count += 1
#             i += 1
#         return count
#     return silly
            
# count_factors = count_cond(lambda n, i: n % i == 0)
# is_prime = lambda n, i: count_factors(i) == 2
# count_primes = count_cond(is_prime)
# print(count_primes(20))

# print(count_factors(12))




#问题三draft

# def compose1(f, g):
#     """Return the composition function which given x, computes f(g(x)).

#     >>> add_one = lambda x: x + 1        # adds one to x
#     >>> square = lambda x: x**2
#     >>> a1 = compose1(square, add_one)   # (x + 1)^2
#     >>> a1(4)
#     25
#     >>> mul_three = lambda x: x * 3      # multiplies 3 to x
#     >>> a2 = compose1(mul_three, a1)    # ((x + 1)^2) * 3
#     >>> a2(4)
#     75
#     >>> a2(5)
#     108
#     """
#     return lambda x: f(g(x))

# def composite_identity(f, g):
#     """
#     Return a function with one parameter x that returns True if f(g(x)) is
#     equal to g(f(x)). You can assume the result of g(x) is a valid input for f
#     and vice versa.

#     >>> add_one = lambda x: x + 1        # adds one to x
#     >>> square = lambda x: x**2
#     >>> b1 = composite_identity(square, add_one)
#     >>> b1(0)                            # (0 + 1)^2 == 0^2 + 1
#     True
#     >>> b1(4)                            # (4 + 1)^2 != 4^2 + 1
#     False
#     """
#     "*** YOUR CODE HERE ***"
#     res1 = lambda x: f(g(x))
#     res2 = lambda y: g(f(y))
#     return lambda z: res1(z) == res2(z)

# add_one = lambda x: x + 1
# square = lambda x: x**2
# b1 = composite_identity(square, add_one)
# b1(0)
# print(b1(0), b1(4))


#问题四draft

def cycle(f1, f2, f3):
    """Returns a function that is itself a higher-order function.

    >>> def add1(x):
    ...     return x + 1
    >>> def times2(x):
    ...     return x * 2
    >>> def add3(x):
    ...     return x + 3
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
    def nested_fuc(x):
        return f3(f2(f1(x)))
    
    def logic(n, req):
        if n == 1 :
            n -= 1
            return n, f1(req)
        if n == 2 :
            n -= 2
            return n, f2(f1(req))
        if n >= 3 :
            n -= 3 
            return n, nested_fuc(req)
        
    def start(count, req):
        while(count > 0) : 
            count, req = logic(count, req)
        return req  
    return lambda count : lambda req : start(count, req)

def add1(x):
    return x + 1
def times2(x):
    return x * 2
def add3(x):
    return x + 3
my_cycle = cycle(add1, times2, add3)
identity = my_cycle(0)
print(identity(12))

add_one_then_double = my_cycle(2)
print(add_one_then_double(1))

do_all_functions = my_cycle(3)
print(do_all_functions(2))

do_more_than_a_cycle = my_cycle(4)
print(do_more_than_a_cycle(2))

do_two_cycles = my_cycle(6)
print(do_two_cycles(1))
        
            


# 下面是lambda 示例

# e = lambda x: lambda y: lambda z: x + y + z
# func1 = e(1)
# func2 = func1(2)
# res = func2(3)
# print(res)

# higher_order_lambda = lambda f: lambda x: f(x)

# func1 = higher_order_lambda(abs)
# res = func1(-5)
# print(res)


# higher_order_lambda2 = lambda f: lambda x: lambda y: f(x, y)

# func1 = higher_order_lambda2(add)
# func2 = func1(-5)
# res = func2(6)
# print(res)

# call_thrice = lambda f: lambda x: f(f(f(x)))
# tt = call_thrice(lambda y: y + 1)(0)
# print(tt)

# examples of lambda ending 