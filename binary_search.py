def binary_search(arr: list, n: int, l: int, p: int) -> int:
    while l <= p:
        sr = (l + p) // 2
        if arr[sr] == n:
            return sr

        if arr[sr] > n:
            p = sr - 1
        else:
            l = sr + 1

    return -1

if __name__ == '__main__':
    arr = [2, 5, 3, 0, 7, 1]
    arr.sort()

    print(binary_search(arr, 7, 0, len(arr) - 1))