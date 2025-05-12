def fibo(n: int):
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)

if __name__ == '__main__':
    print(f"20 element ciągu fibonacciego: {fibo(20)}")
    fibo_15 = [fibo(n) for n in range(15)]
    print("Pierwsze 15 elementów ciągu fibonacciego:", fibo_15)