class BinarySearch:
    @staticmethod
    def binary_search(arr, target, low, high):
        if low > high:
            return -1

        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return BinarySearch.binary_search(arr, target, mid + 1, high)
        else:
            return BinarySearch.binary_search(arr, target, low, mid - 1)
