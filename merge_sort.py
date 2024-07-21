class MergeSort:
    @staticmethod
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        left_half = MergeSort.merge_sort(left_half)
        right_half = MergeSort.merge_sort(right_half)

        return MergeSort.merge(left_half, right_half)

    @staticmethod
    def merge(left, right):
        result = []
        left_index, right_index = 0, 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index].lower() < right[right_index].lower():
                result.append(left[left_index])
                left_index += 1
            else:
                result.append(right[right_index])
                right_index += 1

        result.extend(left[left_index:])
        result.extend(right[right_index:])
        return result
