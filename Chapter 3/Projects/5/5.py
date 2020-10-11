lyst = [3, 6, 1, 7, 3, 9, 5, 8, 3, 3, 4]

def selection_sort(lyst, reverse = False):
    i = 0
    while i < len(lyst):
        index = i
        j = i + 1
        if reverse:
            while j < len(lyst):
                if lyst[j] > lyst[index]:
                    index = j
                j += 1
        else:
            while j < len(lyst):
                if lyst[j] < lyst[index]:
                    index = j
                j += 1
        if index != i:
            lyst[i], lyst[index] = lyst[index], lyst[i]
        i += 1
    return lyst

print(selection_sort(lyst))
print(selection_sort(lyst, reverse=True))
