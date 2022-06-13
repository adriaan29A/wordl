import math

N = 5
base = 3


def generate_pattern(source, target):

    mask = ['0','0','0','0','0']

    for i in range(5):
        if target[i] != source[i]:
            idxs = [j for j, c in enumerate(source) if c == target[i]]
            if len(idxs) != 0:
                mask[i] = '2'
        else:
            mask[i] = '1'

    st = ''
    for j in range(5):
        st += mask[j]

    return st


def verify_pattern(pattern, target, source):
    """ 
    Given a pattern like '00120', a src like 'women' and a target like 'roman'
    returns True if the target string matches the pattern for the src string
    """

    n= len(pattern)
    b = True

    for i in range(n):

        if pattern[i] == '0':
            if source[i] == target[i]:
                b = False; break
            else:
                idx = [j for j, c in enumerate(source) if target[i] == c]
                if idx:
                    b = False; break

        elif pattern[i] == '1':
            if source[i] != target[i]:
                b = False; break
 
        elif pattern[i] == '2':
            if source[i] == target[i]:
                b = False; break
            else:
                idx = [j for j, c in enumerate(source) if target[i] == c]
                if not idx:
                    b = False; break

    return b



def filter_words(pattern, words, source):

    matches = []
    for target in words:
        if verify_pattern(pattern, source, target[0]):
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
iad(words)


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





