"""Sequential Search.
   Best Case: O(1)
   Worst Case: O(N)
   Average Case: O(N)"""


lyst = [4, 2, 8, 4, 7, 1, 5]
lyst.sort()

def seq_search(num, lyst):
    """Assumes lyst is sorted."""
    for element in lyst:
        if element == num:
            return True
        elif element > num:
            return False

print(seq_search(3, lyst))
