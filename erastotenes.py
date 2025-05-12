def erastotenes(n):
    tab = [True] * (n + 1)

    i = 2
    while i * i <= n:
        if tab[i]:
            for j in range(i * i, n + 1, i):
                tab[j] = False
        i += 1

    w = [i for i in range(2, len(tab)) if tab[i]] # zamiana tab na liczby

    return w

print("Pierwsze 100 liczb pierwszych:", erastotenes(100))