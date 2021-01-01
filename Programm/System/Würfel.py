from random import randint

def würfeln():
    würfelEins = randint(1,6)
    würfelZwei = randint(1,6)
    return (würfelEins, würfelZwei)

ergebnis = würfeln()
print(ergebnis[0], ergebnis[1])