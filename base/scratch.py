def sum(n, acc):
    if n == 0:
        return acc
    else:
        return acc + sum(n - 1, n)


N = 5
digits = [0] * N
base = 10


def add_one_and_mod(digits, i):
    digits[i] = (digits[i] + 1) % base
    return digits[i] == 0

def increment(digits):
    i = 0
    while add_one_and_mod(digits, i):
        i += 1
 
for i in range(base**N - 1):
    increment(digits)
    print(digits)

"""
0 0

0 0 0 0 0        n div 3   n mod 3
0 0 0 0 1       n^2 div 3  n div 3 n mod 3 
0 0 0 0 2 

0 0 0 1 0
0 0 0 1 1
0 0 0 1 2

0 0 0 2 0 
0 0 0 2 1
0 0 0 2 2

0 0 1 0 0
0 0 1 0 1
0 0 1 0 2

0 0 1 1 0
0 0 1 1 1
0 0 1 1 2

0 0 1 2 0
0 0 1 2 1
0 0 1 2 2

0 0 2 0 0


"""

"""
with open('words') as f:
    lines = f.read().splitlines()
    f.close

words = []

for line in lines:
    s = line.split(' ')
    t = tuple(((s[0], '' if len(s) == 1 else s[1] )))
    words.append(t)

generate_expecteds(words)

#matches1 = filter_words('00022', matches, 'minor')
#matches2 = filter_words('21100', matches1, 'troll')
#matches3 = filter_words('21100', matches2, 'shock')


"""

"""
#sm = {key: val for key, val in sorted(matches, 
#    key = lambda ele: ele[1], reverse=True)}



#is_match('00001', 'women', 'linin')
#is_match('00201', 'women', 'fanny')
#matches = get_matches('00121', words, 'women')
#iterate_and_do(tokens)
"""
#print (get_pattern('target', 'source'))
#is_match('00002', 'monde', 'tares')
#is_match('00002', 'tares', 'monde')


    
    
