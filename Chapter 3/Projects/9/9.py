import random, time

def make_random_list(size):
    lyst = []
    for i in range(size):
        while True:
            num = random.randint(1, size)
            if not num in lyst:
                lyst.append(num)
                break
    return lyst
    

def insertion_sort(lyst):
    size = len(lyst)
    i = 1
    while i < size:
        elem = lyst[i]
        j = i - 1
        while elem < lyst[j] and j >= 0:
            lyst[j + 1] = lyst[j]
            j -= 1
        lyst[j + 1] = elem
        i += 1
        

def quick_sort(lyst, left, right):
    if (right - left) < 50:
        insertion_sort(lyst)
    elif left < right:
        mid = (left + right) // 2
        lyst[mid], lyst[right] = lyst[right], lyst[mid]
        pivot = lyst[right]
        i = left
        j = right
        while i < j:
            while lyst[i] < pivot:
                i += 1
            while (lyst[j] > pivot) and (j > i):
                j -= 1
            if i < j:
                lyst[i], lyst[j] = lyst[j], lyst[i]
                i += 1
                j -= 1
        lyst[i], lyst[right] = lyst[right], lyst[i]
        quick_sort(lyst, left, mid - 1)
        quick_sort(lyst, mid + 1, right)

        
lyst = make_random_list(2000)
t1 = time.time()
quick_sort(lyst, 0, len(lyst) - 1)
t2 = time.time()
time_taken = t2 - t1
print(time_taken)
