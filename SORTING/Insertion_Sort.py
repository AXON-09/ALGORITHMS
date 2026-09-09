def Insertion_Sort(arr):
    n = len(arr)

    for i in range(1, n):
        temp = arr[i]
        j = i - 1

        while j >= 0:
            if arr[j] > temp:
                arr[j + 1] = arr[j]
            else:
                break
            j -= 1

        arr[j + 1] = temp

    return arr


arr = [1, 25, 12, 22, 11]

print(Insertion_Sort(arr))