def zamiana(liczba, system):
    """
    Dla systemów liczbowych do base36 (0-9A-Z)
    :param liczba: int
    :param system: int
    :return:
    """
    pom = ""
    while liczba > 0:
        l = liczba % system
        if l >= 10 and l <= 36:
            pom += chr(ord('A') + (l - 10))
        else:
            pom += str(l)
        liczba //= system
    return pom[::-1]

def to_decimal(liczba_str: str, system):
    liczba_str = liczba_str.upper()
    w = 0
    for i in range(len(liczba_str)):
        v = 0
        if liczba_str[i].isnumeric(): # 0-9
            v = int(liczba_str[i])
        elif ord('A') <= ord(liczba_str[i]) <= ord('Z'): # A-Z
            v = ord(liczba_str[i]) - ord('A') + 10
        else:
            return
        if v >= system:
            return
        power = len(liczba_str) - i - 1
        w += v * (system ** power)
    return w

"""
Wersja uproszczona - dla systemów liczbowych od base2 do base9
"""
def zamiana9(liczba, system):
    pom = ""
    while liczba > 0:
        pom += str(liczba % system)
        liczba //= system
    return pom[::-1]

"""
Wersja uproszczona - dla systemów liczbowych od base2 do base9
"""
def to_decimal9(liczba_str: str, system):
    w = 0
    for i in range(len(liczba_str)):
        v = int(liczba_str[i])
        power = len(liczba_str) - i - 1
        w += v * (system ** power)
    return w