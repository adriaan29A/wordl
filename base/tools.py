import sys
import math

# Odometer - tools
N = 5
BASE = 3

# Tuple indexes 
WORD        = 0
EXPECTED    = 1
FREQUENCY   = 1
COUNT       = 2

# input files
WORDLE_DATA_FILE                    = 'wd/1297_word_expected_values'
GOOGLE_330K_WORD_COUNTS             = 'wd/google_330k_word_counts'

# output files
COMBINED_1297_SORTED_EXPECTED       = 'wd/1297_combined_sorted_expected'
COMBINED_1297_SORTED_COUNTS         = 'wd/1297_combined_sorted_counts'
COMBINED_1297                       = 'wd/1297_combined'

class Hint:
    miss    = 0
    hit     = 1
    other   = 2     

def verify_pattern(pattern, target, source):
    """ 
    Given a pattern like '00120', a src string like 'women' and a target string 
    like 'roman' returns True if the target string matches the pattern given the 
    src string

    """
    n= len(pattern)
    res = True

    for i in range(n):

        if int(pattern[i]) == Hint.miss:
            if source[i] == target[i]:
                res = False; break
            else:
                if [j for j, c in enumerate(source) if target[i] == c]:
                    res = False; break
        elif int(pattern[i]) ==  Hint.hit:
            if source[i] != target[i]:
                res = False; break

        elif int(pattern[i]) == Hint.other:
            if source[i] == target[i]:
                res = False; break
            else:
                if not [j for j, c in enumerate(source) if target[i] == c]:
                    res = False; break

    return res


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

def generate_pattern(src, trgt):
    """ 
    Given two words like 'women', 'roman' (src, trgt), return the corresponding Wordle "hint" 
    encoded as a list of integers each taking on one of three enum values - hit, miss or other -
    for each character in the word - eg 20021  
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
            res += str(pattern[j])

    return res


def read_word_data(filename):
    """ 

    """
    words = []
    with open(filename) as f:
         lines = f.read().splitlines()
         f.close

    if filename == WORDLE_DATA_FILE:
        for line in lines:
            s = line.split(' ')
            t = tuple(((s[WORD], float(s[EXPECTED]))))
            words.append(t)

    elif filename == GOOGLE_330K_WORD_COUNTS:
        for line in lines:
            s = line.split('\t')
            t = tuple((s[WORD], int(s[1])))
            words.append(t)

    elif filename == COMBINED_1297_SORTED_EXPECTED:
        for line in lines:
            t = eval(line)
            words.append(t)

    elif filename == COMBINED_1297:
        for line in lines:
            t = eval(line)
            words.append(t)

    return words


def generate_expecteds():
    """ 
    Pre-compute expected values using Shannon's rule = sum(p(i) * log(1/p(i)))
    grep -E '^[[:alpha:]]{5}$'
    """
    words = read_word_data(WORDLE_DATA_FILE)
    n = len(words)
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
    
        # How to sort a list of tuples....
        # sorted_patterns = {key: val for key, val in sorted(raw_patterns.items(), 
        # key = lambda ele: ele[1], reverse=True)}

        print('{0:s} {1:n} {2:s} {3:2.5f}'.format(words[i][WORD], count, p, s))
        #print('word = {0:s}'.format(words[i][WORD]))
        #print( ('E(I) = {0:2.6f} bits'.format(s)) )
    # ?
    print('{0:s} {1:2.5f}'.format(words[i][0], s))


def generate_1297_counts():
    """

"""
    words330k = read_word_data(GOOGLE_330K_WORD_COUNTS)
    words1297 = read_word_data(WORDLE_DATA_FILE) 
    words1297_revised = []
    words330k_5 = []

    # Get 5 letter words & counts from the 330k corpus
    for w in words330k:
        if len(w[WORD]) == 5:
            t = (w[WORD], w[1])
            words330k_5.append(t)
    
    # O(N*M) operation.
    total_counts = 63150283289
    for w in words1297:
        t = next((v for i, v in enumerate(words330k_5) if v[WORD] == w[WORD]), None)
        if t != None:
            f = t[FREQUENCY]
            s = round((f / total_counts * math.log2(total_counts/ f)), 6) 
            w += (s,)
        else:
            w += (0,)
        print(w)
        words1297_revised.append(w)
        # total_counts += t[COUNT]


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

def iterate_and_do2():
    """
    Test function
    """
    matches = []
    words = read_word_data(WORDLE_DATA_FILE)
    for target in words:
        for source in words:
            pattern = [0] * N
            od = Odometer(pattern, BASE)
            for i in range(BASE**N):
                res = verify_pattern(od.digits, source[WORD], target[WORD] )
                if res:
                    print(od.digits, source[WORD], target[WORD])
                od.increment()


