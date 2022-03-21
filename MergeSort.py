class MergeSort:
    def __init__(self, array):
        self.array = array
        self.first = 0
        self.last = len(array) - 1
        self.sort(self.first, self.last)
        self.displayResult()

    def sort(self, first, last):
        if first < last:
            mid = (last + first) // 2
            self.sort(first, mid)
            self.sort(mid + 1, last)
            for i in range(mid + 1):
                left = [0]
                left.append(self.array[i])
            for i in range(mid + 1, last + 1):
                right = [0]
                right.append(self.array[i])
            self.merge(left, right, self.array)

    def merge(self, left, right, result):
        len_left = len(left)
        len_right = len(right)
        i = j = 0
        result = [0]

        while i < len_left and j < len_right:
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        while i < len_left:
            result.append(left[i])
            i += 1
        while j < len_right:
            result.append(right[j])
            j += 1

    def displayResult(self):
        print("Sorted list: " + str(self.array), sep="\n")
