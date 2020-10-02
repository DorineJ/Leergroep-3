def rot(c, n):
    """rot zorgt er voor dat een enkel karakter c n stappen verplaatst in het alfabet
    arguments: str en int
    """
    if c.lower() not in "abcdefghijklmnopqrstuvwxyz":
        return c
    else:  
        if 'A' <= c <= 'Z' :
            rotation = chr((ord(c)-ord('A')+n) % 26 + ord('A'))
        else:            
            rotation = chr((ord(c)-ord('a')+n) % 26 + ord('a'))
        return rotation

assert rot("a", 2) == "c"
assert rot("y", 2) == "a"
assert rot("A", 3) == "D"
assert rot("Y", 3) == "B"
assert rot(" ", 4) == " "


def encipher(s, n):
    """encipher verplaatst alle karakters uit de str s n stappen uit het alfabet
    arguments: str en int
    """
    if len(s) == 0:
        return ""
    else:
        return rot( s[0], n) + encipher( s[1:], n) 


# tabel met kansen per letter
def letter_prob(c):
    """If c is an alphabetic character,
       we return its monogram probability (for Dutch),
       otherwise we return 1.0.  We ignore capitalization.
       Adapted from
       https://www.sttmedia.com/characterfrequency-nederlands
    """
    if c == 'e' or c == 'E':
        return 0.1909
    if c == 'n' or c == 'N':
        return 0.0991
    if c == 'a' or c == 'A':
        return 0.0769
    if c == 't' or c == 'T':
        return 0.0642
    if c == 'i' or c == 'I':
        return 0.0630
    if c == 'o' or c == 'O':
        return 0.0581
    if c == 'r' or c == 'R':
        return 0.0562
    if c == 'd' or c == 'D':
        return 0.0541
    if c == 's' or c == 'S':
        return 0.0384
    if c == 'l' or c == 'L':
        return 0.0380
    if c == 'h' or c == 'H':
        return 0.0312
    if c == 'g' or c == 'G':
        return 0.0312
    if c == 'k' or c == 'K':
        return 0.0279
    if c == 'm' or c == 'M':
        return 0.0256
    if c == 'v' or c == 'V':
        return 0.0224
    if c == 'u' or c == 'U':
        return 0.0212
    if c == 'j' or c == 'J':
        return 0.0182
    if c == 'w' or c == 'W':
        return 0.0172
    if c == 'z' or c == 'Z':
        return 0.0160
    if c == 'p' or c == 'P':
        return 0.0149
    if c == 'b' or c == 'B':
        return 0.0136
    if c == 'c' or c == 'C':
        return 0.0130
    if c == 'f' or c == 'F':
        return 0.0073
    if c == 'y' or c == 'Y':
        return 0.0006
    if c == 'x' or c == 'X':
        return 0.0005
    if c == 'q' or c == 'Q':
        return 0.0001
    return 1.0
     
def score(s): #berekent waarschijnlijkheid van string
    if len(s) == 0:
        return 1.0

    return letter_prob(s[0]) * score(s[1:])

def decipher(s):
    L = [encipher(s, n) for n in range(26)] #geeft alle mogelijke strings
    lists = [[score(x),x] for x in L] #geeft alle scores voor alle mogelijke strings
    return max(lists)  #kiest de beste optie aan de hand van de hoogste score

def blsort(L):
    """deze functie krijgt een lijst binnen met bineaire getallen en deze worden opeenlopend teruggegeven 
    in een nieuwe lijst 
    arguments: int
    """
    lc = [1 for x in L if x == 1] #geen count functie nodig kan gewoon hier in
    oc = [0 for x in L if x == 0]

    if len(L) == 0:
        return 0
    else:
        return oc + lc #geen haken nodig, maakt er zelf al een lijst van
    
    def gensort(L): #nog niet werkend
    """krijgt lijst en geeft dezelfde lijst terug maar dan in oplopende volgorde
    arguments: int of float
    """
    if len(L) == 0:
        return 0
    else:
        new_list = min(L) + L.remove(min(L)) + gensort(L[1:])
        return new_list
