def asqrt(n, eps):
    a = 1.
    b = n

    while abs(a - b) >= eps:
        a = (a + b) / 2
        b = n / a

    return (a + b) / 2

print(asqrt(64, 0.01))