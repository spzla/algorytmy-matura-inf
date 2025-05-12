def czynniki(n):
    czyn = []

    k = 2
    while n > 1 and k * k <= n: # optymalizacja - szukamy do pierwiastka z n
        while n % k == 0:
            czyn.append(k)
            n //= k
        k += 1

    return czyn

if __name__ == '__main__':
    print(czynniki(72))