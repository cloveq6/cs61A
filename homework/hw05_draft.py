import itertools

class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.first = 5
    >>> s.rest.first = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'


class Tree:
    """
    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def map(self, fn):
        """
        Apply a function `fn` to each node in the tree and mutate the tree.

        >>> t1 = Tree(1)
        >>> t1.map(lambda x: x + 2)
        >>> t1.map(lambda x : x * 4)
        >>> t1.label
        12
        >>> t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> t2.map(lambda x: x * x)
        >>> t2
        Tree(9, [Tree(4, [Tree(25)]), Tree(16)])
        """
        self.label = fn(self.label)
        for b in self.branches:
            b.map(fn)

    def __contains__(self, e):
        """
        Determine whether an element exists in the tree.

        >>> t1 = Tree(1)
        >>> 1 in t1
        True
        >>> 8 in t1
        False
        >>> t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> 6 in t2
        False
        >>> 5 in t2
        True
        """
        if self.label == e:
            return True
        for b in self.branches:
            if e in b:
                return True
        return False

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()

def store_digits(n):
    """Stores the digits of a positive number n in a linked list.

    >>> s = store_digits(1)
    >>> s
    Link(1)
    >>> store_digits(2345)
    Link(2, Link(3, Link(4, Link(5))))
    >>> store_digits(876)
    Link(8, Link(7, Link(6)))
    >>> # a check for restricted functions
    >>> import inspect, re
    >>> cleaned = re.sub(r"#.*\\n", '', re.sub(r'"{3}[\s\S]*?"{3}', '', inspect.getsource(store_digits)))
    >>> print("Do not use str or reversed!") if any([r in cleaned for r in ["str", "reversed"]]) else None
    """
    "*** YOUR CODE HERE ***"
    def transfer_link(lst):
        if len(lst) == 1:
            return Link(lst[0], Link.empty)
        link_last = transfer_link(lst[1:])
        return Link(lst[0], link_last)
    lst = []
    while(n):
        all_but_last, last = n // 10, n % 10
        lst.insert(0, last)
        n = all_but_last
    return transfer_link(lst)

# print(store_digits(2345))

def is_bst(t):
    """Returns True if the Tree t has the structure of a valid BST.

    >>> t1 = Tree(6, [Tree(2, [Tree(1), Tree(4)]), Tree(7, [Tree(7), Tree(8)])])
    >>> is_bst(t1)
    True
    >>> t2 = Tree(8, [Tree(2, [Tree(9), Tree(1)]), Tree(3, [Tree(6)]), Tree(5)])
    >>> is_bst(t2)
    False
    >>> t3 = Tree(6, [Tree(2, [Tree(4), Tree(1)]), Tree(7, [Tree(7), Tree(8)])])
    >>> is_bst(t3)
    False
    >>> t4 = Tree(1, [Tree(2, [Tree(3, [Tree(4)])])])
    >>> is_bst(t4)
    True
    >>> t5 = Tree(1, [Tree(0, [Tree(-1, [Tree(-2)])])])
    >>> is_bst(t5)
    True
    >>> t6 = Tree(1, [Tree(4, [Tree(2, [Tree(3)])])])
    >>> is_bst(t6)
    True
    >>> t7 = Tree(2, [Tree(1, [Tree(5)]), Tree(4)])
    >>> is_bst(t7)
    False
    """
    "*** YOUR CODE HERE ***"
    def bst_min(t):
        if t.is_leaf(): return t.label
        min = t.label
        t_branchs = t.branches
        for b in t_branchs:
            value = bst_min(b)
            if value < min:
                min = value
        return min
    def bst_max(t):
        if t.is_leaf(): return t.label
        max = t.label
        t_branchs = t.branches
        for b in t_branchs:
            value = bst_max(b)
            if value > max:
                max = value
        return max
    if t.is_leaf():
        return True
    t_branchs = t.branches
    if len(t_branchs) == 2:
        left_t = bst_max(t_branchs[0])
        right_t = bst_min(t_branchs[1])
        return left_t <= t.label and right_t > t.label and is_bst(t_branchs[0]) and is_bst(t_branchs[1])
    left_t = bst_max(t_branchs[0])
    right_t = bst_min(t_branchs[0])
    return (left_t <= t.label and is_bst(t_branchs[0])) or (right_t > t.label and is_bst(t_branchs[0]))
# def silly(t):
#     if t.is_leaf(): return t.label
#     min = t.label
#     t_branchs = t.branches
#     for b in t_branchs:
#         value = silly(b)
#         if value < min:
#             min = value
#     return min

# def silly2(t):
#     if t.is_leaf(): return t.label
#     max = t.label
#     t_branchs = t.branches
#     for b in t_branchs:
#         value = silly2(b)
#         if value > max:
#             max = value
#     return max
# print(silly(Tree(6, [Tree(2, [Tree(1), Tree(4)]), Tree(7, [Tree(7), Tree(8)])])))
# print(silly2(Tree(6, [Tree(2, [Tree(1), Tree(4)]), Tree(7, [Tree(7), Tree(8)])])))


# t1 = Tree(6, [Tree(2, [Tree(1), Tree(4)]), Tree(7, [Tree(7), Tree(8)])])
# print(is_bst(t1))
# t2 = Tree(8, [Tree(2, [Tree(9), Tree(1)]), Tree(3, [Tree(6)]), Tree(5)])
# print(is_bst(t2))
# t3 = Tree(6, [Tree(2, [Tree(4), Tree(1)]), Tree(7, [Tree(7), Tree(8)])])
# print(is_bst(t3))
# t4 = Tree(1, [Tree(2, [Tree(3, [Tree(4)])])])
# print(is_bst(t4))
# t5 = Tree(1, [Tree(0, [Tree(-1, [Tree(-2)])])])
# print(is_bst(t5))
# t6 = Tree(1, [Tree(4, [Tree(2, [Tree(3)])])])
# print(is_bst(t6))
# t7 = Tree(2, [Tree(1, [Tree(5)]), Tree(4)])
# print(is_bst(t7))

def preorder(t):
    """Return a list of the entries in this tree in the order that they
    would be visited by a preorder traversal (see problem description).

    >>> numbers = Tree(1, [Tree(2), Tree(3, [Tree(4), Tree(5)]), Tree(6, [Tree(7)])])
    >>> preorder(numbers)
    [1, 2, 3, 4, 5, 6, 7]
    >>> preorder(Tree(2, [Tree(4, [Tree(6)])]))
    [2, 4, 6]
    """
    "*** YOUR CODE HERE ***"
    if t.is_leaf():
        return [t.label]
    res = [t.label]
    t_branches = t.branches
    for b in t_branches:
        res += preorder(b)
    return res

# numbers = Tree(1, [Tree(2), Tree(3, [Tree(4), Tree(5)]), Tree(6, [Tree(7)])])
# print(preorder(numbers))
# vv = preorder(Tree(2, [Tree(4, [Tree(6)])]))
# print(vv)


# lst = []
def path_yielder(t, value):
    """Yields all possible paths from the root of t to a node with the label value
    as a list.

    >>> t1 = Tree(1, [Tree(2, [Tree(3), Tree(4, [Tree(6)]), Tree(5)]), Tree(5)])
    >>> print(t1)
    1
      2
        3
        4
          6
        5
      5
    >>> next(path_yielder(t1, 6))
    [1, 2, 4, 6]
    >>> path_to_5 = path_yielder(t1, 5)
    >>> sorted(list(path_to_5))
    [[1, 2, 5], [1, 5]]

    >>> t2 = Tree(0, [Tree(2, [t1])])
    >>> print(t2)
    0
      2
        1
          2
            3
            4
              6
            5
          5
    >>> path_to_2 = path_yielder(t2, 2)
    >>> sorted(list(path_to_2))
    [[0, 2], [0, 2, 1, 2]]
    """

    "*** YOUR CODE HERE ***"
    if t.label == value:
        yield [value]
    if t.is_leaf():
        return
    t_branches = t.branches
    for b in t_branches:
        res = path_yielder(b, value)
        for lst in res:
            yield [t.label] + lst


# def path_yielder(t, value):
#     """Yields all possible paths from the root of t to a node with the label value
#     as a list.

