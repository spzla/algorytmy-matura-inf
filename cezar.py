def cezar(tekst: str, przes: int):
    szyfr = ""
    for lit in tekst.lower():
        nowa = ord(lit) - ord('a') + przes
        szyfr += chr(nowa % 26 + ord('a'))
    return szyfr

"""
Wariant który zachowuje małe i duże litery
"""
def cezar_keepcase(tekst: str, przes: int):
    szyfr = cezar(tekst, przes) # W tym miejscu implementacja funkcji cezara
    nowy = ""
    for i in range(len(tekst)):
        if tekst[i].isupper():
            nowy += szyfr[i].upper()
        else:
            nowy += szyfr[i].lower()
    return nowy

if __name__ == '__main__':
    print(cezar_keepcase("AbC", 13))