def vowlToConsonantRatio(word):
    numv = 0; numc = 0
    for c in word:
        if (c == 'a' or (c == 'e') or (c == 'i') or (c == 'o') or (c == 'u')):
            numv += 1
        else:
            numc += 1
    return numv / numc



COMPUTED = 3
VCR = 4
def rank_words():

    freqs = { 'a': 7.8, 'b': 2, 'c': 4, 'd': 3.8, 'e': 11, 'f': 1.4, 'g': 2, 'h': 2.6,
        'i': 8.6, 'j': .21, 'k': .97, 'l': 5.3, 'm': 2.7,  'n': 7.2, 'o': 6.1, 'p': 2.8,
        'q': .19, 'r': 7.3, 's': 8.7, 't': 6.7, 'u': 3.3, 'v': 1, 'w': .91, 'x': .27, 
        'y': 1.6, 'z': .44 }

    word_data_prev_format = read_word_data(WORD_EXPECTED_RANK_VALUES)
    word_data_new_format = []

    for wd in word_data_prev_format:
        w = wd[WORD]
        ord = 0.0
        for c in w:
            ord = ord + freqs[c] / 49 # 49 is the max

        vcr = vowlToConsonantRatio(w)
        wd = wd + (ord, )
        wd = wd + (vcr, )
        word_data_new_format.append(wd)

    sorted_words_new_format = list(sorted(word_data_new_format, 
        key = lambda ele: ele[RANK], reverse = True))

    for wd in sorted_words_new_format:
        print('{0:s}    {1:3.2f}   {2:3.2f}   {3:3.2f}   {4:3.2f}'.format(
            wd[WORD], wd[EXPECTED], wd[RANK], wd[COMPUTED], wd[VCR]))



rank_words()
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

  