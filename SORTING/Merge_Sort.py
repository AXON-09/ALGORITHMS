class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        self.mergeSort(nums)
        return nums

    def mergeSort(self, arr: list[int]) -> None:
        if len(arr) <= 1:
            return

        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursive split
        self.mergeSort(left_half)
        self.mergeSort(right_half)

        # Merge step
        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
