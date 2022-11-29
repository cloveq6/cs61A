class Account:
    """An account has a balance and a holder.
    All accounts share a common interest rate.

    >>> a = Account('John')
    >>> a.holder
    'John'
    >>> a.deposit(100)
    100
    >>> a.withdraw(90)
    10
    >>> a.withdraw(90)
    'Insufficient funds'
    >>> a.balance
    10
    >>> a.interest
    0.02
    >>> Account.interest = 0.04
    >>> a.interest
    0.04
    """

    interest = 0.02  # A class attribute

    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 0

    def deposit(self, amount):
        """Add amount to balance."""
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        """Subtract amount from balance if funds are available."""
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        return self.balance



# tom_account = Account('Tom')
# sun_account = Account('sun')
# print(tom_account.interest)
# tom_account.interest = 0.01
# print(tom_account.interest)
# print(sun_account.interest)


def naturals():
    """A generator function that yields the infinite sequence of natural
    numbers, starting at 1.

    >>> m = naturals()
    >>> type(m)
    <class 'generator'>
    >>> [next(m) for _ in range(10)]
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    i = 1
    while True:
        yield i
        i += 1

def scale(it, multiplier):
    """Yield elements of the iterable it scaled by a number multiplier.

    >>> m = scale([1, 5, 2], 5)
    >>> type(m)
    <class 'generator'>
    >>> list(m)
    [5, 25, 10]

    >>> m = scale(naturals(), 2)
    >>> [next(m) for _ in range(5)]
    [2, 4, 6, 8, 10]
    """
    "*** YOUR CODE HERE ***"
    yield from map(lambda x: x * multiplier, it)


   
   
# m = scale([1, 5, 2], 5)
# print(type(m))
# print(list(m))

# m = scale(naturals(), 2)
# print([next(m) for _ in range(5)])


def hailstone(n):
    """
    >>> for num in hailstone(10):
    ...     print(num)
    ...
    10
    5
    16
    8
    4
    2
    1
    """
    "*** YOUR CODE HERE ***"
    yield n
    if n % 2 == 0:
        yield from hailstone(n // 2)
    elif n == 1:
        pass
    else:
        yield from hailstone(n * 3 + 1)    


# print(list(hailstone(1)))
# print(list(hailstone(25)))

# for num in hailstone(10):
#     print(num)

class A:
    z = -1
    def f(self, x):
        return B(x-1)

class B(A):
    n = 4
    def __init__(self, y):
        if y:
            self.z = self.f(y)
        else:
            self.z = C(y+1)


class C(B):
    def f(self, x):
        return x


# a = A()
# b = B(1)
# b.n = 5
# print(C(2).n)
# print(C(2).z)
# print(a.z == C.z)
# print(a.z == b.z)
# print(b.z.z.z)
  
    
def WWPD():
    """What would Python Display?

    >>> a = A()
    >>> b = B(1)
    >>> b.n = 5
    >>> C(2).n
    4
    >>> C(2).z
    2
    >>> a.z == C.z
    True
    >>> a.z == b.z
    False
    >>> b.z.z.z
    1
    """
    
class Car(object):
    num_wheels = 4
    gas = 30
    headlights = 2
    size = 'Tiny'

    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.color = 'No color yet. You need to paint me.'
        self.wheels = Car.num_wheels
        self.gas = Car.gas

    def paint(self, color):
        self.color = color
        return self.make + ' ' + self.model + ' is now ' + color

    def drive(self):
        if self.wheels < Car.num_wheels or self.gas <= 0:
            return 'Cannot drive!'
        self.gas -= 10
        return self.make + ' ' + self.model + ' goes vroom!'

    def pop_tire(self):
        if self.wheels > 0:
            self.wheels -= 1

    def fill_gas(self):
        self.gas += 20
        return 'Gas level: ' + str(self.gas)
    
    
class MonsterTruck(Car):
    size = 'Monster'

    def rev(self):
        print('Vroom! This Monster Truck is huge!')

    def drive(self):
        self.rev()
        return Car.drive(self)

# deneros_car = Car('Tesla', 'Model S')
# print(deneros_car.model)

# deneros_car.gas = 10
# print(deneros_car.drive())
# print(deneros_car.drive())
# print(deneros_car.fill_gas())
# print(deneros_car.gas)
# print(Car.gas)

# deneros_car = Car('Tesla', 'Model S')
# deneros_car.wheels = 2
# print(deneros_car.wheels)
# print(Car.num_wheels)
# print(deneros_car.drive())
# # print(Car.drive()) # missing 1 required positional argument: 'self'
# print(Car.drive(deneros_car))


# deneros_car = MonsterTruck('Monster', 'Batmobile')
# print(deneros_car.drive())
# print(Car.drive(deneros_car))
# print(MonsterTruck.drive(deneros_car))
# print(Car.rev(deneros_car))


class A:
    interest = 1
    def fun(self):
        print(self.interest)
        
    
    
class B(A):
    interest = 2
    def fun(self):
        print(self.interest)
    
    
a = A()
b = B()
a.fun()
b.fun()
    
    
    