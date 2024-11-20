import sys
sys.setrecursionlimit(30000000)
def bubblesort(l):
    a = 0
    i = 0
    n = 0
    v = 1
    while n < len(l) - 1:
        while i < len(l) - v:
            a = l[i]
            A = l[i + 1]
            if A > a:
                l[i] = A
                l[i + 1] = a
            i += 1
        i = 0
        n += 1
        v += 1

def insertionsort(l):
    i=1
    n=0
    q=0
    while i<len(l):
        n=i-1
        k=l[i]
        while l[n]>k and n>=0:
            l[n+1]=l[n]
            n -= 1
        l[n+1]=k
        i+=1

def selectionsort(l):
    n=0
    k=0
    while n<len(l):
        i=n+1
        q=l[n]
        while i<len(l):
            if l[i]<q:
                q=l[i]
                t=i
                k+=1
            i+=1
        if k>0:
            l[t]=l[n]
            l[n]=q
        t=0
        k=0
        n+=1

def quick_sort(l, low, high):
    if low < high:
        pivot_index = partition(l, low, high)
        quick_sort(l, low, pivot_index - 1)
        quick_sort(l, pivot_index + 1, high)

def partition(l, low, high):
    pivot = l[low]
    i = low + 1
    for j in range(low + 1, high + 1):
        if l[j] <= pivot:
            l[i], l[j] = l[j], l[i]
            i += 1
    l[low], l[i - 1] = l[i - 1], l[low]
    return i - 1
def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    leftHalf = arr[:mid]
    rightHalf = arr[mid:]

    sortedLeft = mergeSort(leftHalf)
    sortedRight = mergeSort(rightHalf)

    return merge(sortedLeft, sortedRight)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result