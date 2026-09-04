def Binary_search(arr, target):
    l = 0
    r = len(arr)-1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            l = mid + 1
        elif arr[mid] > target:               #else:
            r = mid - 1
    return -1




arr = [10, 25, 30, 45, 50, 90]
target = 90

result = Binary_search(arr, target)

print(result)