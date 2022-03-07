class SelectionSort:

    def __init__(self, array):
        self.array = array
        self.size = len(self.array)
        self.passes = 0
        self.swaps = 0
        self.comparisons = 0

    def sort(self):
        for i in range(self.size-1):
            i_min = i
            self.passes += 1
            for j in range(i + 1, self.size):
                if self.array[j] < self.array[i_min]:
                    i_min = j
                    self.comparisons += 1
            if i != i_min:
                (self.array[i], self.array[i_min]) = (self.array[i_min], self.array[i])
                self.swaps += 1

    def displayResult(self):
        print("Sorted list: " + str(self.array), sep="\n")
        # number of passes: N-1
        print("Passes count: " + str(self.passes), sep="\n")
        # O(N) number of swaps
        print("Swaps count: " + str(self.swaps), sep="\n")
        # O(N^2) number of comparisons
        print("Comparisons count: " + str(self.comparisons), sep="\n")
