def horner_r(wsp: list, st, x):
    if st == 0:
        return wsp[0]

    return x * horner_r(wsp, st - 1, x) + wsp[st]

def horner_i(wsp: list, st, x):
    wynik = wsp[0]
    for i in range(1, st + 1):
        wynik = wynik * x + wsp[i]
    return wynik

if __name__ == '__main__':
    print("x^3 - 6x + 13x - 12  dla x = 3: ", horner_r([1, -6, 13, -12], 3, 3))
    print("x^3 - 6x + 13x - 12  dla x = 7: ", horner_r([1, -6, 13, -12], 3, 7))