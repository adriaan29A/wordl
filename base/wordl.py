""" 
Wordl

Helps you cheat playing Wordle

"""
import math
from enum import IntEnum

N = 5
base = 3

class Hint(IntEnum):
    miss    = 0
    hit     = 1
    reveal  = 2


def generate_pattern(src, trgt):
    """ 
    Given two words like 'women', 'roman' (src, trgt), return the corresponding Wordle "hint" 
    encoded as a list of integers each taking on one of three enum values - hit, miss or reveal -
    for each character in the word.  
    
    """
    pattern = [Hint.miss] * N

    for i in range(N):
        if trgt[i] != src[i]:
            hits = [j for j, c in enumerate(src) if c == trgt[i]]
            if len(hits) != 0:
                pattern[i] = Hint.reveal
        else:
            pattern[i] = Hint.hit


    res = ''
    for j in range(N):
            res += str(pattern[j].value)

    return res



def verify_pattern(pattern, target, source):
    """ 
    Given a pattern like '00120', a src like 'women' and a target like 'roman'
    returns True if the target string matches the pattern for the src string

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
            case Hint.reveal:
                if source[i] == target[i]:
                    b = False; break
                else:
                    idx = [j for j, c in enumerate(source) if target[i] == c]
                    if not idx:
                        b = False; break              

    return b

def filter_words(pattern, words, src):

    matches = []
    for target in words:
        if verify_pattern(pattern, src, target[0]):
            matches.append(target)

    return matches

def add_one_and_mod(digits, i):
    digits[i] = (digits[i] + 1) % base
    return digits[i] == 0

def increment(digits):
    i = 0
    while i < N and add_one_and_mod(digits, i):
        i += 1
 
def digits_to_string(digits):
    n = len(digits)

    s = ''
    for i in range(n):
        s += str(digits[i])
    
    return s


def iad(words):

    digits = [0] * N
    for i in range(base**N):
        pattern = digits_to_string(digits)
        sourceterm= 'slate'
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

        increment(digits)


def generate_expecteds(words):

    #sorted_patterns = {key: val for key, val in sorted(raw_patterns.items(), 
    #    key = lambda ele: ele[1], reverse=True)}

    n = len(words)
    expected = {}

    for i in range(n):
        
        patterns = {}

        for j in range(n):

            p = generate_pattern(words[i][0], words[j][0])

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
        
        print('{0:s} {1:n} {2:s} {3:2.5f}'.format(words[i][0], count, p, s))
        print('word = {0:s}'.format(words[i][0]))
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
    t = tuple(((s[0], s[1])))
    words.append(t)

#iterate_and_do(words)
#iad(words)
#verify_pattern1('20221', 'women', 'roman')

generate_expecteds(words)

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
        print(matches[i][0], end=" ")
        
    print()





