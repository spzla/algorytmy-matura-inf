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


print(onp("5 3 7 - 2 * 3 5 1 + * - * 3 -")) # -133
