# Programmeren I, Week 2 Opgave 3
# Bestandsnaam: wk2ex3.py
# groepje 3
# Problemomschrijving: Feest met functies!


#
# voorbeeldfunctie leng uit het college
#
def leng(s):
    """leng returns the length of s
       Argument: s, which can be a string or list
    """
    if s == '' or s == []:   # als lege string of lege lijst
        return 0
    else:
        return 1 + leng(s[1:])

def mult(n, m):
    """ mult vermenigdvuldigt n en m met elkaar en geeft resultaat terug maar maakt alleen gebruik van + en -
    arguments: integer or float
    """
    if n == 1: 
        return m
    else:
        return mult(n-1, m) + m

def dot(L, k):
    """ vermenigdvuldigt alle integers op dezelfde plaats met elkaar uit de lijst L en K
    arguments: integer
    """
    if len(L) != len(k):
        return 0.0
    elif L == [] or L == [0,0] or k == [0,0] or k == []:
        return 0.0
    else:
        return (L[0] * k[0]) + dot(L[1:], k[1:])
#
# Tests
#
assert dot([5, 3], [6, 4]) == 42.0
assert dot([1, 2, 3, 4], [10, 100, 1000, 10000]) == 43210.0
assert dot([5, 3], [6]) == 0.0
assert dot([], [6]) == 0.0
assert dot([], []) == 0.0

def ind(e, L, p =0):
    """ind moet de positie of index teruggeven waarop e voor het eerst voorkomt in L
    arguments: int, float, str
    """
    if e not in L: 
        return len(L)
    elif e in L:
        if L[p] == e:
            return p
        else:
            return ind(e, L, p+1)
            

def letter_score(let):
    """letter_score krijgt slecht 1 letter str als argument en geeft de bijbehorende scrabble score van deze letter terug int'
    arguments: string, integer
    """
    if let in "adeinorst":
        return 1
    elif let in "bcmp":
        return 3
    elif let in "f":
        return 5
    elif let in "ghl":
        return 2
    elif let in "jkuvw":
        return 4
    elif let in "xy":
        return 8
    elif let in "z":
        return 6
    elif let in "q":
        return 10
    else:
        return 0

def scrabble_score(s,t = 0,p = 0):
    """scrabble_score krijgt een str met kleine letters binnen en geeft als output de totale scrabble score terug van deze str
    agruments: str en int
    """
    if p == len(s):
        return t + letter_score(s[p])
    else:
        return scrabble_score(s,t,p+1)

def one_dna_to_rna(c):
    """Converts a single-character c from DNA nucleotide
    to complementary RNA nucleotide
    """
    if c == 'A':
        return 'U'
    elif c == 'C':
        return 'G'
    elif c == 'G':
        return 'C'
    elif c == 'T':
        return 'A'
    else:
        return ''
