def szukaj(tab: list):
    n = len(tab)
    if n >= 2:
        if tab[0] > tab[1]:
            MIN = tab[1]
            MAX = tab[0]
        else:
            MIN = tab[0]
            MAX = tab[1]

        for i in range(2, n - 1, 2):
            if tab[i] > tab[i + 1]:
                if tab[i] > MAX:
                    MAX = tab[i]
                if tab[i + 1] < MIN:
                    MIN = tab[i + 1]
            else:
                if tab[i + 1] > MAX:
                    MAX = tab[i + 1]
                if tab[i] < MIN:
                    MIN = tab[i]
    else:
        MIN = MAX = tab[0]

    return MIN, MAX

if __name__ == '__main__':
    lista = [2, 5, 3, 0, 7, 1]

    MIN, MAX = szukaj(lista)
    print("Lista:", lista, f"\nmin: {MIN}\nmax: {MAX}")
