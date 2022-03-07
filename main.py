from selectionSort import SelectionSort
from BubbleSort import BubbleSort
from inersionSort import insertionSort

list_1 = [9, 4, 5, 6, 2, 3]
list_2 = [1, 4, 5, 6, 2, 3]

sort_selection = SelectionSort(list_2)
sort_bubble = BubbleSort(list_1)
sort_insertion = insertionSort(list_1)

# print("Bubble sort: ", sep="\n")
# sort_bubble.sort()
# sort_bubble.displayResult()
# print("\n \n")
#
# print("Selection sort: ", sep="\n")
# sort_selection.sort()
# sort_selection.displayResult()
# print("\n\n")

print("Insertion sort: ", sep="\n")
sort_insertion.sort()
sort_insertion.displayResult()
