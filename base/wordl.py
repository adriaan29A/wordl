""" 
Cheatle

Helps you cheat playing Wordle


"""
import math
from tools import Hint, read_word_data, filter_words, WORDLE_DATA, WORD, EXPECTED, COUNT


def main():
    """ 
    Main:

    Usage: cheatle <word> <pattern>
    eg:    cheatle ozone 00122

    """
    # User starts out with a guess on Wordle, followed by inputting the result to the program in the form of
    # <word> <pattern> like "tacos" and pattern like 00211
    matches = []
    words = read_word_data(WORDLE_DATA)
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

        if count > 15: count = 15
        ranked_by_entropy = list(sorted(matches, 
             key = lambda ele: ele[EXPECTED], reverse = True))

        ranked_by_frequency = list(sorted(matches, 
             key = lambda ele: ele[COUNT], reverse = True))

        print('\n\nWord:\t' + word + '\tPattern: ' + pattern )
        print('Expected Bits:\t' + str(expectedbits))
        print('Actual Bits:\t' + str(actualbits))
    
        print("\nExpected values and frequencies:\n"); 

        for j in range(count):
            en = ranked_by_entropy[j]
            fr = ranked_by_frequency[j]
            print('{0:s}  {1:1.2f}  {2:1.2f}   '.format(en[WORD], en[EXPECTED], en[COUNT]), end=' ')
            print('{0:s}  {1:1.2f}  {2:1.2f}'.format(fr[WORD], fr[EXPECTED], fr[COUNT]))
      
main()
#doSort()
#generate_entropies()
#generate_expecteds()
#iterate_and_do2()
#iterate_and_do()






