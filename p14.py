from itertools import combinations
from itertools import permutations
import numpy as np

def check_equal(set_to_test): 

    check_failed = False
    len_set = len(set_to_test)
    if (len_set%2 == 0): 
        limit = int(len_set/2)
    else: 
        limit = int(math.floor(len_set/2))
    for j in range(2,limit+1): 
        for set1 in combinations(set_to_test, j):
            rest = set(set_to_test) - set(set1)
            for set2 in combinations(rest, j): 
                if (sum(set1) == sum(set2)): 
                    check_failed = True
                    break
    
    return check_failed

def check_greater(set_to_test): 

    check_failed = False
    len_set = len(set_to_test)
    if (len_set%2 == 0): 
        limit = int(len_set/2) - 1
    else: 
        limit = int(math.floor(len_set/2))
    for j in range(2,limit+1):
        num1 = j
        num2 = j+1
        for set1 in combinations(set_to_test, num1):
            rest = set(set_to_test) - set(set1)
            for set2 in combinations(rest, num2): 
                if (sum(set1) >= sum(set2)): 
                    check_failed = True
                    break        
    
    return check_failed

with open("p105_sets.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content] 

n = len(content)
res = 0

for i in range(n): 
    next_element = content[i].split(",")
    candidates = [int(x) for x in next_element]
    sorted_set = sorted(candidates)
    check_failed = False
    check_failed = check_equal(sorted_set)
    if (check_failed == False): 
        check_failed = (check_greater(sorted_set))
        if (check_failed == False):
            res += sum(sorted_set)
                    
print(res)

# test with two good and two bad sets

with open("test_sets.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content] 

n = len(content)
res = 0

for i in range(n): 
    next_element = content[i].split(",")
    candidates = [int(x) for x in next_element]
    sorted_set = sorted(candidates)
    check_failed = False
    check_failed = check_equal(sorted_set)
    if (check_failed == False): 
        check_failed = (check_greater(sorted_set))
        if (check_failed == False):
            print(sorted_set)
            print(res)
            res += sum(sorted_set)
                    
print(res)