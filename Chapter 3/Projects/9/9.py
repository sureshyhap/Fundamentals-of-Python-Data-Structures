lyst = [6, 1, 5, 2, 8, 5, 1, 1, 2, 1, 5, 9, 8]

def quicksort(lyst, size):
    quick_sort(lyst, 0, size - 1)

def quick_sort(lyst, left, right):
    if left >= right:
        return
    mid = (left + right) // 2
    pivot = lyst[mid]
    lyst[mid], lyst[right] = lyst[right], lyst[mid]
    i = left
    j = right - 1
    while i < j:
        while lyst[i] < pivot:
            i += 1
        while (lyst[j] > pivot) and (j > i):
            j -= 1
        if i < j:
            lyst[i], lyst[j] = lyst[j], lyst[i]
    lyst[i], lyst[right] = lyst[right], lyst[i]
    quick_sort(lyst, left, mid - 1)
    quick_sort(lyst, mid + 1, right)
    

quicksort(lyst, len(lyst))
print(lyst)

########################### ?????????? ###################
