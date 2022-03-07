"""
Time complexity: O(N^2)
Space complexity: O(1)
Best case: O(N)
"""


class insertionSort:

    def __init__(self, array):
        self.array = array
        self.size = len(self.array)
        self.passes = 0
        self.swaps = 0
        self.comparisons = 0

    def sort(self):
        for i in range(1, self.size):
            key = self.array[i]
            self.passes += 1
            j = i-1
            while j >= 0 and self.array[j] > key:
                self.array[j+1] = self.array[j]
                j -= 1
            self.array[j+1] = key

    def displayResult(self):
        print("Sorted list: " + str(self.array), sep="\n")
        # number of passes: N-1
        print("Passes count: " + str(self.passes), sep="\n")
