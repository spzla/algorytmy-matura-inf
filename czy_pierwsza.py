from czynniki_pierwsze import czynniki

def czy_pierwsza(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1

    return True

"""
Możemy też sprawdzić pierwszość liczby po rozłożeniu jej na czynniki pierwsze - jak się nie rozkłada to jest pierwsza
"""
def czy_pierwsza_czynniki(n):
    return len(czynniki(n)) == 0

if __name__ == '__main__':
    print("91 pierwsza?", czy_pierwsza(91))