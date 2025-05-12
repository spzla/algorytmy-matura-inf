def f(x):
    return x**3 - 3*x**2 + 2*x-6

def polowienie_i(a, b, epsilon):
    if f(a) == 0: return a
    if f(b) == 0: return b

    while b - a > epsilon:
        srodek = (a + b) / 2
        if f(srodek) == 0.0:
            return srodek

        if f(a) * f(srodek) < 0:
            b = srodek
        else:
            a = srodek

    return (a + b) / 2

def polowienie_r(a, b, epsilon):
    if f(a) == 0: return a
    if f(b) == 0: return b

    srodek = (a + b) / 2

    if b - a <= epsilon: return srodek

    if f(a) * f(srodek) < 0:
        return polowienie_r(a, srodek, epsilon)

    return polowienie_r(srodek, b, epsilon)

print(polowienie_r(-10, 10, 0))