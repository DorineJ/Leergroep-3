def sq(x):
    """Kwadraat van x
    para x: de waarde die in kwadraat moet
    type x: int of float
    rtype x: int of float
    """
    return x*x

def interp(low, hi, fraction):
    """het verschil tussen hi en low keer fraction + low 
    """
    return ((hi-low) * fraction) + low

def checkend(s): 
    """de functie checkt of het laatste karakter van de string gelijk is aan de eerste
    para s: de string waarbij het eerste en laatste karakter gelijk moeten zijn
    type s: str
    rtype s: str
    """
    if s[0] == s[-1]:
        return True
    else:
        return False

def flipside(s):
    """splitst de string door de helft en draait de helften om
    para s: 
    type s: str
    rtype s: str
    """
    eerste_l = len(s) // 2
    tweede_l = len(s) - eerste_l
    return s[eerste_l:] + s[:eerste_l]

def convert_from_seconds(s):
    """seconden worden omgezet naar dagen, uren, minuten en seconden
    para s: reserende aantallen niet totaal
    type s: int of float
    rtype s: int of float
    """
    days = s // (24 * 60 * 60)
    s = s % (24 * 60 * 60)
    hours = s // (60 * 60)
    s = s % (60 * 60)
    minutes = s // 60
    seconds = s % 60
    return [days, hours, minutes, seconds]
