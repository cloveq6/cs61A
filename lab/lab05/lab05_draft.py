from math import sqrt

def reverse_string(s):
    """Reverse a string s.

    >>> reverse_string('draw')
    'ward'
    """
    if len(s) == 1:
        return s
    else:
        return reverse_string(s[1:]) + s[0]


ll = [i**2 for i in [1, 2, 3, 4] if i % 2 == 0]
lll = [i+1 for i in ll if i > 10]
# print(ll)
# print(lll)



a = [1, 2, 3]
b = [2, 3, 4]
lw = [[a[i], b[i]] for i in range(3)]
# print(lw)

res = []
for i in range(len(a)):
    item = [a[i], b[i]]
    res.append(item)
    # print(item)
# print(res)



def fun(x1, x2):
    m = x1[0] - x2[0]
    n = x1[1] - x2[1]
    return sqrt(m*m + n*n)


x1 = [0, 1]
x2 = [0, 2]
# print(fun(x1, x2))

x1 = [6.5, 12]
x2 = [2.5, 15]
# print(fun(x1, x2))

# (x1 - x2)**2 + (y1 - y2)**2


def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

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
    """Construct a Fibonacci tree.

    >>> fib_tree(1)
    [1]
    >>> fib_tree(3)
    [2, [1], [1, [0], [1]]]
    >>> fib_tree(5)
    [5, [2, [1], [1, [0], [1]]], [3, [1, [0], [1]], [2, [1], [1, [0], [1]]]]]
    """
    if n == 0 or n == 1:
        return tree(n)
    else:
        left = fib_tree(n-2)
        right = fib_tree(n-1)
        fib_n = label(left) + label(right)
        return tree(fib_n, [left, right])

def count_leaves(t):
    """The number of leaves in tree.

    >>> count_leaves(fib_tree(5))
    8
    """
    if is_leaf(t):
        return 1
    else:
        return sum([count_leaves(b) for b in branches(t)])
    
def count_leaves2(s):
    count = 0
    if is_leaf(s):
        return 1
    else:
        tree_branches = branches(s)
        for i in tree_branches:
            count += count_leaves(i)
    return count

first_tree = tree(3, [tree(1), tree(2, [tree(1), [tree(1)]])]) # [3, [1], [2, [1], [[1]]]]

# print(count_leaves(first_tree))
# print(count_leaves2(first_tree))

# print(first_tree)
# print(is_tree(first_tree))
# print(branches(first_tree))
# print(label(first_tree))
# for branch in branches(first_tree):
#     print(label(branch))

# second_tree = tree(5, [tree(1)])
# third_tree = tree(6)
# print(is_tree(third_tree))

# string_tree = tree('hello')
# print(string_tree)


def leaves(tree):
    """Return a list containing the leaf labels of tree.
    lst = [[1, 2], [3, 4]]
    print(sum(lst, [])) 
    #[1, 2, 3, 4]
    
    >>> leaves(fib_tree(5))
    [1, 0, 1, 0, 1, 1, 0, 1]
    """
    if is_leaf(tree):
        return [label(tree)]
    else:
        return sum([leaves(b) for b in branches(tree)], [])
        
        # ll = [leaves(b) for b in branches(tree)]
        # print(ll)
        # return sum(ll, [])

    
fib0 = fib_tree(0)
fib1 = fib_tree(1)
fib2 = fib_tree(2)
# print(fib0)
# print(fib1)
# print(fib2)
# print(leaves(fib2))
leaves(fib2)

def print_tree(t, indent=0):
    """Print a representation of this tree in which each label is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> print_tree(fib_tree(4))
    3
      1
        0
        1
      2
        1
        1
          0
          1
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)
  




def print_sums(t, path_sum):
    """Print the sum of labels along the path from the root to each leaf.

    >>> print_sums(tree(3, [tree(4), tree(5, [tree(6)])]), 0)
    7
    14
    >>> print_sums(haste, '')
    has
    hat
    he
    """
    path_sum = path_sum + label(t)
    if is_leaf(t):
        print(path_sum)
    else:
        for branch in branches(t):
            print_sums(branch, path_sum)
  
      
# tree1 = tree(1, [tree(2), tree(3, [tree(4), tree(5)])])  
tree1 = tree(1, [tree(2), tree(3, [tree(4, [tree(5)])])])  
# print_tree(fib_tree(3))
# print_tree(tree1)


# def berry_finder(t):
#     """Returns True if t contains a node with the value 'berry' and 
#     False otherwise.

#     >>> scrat = tree('berry')
#     >>> berry_finder(scrat)
#     True
#     >>> sproul = tree('roots', [tree('branch1', [tree('leaf'), tree('berry')]), tree('branch2')])
#     >>> berry_finder(sproul)
#     True
#     >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
#     >>> berry_finder(numbers)
#     False
#     >>> t = tree(1, [tree('berry',[tree('not berry')])])
#     >>> berry_finder(t)
#     True
#     """
#     "*** YOUR CODE HERE ***"
#     if label(t) == 'berry': return True
#     if is_leaf(t) and label(t) != 'berry': return False 
#     # if is_leaf(t) != 'berry' : return False
#     else:
#         flag = False
#         for branch in branches(t):
#             t = berry_finder(branch)
#             # print('t ' + str(t))
#             flag = flag or t
#     return flag

# scrat = tree('berry')
# print(berry_finder(scrat))

# sproul = tree('roots', [tree('branch1', [tree('leaf'), tree('berry')]), tree('branch2')])
# print(berry_finder(sproul))

# numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
# print(berry_finder(numbers))

# t = tree(1, [tree('berry',[tree('not berry')])])
# print(berry_finder(t))


# def count_leaves2(s):
#     count = 0
#     if is_leaf(s):
#         return 1
#     else:
#         tree_branches = branches(s)
#         for i in tree_branches:
#             count += count_leaves(i)
#     return count

# def sprout_leaves(t, leaves):
#     """Sprout new leaves containing the data in leaves at each leaf in
#     the original tree t and return the resulting tree.

#     >>> t1 = tree(1, [tree(2), tree(3)])
#     >>> print_tree(t1)
#     1
#       2
#       3
#     >>> new1 = sprout_leaves(t1, [4, 5])
#     >>> print_tree(new1)
#     1
#       2
#         4
#         5
#       3
#         4
#         5

#     >>> t2 = tree(1, [tree(2, [tree(3)])])
#     >>> print_tree(t2)
#     1
#       2
#         3
#     >>> new2 = sprout_leaves(t2, [6, 1, 2])
#     >>> print_tree(new2)
#     1
#       2
#         3
#           6
#           1
#           2
#     """
#     "*** YOUR CODE HERE ***"
#     if is_leaf(t):
#         leaf_trees = [tree(i) for i in leaves]
#         return tree(label(t), leaf_trees)
#     else:
#         tree_branches = branches(t)
#         return tree(label(t), [sprout_leaves(i, leaves) for i in tree_branches])


# t1 = tree(1, [tree(2), tree(3)])
# print_tree(t1)
# new1 = sprout_leaves(t1, [4, 5])
# print_tree(new1)

# t2 = tree(1, [tree(2, [tree(3)])])
# print_tree(t2)
# new2 = sprout_leaves(t2, [6, 1, 2])
# print_tree(new2)
 
        

                
        

