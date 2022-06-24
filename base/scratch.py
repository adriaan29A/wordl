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
    def verify_pattern(pattern, target, source):
    n= len(pattern)
    b = True

    for i in range(n):

        match int(pattern[i]):
            case Hint.miss:
                if source[i] == target[i]:
                    b = False; break
                else:
                    idx = [j for j, c in enumerate(source) if target[i] == c]
                    if idx:
                        b = False; break
            case Hint.hit:
                if source[i] != target[i]:
                    b = False; break
            case Hint.other:
                if source[i] == target[i]:
                    b = False; break
                else:
                    idx = [j for j, c in enumerate(source) if target[i] == c]
                    if not idx:
                        b = False; break              

    
    return b
"""