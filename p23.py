from itertools import combinations
from itertools import permutations
import numpy as np

np.seterr(divide='ignore')

def firstNotExpressableNumber(numbers): 

    generated = []
    result = 0
    s = '+-*/'

    for letters in product(s, repeat = 3):
        for perm in permutations(numbers,4): 
            # (a b c) d
            result = eval(perm[0]+letters[0]+perm[1]+letters[1]+perm[2]+letters[2]+perm[3])
            if (0 < result): 
                if (0 == result - math.ceil(result)): 
                    if (not(result in generated)): 
                        generated.append(result)
            # a (b c d)
            if (not(letters[0] == "/" and eval(perm[1]+letters[1]+perm[2]+letters[2]+perm[3]) == 0)):
                result = eval(perm[0]+letters[0]+"("+perm[1]+letters[1]+perm[2]+letters[2]+perm[3]+")")
                if (0 < result): 
                    if (0 == result - math.ceil(result)): 
                        if (not(result in generated)): 
                            generated.append(result)
            # (a b) (c d)
            if (not(letters[1] == "/" and eval(perm[2]+letters[2]+perm[3]) == 0)):
                result = eval("(" + perm[0]+letters[0]+perm[1]+ ")"+letters[1]+"("+perm[2]+letters[2]+perm[3]+")")
                if (0 < result): 
                    if (0 == result - math.ceil(result)): 
                        if (not(result in generated)): 
                            generated.append(result)
            # (a b) c d
            result = eval("(" + perm[0]+letters[0]+perm[1]+ ")"+letters[1]+perm[2]+letters[2]+perm[3])
            if (0 < result): 
                    if (0 == result - math.ceil(result)): 
                        if (not(result in generated)): 
                            generated.append(result)

            # a (b c) d
            if (not(letters[0] == "/" and eval(perm[1]+letters[1]+perm[2]) == 0)):
                result = eval(perm[0]+letters[0]+"(" + perm[1]+ letters[1]+perm[2]+")"+letters[2]+perm[3])
                if (0 < result): 
                    if (0 == result - math.ceil(result)): 
                        if (not(result in generated)): 
                            generated.append(result)

            # a b (c d)
            if (not(letters[1] == "/" and eval(perm[2]+letters[2]+perm[3]) == 0)):
                result = eval(perm[0]+letters[0]+perm[1]+ letters[1]+"("+perm[2]+letters[2]+perm[3]+")")
                if (0 < result): 
                    if (0 == result - math.ceil(result)): 
                        if (not(result in generated)): 
                            generated.append(result)
            # ((a b) c) d
            result = eval("(" + "(" + perm[0]+letters[0]+perm[1]+ ")"+letters[1]+perm[2]+")"+letters[2]+perm[3])
            if (0 < result): 
                    if (0 == result - math.ceil(result)): 
                        if (not(result in generated)): 
                            generated.append(result)

            # (a (b c)) d 
            if (not(letters[0] == "/" and eval(perm[1]+letters[1]+perm[2]) == 0)):
                result = eval("(" + perm[0]+letters[0]+"(" + perm[1]+ letters[1]+perm[2]+")"+")"+letters[2]+perm[3])
                if (0 < result): 
                    if (0 == result - math.ceil(result)): 
                        if (not(result in generated)): 
                            generated.append(result)
            # a ((b c) d)
            if (not(letters[0] == "/" and eval("("+perm[1]+letters[1]+perm[2]+")"+letters[2]+perm[3]) == 0)):
                result = eval(perm[0]+letters[0]+"("+"("+perm[1]+letters[1]+perm[2]+")"+letters[2]+perm[3]+")")
                if (0 < result): 
                    if (0 == result - math.ceil(result)): 
                        if (not(result in generated)): 
                            generated.append(result)

            # a (b (c d))
            if (not(letters[0] == "/" and eval(perm[1]+letters[1]+"("+perm[2]+letters[2]+perm[3]+")") == 0) and
               not(letters[1] == "/" and eval(perm[2]+letters[2]+perm[3]))):
                result = eval(perm[0]+letters[0]+"("+perm[1]+letters[1]+"("+perm[2]+letters[2]+perm[3]+")"+")")
                if (0 < result): 
                    if (0 == result - math.ceil(result)): 
                        if (not(result in generated)): 
                            generated.append(result)

    sorted_generated = sorted(generated)

    # find the first missing integer
    for i in range(len(sorted_generated)):
            if (i + 1 < sorted_generated[i]):
                   break
       
    return i+1

max_expressable = 0
max_numbers = ""
candidate = 0

for numbers in combinations("123456789", 4):
    candidate = firstNotExpressableNumber(numbers)-1
    if (max_expressable < candidate): 
        max_expressable = candidate
        max_numbers = numbers
        print("Better found, numbers = ", numbers, ", max_number = ", candidate-1)

# numbers = str(a) + str(b) + str(c) + str(d)

print("The max first integer that cannot be expressed by ", max_numbers, " is ", max_expressable - 1)

