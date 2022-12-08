from scheme_reader import *


# tokens = tokenize_lines(["(+ 1 ", "(23 4)) ("])
# tokens_new = tokenize_lines(["(+ 1 ", "(23 4)) ("])
# print(list(tokens_new))
# src = Buffer(tokens)
# print(src.pop_first())
# print(src.pop_first())
# print(src.pop_first())
# print(src.pop_first())
# print(src.pop_first())
# print(src.pop_first())
# print(src.pop_first())
# print(src.pop_first())
# print(src.pop_first())
# print(src.pop_first())
# print(src.pop_first())


# tokens_nil = tokenize_lines(['nil'])
# src = Buffer(tokens_nil)
# print(src.pop_first())
# print(src.pop_first())
# print(list(tokens_nil))

# scheme_read(Buffer(tokenize_lines(['(+ 1 2)'])))
# scheme_read(Buffer(tokenize_lines(['(+ (- 2 3) 1)'])))


"""
part two

"""

# a = {}
# b = {}
# # a.update('a', 1)
# a['bb'] = 1
# b['aa'] = 2
# a.update(b)

# if 'bb' in a:
#     print('hello')
# if 'aa' in a:
#     print('ahello')
# print(a)


# from scheme import *
# first_frame = create_global_frame()
# first_frame.define("x", 3)
# second_frame = Frame(first_frame)
# # print(first_frame.bindings)
# # second_frame.bindings.update(first_frame.bindings)
# # print(second_frame.bindings)
# third_frame = Frame(second_frame)
# fourth_frame = Frame(third_frame)
# # print(fourth_frame.bindings)
# fourth_frame.lookup("x")



# 函数自动解包
# def add(x, y):
#     return x + y
# args = [1, 2]
# print(add(*args))

# def parrot(voltage, state='a stiff', action='voom'):
#     print("-- This parrot wouldn't", action, end=' ')
#     print("if you put", voltage, "volts through it.", end=' ')
#     print("E's", state, "!")

# d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
# parrot(**d)

from scheme import *
env = create_global_frame()
# plus = env.bindings['+']
# print(env.bindings)
# print(type(plus))


# (* 3 4 (- 5 2) 1)

# expr = read_line('(+ (+ 2 2) (+ 1 3) (* 1 4))')

# print(repr(expr))

# Pair('+', Pair)

# Pair(Pair , Pair(Pair('+', Pair(1, Pair(3, nil))), Pair(Pair('*', Pair(1, Pair(4, nil))), nil)))
# Pair('+', Pair(2, Pair(2, nil)))

# Pair(m, Pair(n, Pair(l)))

# print(scheme_eval(expr, create_global_frame()))
# two = Pair(2, nil)
# eval = BuiltinProcedure(scheme_eval, True) # eval procedure
# scheme_apply(eval, two, env) # be sure to check use_env


# case1
# expr = read_line('(+ 2 3)')
# print(repr(expr))
# print(scheme_eval(expr, env))

# case2
# def fun(x, y):
#     return x + y
# feifei = lambda x : fun(x , 1)
# fn = feifei
# print(fn(1))

# case3

# expr2 = read_line('(+ (+ 2 2) (+ 1 3) (* 1 4))')
# print(repr(expr2))
# print(scheme_eval(expr2, env))

# case 4
# expr = read_line('(+ (* 2 2) 3)')
# print(repr(expr))
# print(scheme_eval(expr, env))

# part 5
"""Evaluate a define form.
>>> env = create_global_frame()
>>> do_define_form(read_line("(x 2)"), env)
'x'
>>> scheme_eval("x", env)
2
>>> do_define_form(read_line("(x (+ 2 8))"), env)
'x'
>>> scheme_eval("x", env)
10
"""
# # case1
# env = create_global_frame()
# do_define_form(read_line("(x 2)"), env)
# print(scheme_eval("x", env))

# # case 2
# do_define_form(read_line("(x (+ 2 8))"), env)
# print(scheme_eval("x", env))


# part 6:

print(repr(scheme_read(Buffer(tokenize_lines(["''hello"])))))
# print(repr(scheme_read(Buffer(tokenize_lines(["'''(+ 1 2)"])))))

