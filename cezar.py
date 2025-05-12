def cezar(tekst: str, przes: int):
    szyfr = ""
    for lit in tekst.lower():
        nowa = ord(lit) - ord('a') + przes
        szyfr += chr(nowa % 26 + ord('a'))
    return szyfr

def cezar_keepcase(tekst: str, przes: int):
    szyfr = cezar(tekst, przes)
    nowy = ""
    for i in range(len(tekst)):
        if tekst[i].isupper():
            nowy += szyfr[i].upper()
        else:
            nowy += szyfr[i].lower()
    return nowy

print(cezar_keepcase("ABC", -1))