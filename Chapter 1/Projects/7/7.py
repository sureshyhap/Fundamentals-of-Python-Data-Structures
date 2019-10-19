"""Mean, Median, Mode"""

def main():
    ls = [5, 1, 6, 3, 4, 8, 1, 3, 9, 2, 1, 0]
    print(mean(ls))
    print(median(ls))
    print(mode(ls))
    

def mean(ls):
    return (sum(ls) / len(ls))

def median(ls):
    mid = len(ls) // 2
    if len(ls) % 2 == 0:
        return (ls[mid - 1] + ls[mid]) / 2
    else:
        return ls[mid]

def mode(ls):
    freqs = {}
    for element in ls:
        if element not in freqs.keys():
            freqs[element] = 1
        else:
            freqs[element] += 1
    max_occurence = 0
    max_num = None
    for element, count in freqs.items():
        if count > max_occurence:
            max_occurence = count
            max_num = element
    return max_num
        
    
if __name__ == "__main__":
    main()


