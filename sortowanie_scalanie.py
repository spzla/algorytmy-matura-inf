"""
https://www.youtube.com/watch?v=ZRPoEKHXTJg
"""

def scal(arr: list, pom: list, lewy: int, srodek: int, prawy: int):
    for i in range(lewy, prawy + 1):
        pom[i] = arr[i]

    i = lewy
    j = srodek + 1

    for k in range(lewy, prawy + 1):
        if i <= srodek:
            if j <= prawy:
                if pom[j] < pom[i]:
                    arr[k] = pom[j]
                    j += 1
                else:
                    arr[k] = pom[i]
                    i += 1
            else:
                arr[k] = pom[i]
                i += 1
        else:
            arr[k] = pom[j]
            j += i


def sortowanie_scalanie(arr: list, pom: list, lewy: int, prawy: int):
    if prawy <= lewy: return

    srodek = (prawy + lewy) // 2

    sortowanie_scalanie(arr, pom, lewy, srodek)
    sortowanie_scalanie(arr, pom, srodek + 1, prawy)

    scal(arr, pom, lewy, srodek, prawy)

if __name__ == '__main__':
    lista = [2, 5, 3, 0, 7, 1]
    pom = [0] * len(lista)

    sortowanie_scalanie(lista, pom, 0, len(lista) - 1)

    print(lista)