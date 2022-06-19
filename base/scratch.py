N = 5
BASE = 3


def myfunc(foo):
    print ("hello world")

class Odometer:

    def __init__(self, digits, base):
        self.digits = digits
        self. n = len(digits)
        self.base = base

    def increment_and_carry(self, i):
        self.digits[i] = (self.digits[i] + 1) % self.base
        return self.digits[i] == 0

    def increment(self):
        i = 0
        while self.increment_and_carry(i):
            i+=1
            if i == self.n: 
                break


"""
num = [0]*N; base = BASE
od = Odometer(num, BASE)

for i in range(base**N):
    print("num =", end=' ')
    print(od.digits)
    od.increment()
"""


