""" 
Wordl

Helps you cheat playing Wordle

"""
import math
from enum import IntEnum
import scratch

N = 5
base = 3

WORD = 0
EXPECTED = 1

class Hint(IntEnum):
    miss    = 0
    hit     = 1
    other   = 2


def generate_pattern(src, trgt):
    """ 
    Given two words like 'women', 'roman' (src, trgt), return the corresponding Wordle "hint" 
    encoded as a list of integers each taking on one of three enum values - hit, miss or other -
    for each character in the word.  
    
    """
    pattern = [Hint.miss] * N

    for i in range(N):
        if trgt[i] != src[i]:
            hits = [j for j, c in enumerate(src) if c == trgt[i]]
            if len(hits) != 0:
                pattern[i] = Hint.other
        else:
            pattern[i] = Hint.hit

    res = ''
    for j in range(N):
            res += str(pattern[j].value)

    return res


def verify_pattern(pattern, target, source):
    """ 
    Given a pattern like '00120', a src string like 'women' and a target string 
    like 'roman' returns True if the target string matches the pattern given the 
    src string

    """
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


def filter_words(pattern, words, src):
    """ 

    """

    matches = []
    for target in words:
        if verify_pattern(pattern, src, target[WORD]):
            matches.append(target)

    return matches


class Tools:
    @classmethod
    def increment_and_mod(cls, digits, i):
        digits[i] = (digits[i] + 1) % base
        return digits[i] == 0

    @classmethod
    def increment(cls, digits):
        i = 0
        while i < N and cls.increment_and_mod(digits, i):
            i += 1
 
    @classmethod
    def digits_to_string(cls, digits):
        n = len(digits)
        s = ''
        for i in range(n):
            s += str(digits[i])
    
        return s

    @classmethod
    def iterate_and_do(cls, words, sourceterm):
    
        digits = [0] * N
        for i in range(base**N):
            pattern = cls.digits_to_string(digits)
            matches = filter_words(pattern, words, sourceterm)
            if (matches): 
                count = len(matches)
                print(pattern, count)

                if count > 15: count = 15
                for o in range(count):
                    print(matches[o], end=" ")
                print()
            else:
                print(pattern + " not matched!")

            cls.increment(digits)


def generate_expecteds(words):

    #sorted_patterns = {key: val for key, val in sorted(raw_patterns.items(), 
    #    key = lambda ele: ele[1], reverse=True)}

    n = len(words)
    expected = {}

    for i in range(n):
        
        patterns = {}

        for j in range(n):

            p = generate_pattern(words[i][WORD], words[j][WORD])

            if (p in patterns):
                patterns[p] += 1
            else:
                patterns[p] = 1

 
        nk = len(patterns.keys())
        print ("# keys=", nk)

        s = 0
        for p in patterns.keys():

            count = patterns[p]
            probability = count/n
            bits = math.log2(1/probability)
            s += probability*bits
    
        expected[words[i]] = s
        
        print('{0:s} {1:n} {2:s} {3:2.5f}'.format(words[i][WORD], count, p, s))
        print('word = {0:s}'.format(words[i][WORD]))
        print( ('E(I) = {0:2.6f} bits'.format(s)) )


    
    print('{0:s} {1:2.5f}'.format(words[i][0], s))
    

####################################################


words = []
matches = []

with open('words_bits.txt') as f:
     lines = f.read().splitlines()
     f.close


for line in lines:
    s = line.split(' ')
    t = tuple(((s[WORD], s[EXPECTED])))
    words.append(t)


Tools.iterate_and_do(words, 'slate')

#iad(words)
#verify_pattern1('20221', 'women', 'roman')
# generate_expecteds(words)

print ('Welcome to Wordl! You have 10 guesses, \'q\' to quit')

for i in range(10):

    line = input("Enter result: ")
    args = line.split(' ')
    if args[0][0] == 'q':
        break

    if not i: matches = words
    matches = filter_words(args[1], matches, args[0])
    count = len(matches)

#    if count > 100: count = 100

    for i in range(count):
        print(matches[i][WORD], end=" ")
        
    print()





