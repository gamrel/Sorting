from Sorting.sort import *
import random
from time import time
for i in range(1, 9):
    n = 10 ** i
    l = [random.randint(1, 100) for _ in range(n)]
    arr = l
    print("Number of elements:", n)
    start_time = time()
    bubble_sorted_list = bubblesort(l.copy())
    print("Bubble sort time:", time() - start_time)
    start_time = time()
    insertion_sorted_list = insertionsort(l.copy())
    print("Insertion sort time:", time() - start_time)
    start_time = time()
    selection_sorted_list = selectionsort(l.copy())
    print("Selection sort time:", time() - start_time)
    start_time = time()
    sorted_list = sorted(l.copy())
    print("Sorted time:", time() - start_time)
    start_time = time()
    merge_sorted_list = mergeSort(l.copy())
    print("Merge sort time:", time() - start_time)
    start_time = time()
    low=0
    high=n-1
    quick_sorted_list = quick_sort(l.copy(),low,high)
    print("Quick sort time:", time() - start_time)