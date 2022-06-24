""" 
Wordl

Helps you cheat playing Wordle

"""
import math
import scratch

N = 5
BASE = 3

WORD = 0
EXPECTED = 1
RANK = 2

WORDLE_DATA_FILE                = "words_bits.txt"
WORD_EXPECTED_RANK_VALUES       = 'word_expected_rank_values.txt'
GOOGLE_20K_DATA_FILE            = '20k.txt'

DEFAULT_RANK, DEFAULT_EXPECTED  = 0, 0

class Hint:
    miss    = 0
    hit     = 1
    other   = 2     

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

    elif filename == GOOGLE_20K_DATA_FILE:
        rank = 0
        for word in lines:
            t = tuple((word, DEFAULT_EXPECTED, rank/(2*10**4)))
            rank += 1
            words.append(t)

    else: # WORD_EXPECTED_RANK_VALUES 
        for line in lines:
            t = eval(line)
            words.append(t)

    return words

def generate_rankings():
    """
    Many of the words in Wordle are junk words even if they yield valuable Shannon entropy
    values. Use the Google 20k ordered word list to generate rankings for words in the Wordle
    word list that are found in the 20k list. Set rank = 0 for Wordle list words that aren't in
    the 20k list.

    """
    t20k5 = []
    t20k = read_word_data(GOOGLE_20K_DATA_FILE)
    for t in t20k:
        if len(t[WORD]) == N:
            t20k5.append(t)

    twordl = read_word_data(WORDLE_DATA_FILE)
    for t in twordl:
        # This is performant (for Lists) and is the recommended way to do it.
        result = next((i for i, v in enumerate(t20k5) if v[WORD] == t[WORD]), None)
        if result != None:
            t += ((t20k5[result][RANK]),)
        else:
            t += (0,)
        print(t)


def generate_expecteds():
    """ 
    Pre-compute expected values using Shannon's rule = sum(p(i) * log(1/p(i)))
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

    print('{0:s} {1:2.5f}'.format(words[i][0], s))


def iterate_and_do():
    """
    Iterating over all patterns and for each word find all matching words and
    print them out. Some pattern, word combinations have no have no matches     

    """
    matches = []
    words = read_word_data(WORDLE_DATA_FILE)
    for word in words:

        pattern = [0] * N
        od = scratch.Odometer(pattern, BASE)
        for i in range(BASE**N):
            matches = filter_words(pattern, words, word[WORD])
            
            if (matches): 
                count = len(matches)
                print(pattern, count)
            
                if count > 15: count = 15
                for i in range(count):
                    print(matches[i], end=" ")
                print(); print()

            else:
                print(pattern, end = " ");  print(" not matched!")
            od.increment()

def iterate_and_do2():
    """

    """
    matches = []
    words = read_word_data(WORDLE_DATA_FILE)
    for target in words:
        for source in words:
            pattern = [0] * N
            od = scratch.Odometer(pattern, BASE)
            for i in range(BASE**N):
                res = verify_pattern(od.digits, source[WORD], target[WORD] )
                if res:
                    print(od.digits, source[WORD], target[WORD])
                od.increment()


def main():
    """ 
    Main:

    Usage: wordl <word> <pattern>
    eg:    wordl ozone 00122

    """
    print ('\nWelcome to Wordl! You have 6 guesses, \'q\' to quit')


    # User starts out with a guess on Wordle, followed by
    # inputting the result to the program in the form of
    # <word> <pattern> like "tacos" and pattern like 00211
    matches = []
    words = read_word_data(WORD_EXPECTED_RANK_VALUES)
    for i in range(6):

        line = input("\nWordl>: ")
        args = line.split(' ')
        if args[0][0] == 'q':
            break

        word = args[0]
        pattern = args[1]

        result =  next((v for k, v in enumerate(words) if v[WORD] == word), None)
        if not result: 
            print(word + ' is not in the dictionary!')
            break
        else:
            expectedbits = result[EXPECTED]

        if not i: 
            matches = words
 
        matches = filter_words(pattern, matches, args[0])
        count = len(matches)
        
        if count:
            actualbits = math.log2(count)
        else: actualbits = 1.0

        if count > 20: count = 20
        ranked_by_entropy = list(sorted(matches, 
             key = lambda ele: ele[EXPECTED], reverse = True))

        ranked_by_frequency = list(sorted(matches, 
             key = lambda ele: ele[RANK], reverse = True))

        print('\n\nWord:\t' + word + '\tPattern: ' + pattern )
        print('Expected Bits:\t' + str(expectedbits))
        print('Actual Bits:\t' + str(actualbits))
    
        print("\nExpected values and frequencies:\n"); 

        for j in range(count):
            en = ranked_by_entropy[j]
            fr = ranked_by_frequency[j]
            print('{0:s}  {1:1.2f}  {2:1.2f}   '.format(en[WORD], en[EXPECTED], en[RANK]), end=' ')
            print('{0:s}  {1:1.2f}  {2:1.2f}'.format(fr[WORD], fr[EXPECTED], fr[RANK]))
      



#iterate_and_do2()
main()
#generate_expecteds()
#iterate_and_do()
#generate_rankings()




