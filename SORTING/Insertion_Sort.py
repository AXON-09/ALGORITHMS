def Insertion_Sort(arr):
    n = len(arr)

    # Start from second element
    for j in range(1, n):
        temp = arr[j]  # Store current element

        # Compare with elements on the left
        for i in range(j-1, -1, -1):
            if temp < arr[i]:
                arr[i+1] = arr[i]  # Shift element right
                arr[i] = temp       # Insert temp
            else:
                arr[i+1] = temp     # Place temp
                break

    return arr  # Return sorted array


arr = [1, 25, 12, 22, 11]

print(Insertion_Sort(arr))