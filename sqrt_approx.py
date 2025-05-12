def asqrt(n, eps):
    a = 1.
    b = n

    while abs(a - b) >= eps:
        a = (a + b) / 2
        b = n / a

    return (a + b) / 2

if __name__ == '__main__':
    print("sqrt(978) ~=", asqrt(978, 0.01))
    print("sqrt(64) ~=", asqrt(64, 0.01))