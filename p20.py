import math

def check_pn(n): 
    n2 = math.sqrt(24*n+1)
    if ((n2 - int(n2)) == 0):
        if ((int(n2)+1)%6 == 0):
            return True
        else: return False
    else: return False

def pn(n): 
    return int(n*(3*n-1)/2)

# analyze only the difference and the sum of two pentagonal numbers in the form P_n, P_(n+k)   
# setting n to 1..2000 and k to 1..2000, found n = 1020, k = 1147. 
# based no the difference, for each n a max_k can be calculated 
# max_n can be calculated from the found pair   

for n in range(1,1827554): 
    max_k = math.ceil(math.sqrt(n*n+3655107)-n)
    if (n==1020): 
        print(max_k)
    for k in range(1,max_k+1):
        if (check_pn(int((6*k*n+3*k*k-k)/2))) and (check_pn(int((6*n*n+6*k*n+3*k*k-k-2*n)/2))): 
            print("Found: ", n, " and ", n+k)


p1 = (1020/2)*(3*1020-1)
print(p1)
print(check_pn(p1))

p2 = 2167*(3*2167-1)/2
print(p2)
print(check_pn(p2))

print(p2-p1)
print(p2+p1)

print(check_pn(p2-p1))
print(check_pn(p2+p1))

print(math.sqrt(3655106))