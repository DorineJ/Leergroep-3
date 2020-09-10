#
# wk1ex2a.py
#

import random          # importeer de module met de naam random


def rps():
    """ this plays a game of rock-paper-scissors in Dutch ("steen"-"papier"-"schaar")
        (or a variant of that game)
        arguments: no arguments    (prompted text doesn't count as an argument)
        results: no results        (printing doesn't count as a result)
    """
    user = input("Kies je wapen [steen, papier, schaar]: ")
    comp = random.choice(['steen', 'papier', 'schaar'])
    print()

    print('De gebruiker (jij) koos', user)
    print('De computer (ik)   koos', comp)
    print()

    if user == 'steen' and comp == 'papier':
        print('Helaas, je hebt verloren.')
    elif user == 'steen' and comp == 'schaar':
        print('Gefeliciteerd, je hebt gewonnen!')
    elif user == 'steen' and comp == 'steen':
        print('Wat toevallig!! Het is gelijkspel.')
    elif user == 'papier' and comp == 'schaar':
        print('Helaas, je hebt verloren.')
    elif user == 'papier' and comp == 'papier':
        print('Wat toevallig!! Het is gelijkspel.')
    elif user == 'papier' and comp == 'steen':
        print('Gefeliciteerd, je hebt gewonnen!')
    elif user == 'schaar' and comp == 'steen':
        print('Helaas, je hebt verloren')
    elif user == 'schaar' and comp == 'papier':
        print('Gefeliciteerd, je hebt gewonnen!')
    else:
        print('Wat toevallig, het is gelijkspel!')

    print("Het spel is afgelopen...")
