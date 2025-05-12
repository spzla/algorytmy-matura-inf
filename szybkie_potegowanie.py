# Iteracyjnie
def fastpow_i(a, n):
    w = 1
    while n > 0:
        if n % 2 == 1:
            w *= a

        a *= a
        n //= 2
    return w

# Rekurencyjnie
def fastpow_r(a, n):
    if n == 0:
        return 1

    if n % 2 == 1:
        return a * fastpow_r(a, n - 1)

    w = fastpow_r(a, n // 2)
    return w * w

if __name__ == '__main__':
    print(fastpow_r(3, 33))