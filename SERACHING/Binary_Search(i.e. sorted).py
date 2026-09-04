def Binary_search(arr, target):
    l = 0
    r = len(arr) - 1  # Initialize pointers

    while l <= r:
        mid = (l + r) // 2  # Find middle index

        if arr[mid] == target:
            return mid  # Target found

        if arr[mid] < target:
            l = mid + 1  # Search right half

        elif arr[mid] > target:
            r = mid - 1  # Search left half

    return "-1"  # Target not found


# Test the function
arr = [10, 25, 30, 45, 50, 90]
target = 90
result = Binary_search(arr, target)
print(result)  # Output: 5
