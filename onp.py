"""
https://www.algorytm.edu.pl/algorytmy-maturalne/onp
"""

def onp(dstr: str):
    d = dstr.split()
    stack = []

    for m in d:
        if m.isnumeric():
            stack.append(int(m))
        elif m in ['+', '-', '*', '/']:
            b = stack.pop()
            a = stack.pop()
            if m == '+':
                stack.append(a + b)
            elif m == '-':
                stack.append(a - b)
            elif m == '*':
                stack.append(a * b)
            elif m == '/':
                stack.append(a / b)

    return stack[0]

if __name__ == '__main__':
    print("(4 7 -) =", onp("4 7 -")) # -3
    print("(4 2 8 - *) =", onp("4 2 8 - *")) # -24
    print("(2 4 + 4 6 - *) =", onp("2 4 + 4 6 - *")) # -12
    print("(5 3 7 - 2 * 3 5 1 + * - * 3 -) =", onp("5 3 7 - 2 * 3 5 1 + * - * 3 -")) # -133
