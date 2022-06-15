"""
class Foo:

    def fribble(x):
        print(x)

    def frooble(x):
        Foo.fribble(x)


Foo.frooble(10)

"""

class MyClass:

    """A simple example class"""
    i = 12345

    @staticmethod
    def rc():
        return 'goodbye world'

    @staticmethod
    def f(bar):
        print(bar)
        print("hello world")
        print(MyClass.rc())



c = MyClass()

mf = MyClass.f("bar")
print(mf)

mf = c.f('bar')
print(mf)
