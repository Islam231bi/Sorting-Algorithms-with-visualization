class MergeSort:
    def __init__(self, array):
        self.array = array
        self.sort(self.array)
        self.displayResult()

    def sort(self, array):
        if len(array) > 1:
            mid = len(array) // 2
            left = array[:mid]
            right = array[mid:]
            self.sort(left)
            self.sort(right)
            self.merge(left, right, array)

    def merge(self, left, right, result):
        len_left = len(left)
        len_right = len(right)
        i = j = k = 0

        while i < len_left and j < len_right:
            if left[i] <= right[j]:
                result[k] = left[i]
                i += 1
                k += 1
            else:
                result[k] = right[j]
                j += 1
                k += 1
        while i < len_left:
            result[k] = left[i]
            i += 1
            k += 1
        while j < len_right:
            result[k] = right[j]
            j += 1
            k += 1

    def displayResult(self):
        print("Sorted list: " + str(self.array), sep="\n")
