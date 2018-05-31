max_length = 1
max_start = 1

i = 9
j = i 

def chain_length(start): 
    current_length = 1
    j = start
    while (1 < j):
        if (j%2 == 0):
            j =j/2
            current_length += 1
        else: 
            j = 3*j +1
            current_length += 1
    return current_length

print(chain_length(871))
        
for i in range (2,1000000):
    l = chain_length(i)
    if (max_length < l): 
        print("better found")
        max_length = l
        max_start = i
print("Max length = ", max_length)
print("Start = ", max_start)