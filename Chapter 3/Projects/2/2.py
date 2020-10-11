"""Reverses a list.
   O(N)"""


lyst = [6, 1, 8, 7, 4, 3, 4, 7, 6, 1, 1, 4, 1]

def reverse(lyst):
    copy = lyst[:]
    length = len(lyst)
    for i in range(length):
        copy[i] = lyst[length - 1 - i]
    print(copy)
    print(lyst)

reverse(lyst)
