def bubble(arr: list):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[j] > arr[i]:
                temp = arr[j]
                arr[j] = arr[i]
                arr[i] = temp
    return arr

def insertion(arr: list):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp

if __name__ == '__main__':
    lista = [2, 5, 3, 0, 7, 1]

    insertion(lista)
    print(lista)
