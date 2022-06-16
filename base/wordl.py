""" 
Wordl

Helps you cheat playing Wordle

"""
import math
from enum import IntEnum

N = 5
BASE = 3

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
    Given a pattern like 00102, a list of (word, expected value) tuples and a candidate
    (target) word returns the list of words that match that combination of pattern and word.
    """
    matches = []
    for target in words:
        if verify_pattern(pattern, src, target[WORD]):
            matches.append(target)

    return matches

"""
This is inelegant but I don't want to break it into a separate module. I guess.
"""
class Tools:

    @staticmethod
    def increment_and_mod(pattern, i):
        pattern[i] = (pattern[i] + 1) % BASE
        return pattern[i] == 0

    @staticmethod
    def increment(pattern):
        i = 0
        while i < N and Tools.increment_and_mod(pattern, i):
            i += 1
 
    @staticmethod
    def pattern_to_string(pattern):
        n = len(pattern)
        s = ''
        for i in range(n):
            s += str(pattern[i])
    
        return s

    @staticmethod
    # Why this class exists
    def iterate_and_do(words, sourceterm):
    
        pattern = [Hint.miss] * N
        for i in range(BASE**N):

            pattern_str = Tools.pattern_to_string(pattern)
            matches = filter_words(pattern_str, words, sourceterm)

            if (matches): 
                count = len(matches)
                print(pattern, count)

                if count > 15: count = 15
                for i in range(count):
                    print(matches[i], end=" ")
                print()

            else:
                print(pattern + " not matched!")

            Tools.increment(pattern)


def generate_expecteds(words):
    """ 
    Pre-compute expected values. 
    Todo: Use word frequency lists, columnized output, better UI, performance
    
    This will prove useful in the future maybe.
    sorted_patterns = {key: val for key, val in sorted(raw_patterns.items(), 
        key = lambda ele: ele[1], reverse=True)}

    """
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
    

################################################################################


print ('Welcome to Wordl! You have 10 guesses, \'q\' to quit')

words = []
matches = []

with open('words_bits.txt') as f:
     lines = f.read().splitlines()
     f.close

# Twiddle this depending on info in file
for line in lines:
    s = line.split(' ')
    t = tuple(((s[WORD], s[EXPECTED])))
    words.append(t)


# User starts out with a guess on Wordle, followed by
# inputting the result to the program in the form of
# <word> <pattern> like "tacos" and pattern like 00211
for i in range(10):

    line = input("Enter result: ")
    args = line.split(' ')
    if args[0][0] == 'q':
        break

    if not i: 
        matches = words

    matches = filter_words(args[1], matches, args[0])
    count = len(matches)


    for i in range(count):
        print(matches[i][WORD], end=" ")
        
    print()
