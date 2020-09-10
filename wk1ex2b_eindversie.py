"""
Titel voor je avontuur: De queeste naar taart.

Opmerkingen over hoe je het avontuuur kan "winnen" of "verliezen":
* kies de tafel om te winnen
* kies de deur om te verliezen
"""

import time


def adventure():
    """Runs one session of interactive fiction

    Well, it's "fiction," depending on the pill color chosen...

    arguments: no arguments (prompted text doesn't count as an argument)
    results: no results     (printing doesn't count as a result)
    """
    # zet deze waarde op 0.0 om te testen of snel te spelen,
    # ..of hoger voor meer dramatisch effect!
    delay = 0.0

    username = input("Hoe noemt men u, edele avonturier? ")

    print()
    print("Welkom,", username, "in het Libracomplex, een labyrint")
    print("van gewichtige wonderen en grote hoeveelheden ... taart!")
    print()
    print("Uw queeste: om een taart te vinden, en te eten! Daarnaast kunt u nog een drankje kiezen..")
    print()

    flavor = input("Welke smaak zoekt u? ")
    if flavor == "aardbeien":
        print("Uw wijsheid in taartkeuze is overweldigend!")
    elif flavor == "kersen":
        print("Een Limburgse klassieker: een goede keuze, avonturier!")
    elif flavor == "chocolade":
        print("Zou je dat wel doen?!")
    else:
        print("Ieder zijn smaak...")

    servet = input("Wilt u er een servet bij? ")
    if servet == "Ja" or servet == "ja":
        vouwen = input("wilt u het servet gevouwen? ")
        if vouwen == "Ja" or vouwen == "ja":
            print("Komt voor mekaar!")
        elif vouwen == "Nee" or vouwen == "nee":
            print("Dan niet, ook goed")
    
    drankje = input("Wilt u een warm of een koud drankje? ")
    if drankje == "warm" or drankje == "Warm":
        print("Daar warmt u lekker van op...")
    else:
        print("Lekker verfrissend!")
    
    if drankje == "warm" or drankje == "Warm":
        warme_drank = input("Wilt u koffie, thee of chocomelk? ")
        if warme_drank == "koffie" or warme_drank == "Koffie":
            print("Lekker, een caffeïneboost!")
        elif warme_drank == "thee" or warme_drank == "Thee":
            print("Hmmm, gezonde keuze") 
        else:
            print("Lekker met slagroom er op!!")
    

    print()
    print("Voorwaarts naar de queeste!\n\n")
    print("Een gang strekt zich voor u uit; in het gedimde licht ziet u")
    print("aan de ene kant een tafel met onduidelijke vormen en")
    print("materialen, en aan de andere kant een deur op een kier,")
    print("waarachter gelach --is dat gelach?-- van studenten klinkt.")

    time.sleep(delay)

    print()
    choice1 = input("Kiest u de tafel of de deur? [tafel/deur] ")
    print()

    if choice1 == "tafel":
        print("Als u de tafel benadert lijkt de onduidelijke massa")
        print("een steeds grotere vorm aan te nemen, tot ...")

        time.sleep(delay)

        print("... ze herkenbaar wordt als een grote stapel verpakte")
        print("taarten, het karton strak geplooid. Uw uitdaging --en")
        print("honger-- is op smakelijke wijze opgelost.")
        print()
        print("Tot ziens,", username, "!")
    else:
        print("U opent de deur en ziet een congregatie van wijze dames")
        print("en heren, die allen genieten van hun taken. Samenwerking")
        print("en vrolijkheid zijn hier in overvloed aanwezig, maar...")

        time.sleep(delay)

        print("...ze hebben ALLE taart opgegeten! Resten van dozen")
        print("liggen overal verspreid. U wordt duizelig en grijpt")
        print("naar een taart. Er is niets. U ademt uit en valt,")
        print("en ligt verslagen tussen de resten van dozen die u")
        print("langzaam bedekken tot verstikking volgt.")
        print()
        print("Vaarwel,", username, ".")
