from itertools import combinations
from itertools import permutations
import numpy as np

def check_equal(set_of_seven, number): 
# checks the equality of all the subsets of set_of_seven with "number" elements  

    check_failed = False
    
    for set1 in combinations(set_of_seven, number):
        rest = set_of_seven - set(set1)
        for set2 in combinations(rest, number): 
            if (sum(set1) == sum(set2)): 
                check_failed = True
                break
    
    return check_failed

def check_greater(set_of_seven, num1, num2): 
# checks whether the sum of subsets with num2 elements is greates than the sum of subsets with num1 elements (num1 < num2)   

    check_failed = False
    for set1 in combinations(set_of_seven, num1):
        rest = set_of_seven - set(set1)
        for set2 in combinations(rest, num2): 
            if (sum(set1) >= sum(set2)): 
                check_failed = True
                break        
    
    return check_failed

candidates = []

for i in range(10,78): 
    candidates.append(i)

# found the set restricting the search within 20 and 50

min_set = set([20, 31, 38, 39, 40, 42, 45])
min_sum = 255

# a set with minimum sum will contain (a-1, a, a+1)

for i in range(10,78):
    candidates.remove(i)
    candidates.remove(i+1)
    candidates.remove(i+2)
    for candidate_list in combinations(candidates,4):
        set_of_seven = []
        set_of_seven.append(i)
        set_of_seven.append(i+1)
        set_of_seven.append(i+2)
        set_of_seven.append(candidate_list[0])    
        set_of_seven.append(candidate_list[1])    
        set_of_seven.append(candidate_list[2])    
        set_of_seven.append(candidate_list[3])    
        set_of_seven = set(set_of_seven)
        check_failed = False
        sorted_set = sorted(set_of_seven)
        if (sum(sorted_set) < min_sum):
            # since the elements have to satisfy the second rule, if there are two sets with two and one elements violating that rule, the following two and one element subset will also violate that rule 
            check_failed = (sorted_set[0] + sorted_set[1] <= sorted_set[6])      
            if (check_failed == False): 
                check_failed = (sorted_set[0]+sorted_set[1]+sorted_set[2] <= sorted_set[5]+sorted_set[6])
                if (check_failed == False):
                    check_failed = (sorted_set[0]+sorted_set[1]+sorted_set[2]+sorted_set[3] <= sorted_set[4]+sorted_set[5]+sorted_set[6])
                    if (check_failed == False):
                        check_failed = check_equal(set_of_seven,2)
                        if (check_failed == False): 
                            check_failed = check_equal(set_of_seven,3)
                            if (check_failed == False): 
                                print("Solution set is found: ", set_of_seven)
                                current_sum = sum(set_of_seven) 
                                if ( current_sum < min_sum): 
                                    min_set = set_of_seven
                                    min_sum = current_sum
    candidates.append(i)
    candidates.append(i+1)
    candidates.append(i+2)


print(min_sum)
print(min_set)