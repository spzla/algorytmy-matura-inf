"""
Wydawanie reszty
"""
"""
Szybsza
"""
def reszta1(n):
    nominaly = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    reszt = []

    i = 0
    while n > 0:
        if n >= nominaly[i]:
            reszt.extend([nominaly[i]] * (n // nominaly[i]))
            n %= nominaly[i]
        i += 1

    return reszt

"""
Wolniejsza
"""
def reszta2(n):
    nominaly = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    reszt = []

    i = 0

    while n > 0:
        if n >= nominaly[i]:
            reszt.append(nominaly[i])
            n -= nominaly[i]
        else:
            i += 1

    return reszt

"""
Z funkcja divmod
"""
def reszta_divmod(n):
    nominaly = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    reszt = []

    for nom in nominaly:
        ile, n = divmod(n, nom)
        """Alternatywa"""
        # ile = n // nom
        # n %= nom

        reszt.extend([nom] * ile)

    return reszt

if __name__ == '__main__':
    print(f"Reszta z 784: {reszta1(784)}")
    print(f"Reszta z 1848: {reszta2(1848)}")
    print(f"Reszta z 999: {reszta_divmod(999)}")