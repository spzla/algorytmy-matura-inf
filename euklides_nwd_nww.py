# Iteracyjna
def nwd_i(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp

    return a

# Rekurencyjna
def nwd_r(a, b):
    if b != 0:
        return nwd_r(b, a % b)
    return a

# NWW
def nww(a, b):
    return a * b / nwd_i(a, b)
