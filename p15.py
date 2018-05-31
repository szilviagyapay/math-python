from itertools import combinations
import numpy as np

# two sets do not have to be checked to be equal if we can make pairs of elements from thetwo sets 
# such that the index of the element from the second set is greater than the index of the element in the first set
# in order to check the indices of each pairs only once, I sort the elements in both sets and check sets only where the 
# first set minimum index is less than the minimum index in the second one
# the sets contains the indices

def check_indices(n, set1, set2): 
    
    check_ok = False
    min1 = min(set1)
    min2 = min(set2)
    if (min1 < min2): 
        for i in range(n):
            if (set2[i] <= set1[i]):
                check_ok = True
                break

    return check_ok

n = 12

set_to_test = []

for i in range(n):
    set_to_test.append(i+1)
    
print(set_to_test)

number_of_pairs = 0

for i in range(2,int(math.floor(n/2))+1): 
    # compute all the 2-element combinations 
    for set1 in combinations(set_to_test, i):
        rest = set(set_to_test) - set(set1)
        for set2 in combinations(rest, i):
            set1 = sorted(set1)
            set2 = sorted(set2)
            if check_indices(i, set1, set2):
                print(set1, " and " , set2)
                number_of_pairs += 1

print(number_of_pairs)