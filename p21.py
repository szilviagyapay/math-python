last_ten = 0
current = 0

for i in range(1,1001): 
    current = 1
    # calculate the last ten digits of (i*i)*i... cut back in each step to ten digits
    for j in range(1,i+1): 
        current *= i
        n_digits = len(str(current))
        if (10 < n_digits): 
            current = int(str(current)[n_digits-10:])
    last_ten += current
    n_digits = len(str(last_ten))
    if(10 < n_digits): 
        last_ten = int(str(last_ten)[n_digits-10:])
        
print(last_ten)