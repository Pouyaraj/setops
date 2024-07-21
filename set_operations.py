from file_handler import FileHandler
from merge_sort import MergeSort

class SetOperations:
    def __init__(self, file1, file2, operation):
        self.file1 = file1
        self.file2 = file2
        self.operation = operation

    def perform_operation(self):
        words1 = FileHandler.read_file_to_words(self.file1)
        words2 = FileHandler.read_file_to_words(self.file2)

        to_lower_recursive = lambda words: list(map(lambda x: to_lower_recursive(x) if isinstance(x, list) else x.lower(), words))
        words1_lower = to_lower_recursive(words1)
        words2_lower = to_lower_recursive(words2)

        words1_sorted = MergeSort.merge_sort(words1_lower)
        words2_sorted = MergeSort.merge_sort(words2_lower)

        if self.operation == 'difference':
            result = self.difference_recursive(words1_sorted, words2_sorted)
        elif self.operation == 'union':
            result = list(set(words1_sorted) | set(words2_sorted))
        elif self.operation == 'intersection':
            result = list(set(words1_sorted) & set(words2_sorted))
        else:
            print("Invalid operation specified.")
            return None

        return set(result)

    @staticmethod
    def difference_recursive(list1, list2):
        if not list1:
            return []
        if list1[0] not in list2:
            return [list1[0]] + SetOperations.difference_recursive(list1[1:], list2)
        else:
            return SetOperations.difference_recursive(list1[1:], list2)