#     >>> t1 = Tree(1, [Tree(2, [Tree(3), Tree(4, [Tree(6)]), Tree(5)]), Tree(5)])
#     >>> print(t1)
#     1
#       2
#         3
#         4
#           6
#         5
#       5
#     >>> next(path_yielder(t1, 6))
#     [1, 2, 4, 6]
#     >>> path_to_5 = path_yielder(t1, 5)
#     >>> sorted(list(path_to_5))
#     [[1, 2, 5], [1, 5]]

#     >>> t2 = Tree(0, [Tree(2, [t1])])
#     >>> print(t2)
#     0
#       2
#         1
#           2
#             3
#             4
#               6
#             5
#           5
#     >>> path_to_2 = path_yielder(t2, 2)
#     >>> sorted(list(path_to_2))
#     [[0, 2], [0, 2, 1, 2]]
#     """
#     lst = []
#     def helper(t, single_lst, value):
#         nonlocal lst
#         # print(single_lst)
#         if t.label == value:
#             lst.append(single_lst + [t.label])
#         if t.is_leaf():
#             return
#         t_branches = t.branches
#         for b in t_branches:
#             helper(b, single_lst + [t.label], value) 
#     helper(t, [], value)
#     yield from lst


t1 = Tree(1, [Tree(2, [Tree(3), Tree(4, [Tree(6)]), Tree(5)]), Tree(5)])
print(t1)
lst = path_yielder(t1, 5)
# print(next(lst))
# print(next(lst))
print(sorted(list(lst)))
# print(lst)


t2 = Tree(0, [Tree(2, [t1])])
print(t2)
path_to_2 = path_yielder(t2, 2)
print(sorted(list(path_to_2)))
# print(path_to_2)