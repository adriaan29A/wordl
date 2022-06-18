"""

import argparse



# let's put together a really fucked up class definition
def increment(self, foo):
  foo = foo + 1
  return foo
  
class X:

    # every instance method is virtual
    def decrement(self, foo):
        foo = foo - 1
        return foo

    def __init__(self, a, b):

        self.a = self.__increment(a) 
        self.b = self.decrement(b)

    # avoid name clashes for sub classes (non virtual)
    __increment = increment


class Y(X):

    # override method in the base class
    def decrement(self,foo):
        if foo != 0: foo = foo - 1
        return foo

x = X(2,1)
print(x.a)
print (x.b)

y = Y(2,1)
print (y.a)
print (y.b)
print ('-------------------')

parser = argparse.ArgumentParser()
parser.add_argument("--verbose", help="increase output verbosity",
                    action="store_true")
args = parser.parse_args()
if args.verbose:
    print("verbosity turned on")

def foo(bar):
    bar = bar + 1
    return bar

quux = foo(9)

print(quux)

class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)


fido = Dog('fido')
rover = Dog('rover')

fido.add_trick('jump')
rover.add_trick('rollover')

print(fido.name, rover.tricks)




class Mapping:

    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)


    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method


class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)


ml = [1,2,3,4,5]
m = Mapping(ml)


def f1(self, x, y):
    return min(x, x+y)

class C:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
        self.mag = (self.r**2 + self.i**2) ** (1/2)
        foo = self

    f = f1

    def g(self):
        return 'hello world'

    def real(self):
        return self.r

    h = g

    def imag(foo):
        return foo.i
        

    

c = C(5,7)

print(c.g())
print (c.r, c.i)
print (c.real())
print (c.imag())
#print (c.foo)


class MyClass:

    i = 12345

    def f(self):
        return 'hello world'


c = MyClass()
mf = MyClass.f
print(mf)

mf = c.f

#
# 
# 
#  
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

        self.mag = (self.r**2 + self.i**2) ** (1/2)


x = Complex(3.0, -4.5)
print(x.r, x.i)

# ghost function!
x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
#del x.counter
print(x.counter)
print(x.mag)


for i in range(0xFF, 0x0, -0x7):
    print(f'{format(i, "#04x")}')

#
#
#
#

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

print([[row[i] for row in matrix] for i in range(4)])

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
    print(transposed)

print(transposed)

print([(x, y) for x in [1,2,3] for y in [3,1,4] if x != y])

def test(**args):
    print(args)
    print(type(args))

test(**{'x':5, 'y':6})

d = {'x':5, 'y':6, 'z':7}
test(**d)


def compound(molecule):
    print(molecule)

# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

atom1 = {'x': 1, 'y': 2}
atom2 = {'x': 2, 'y': 3}


molecule1 = [atom1, atom2]
molecule2 = [{'x' : 1, 'y': 2}, {'x' : 3, 'y' : 4}]

compound(molecule1)


input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]
  
  
list_using_comp = [var for var in input_list if var % 2 == 0]
  
print("Output List using list comprehensions:",
   list_using_comp)


# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        print( users[user])


def example(a, /, b, *, c):
    print(a, b, c)

def example1(id, desc, /, date, *, c):
    print(id, desc, date, c)

def example2(id, *args, **keywds):
    print(id, args, keywds)

def example3(*args, **keywds):
    print(args, keywds)

example1(0, "this is point 0", "01, 11, 91", c = [(5, 1), (6, 2)])
example2(0, "this is point 0", "01, 11, 91", c = [(5, 1), (6, 2)])

example3('one', 'two', 'three', {'foo' : 1, 'bar' : 2})


example3('one', 'two', 'three', foo= 1, bar = 2)




Sieve of Erasthonese

N, M = 2, 1000
int_list = list(range(0, M))
primes = []

for i in range(N, M):
    for j in range(N * i, M, i):
        int_list[j] = 0
        if int_list[j-1] != 0:
            primes.append(j-1)

print(primes)

def standard_arg(arg):
    print(arg)

def pos_only_arg(arg, /):
    print(arg)

def kwd_only_arg(*, arg):
    print(arg)

def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)

# args = ['hello', 'goodbye', 'bonjour' 'au revoir']
# pos_only_arg(*args)
 
def combined_example(a, b, /, c = None, d=None, *, e, f):
    print(a, b, c, d)
    print (e, f)

def func2(a,b, *args, c=None, d=None, **kwargs): 
	print( a,b, args) 
	print('c=',c, 'd=', d, kwargs)

def func3(a, b, /, c=None, d=None, *, *e, f):
	print( a,b) 
	print(c, d, e, f)


combined_example(1, 2, c=3, d=4, e=5, f=6) 
func2(1, 2, 3, 4, c=6, d=7, e=8, f=9) 
func3(1, 2, 3, d=4, e=5, f=6) 
func4(1, 2, 3, 4, 10, 11, c=6, d=7, e=8, f=9) 

def combined_example2(a,b, /, *args, **kwargs):
    print(a, b, args, kwargs)

combined_example2(1,2,3,4, 5,6,7,8, d=9, e=10)

for i in range(n, m):
    for j in range(n*i, m, int_list[i]):
        print(i, j)

words = ['hello', 'goodbye', 'syonara']
for w in words:
    print(w, len(w))

# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status

"""








