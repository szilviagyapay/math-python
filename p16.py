# due to the limits of the coefficients and the problem, the primes that are reached by the equation (in a row) likely are not going to be greater than 1000000. 
# compute the primes under n

n = 1000000 

primes = []

for i in range(n):
    primes.append(1)

primes[0] = 0
primes[1] = 0
number_of_primes = 0

i = 2

while (number_of_primes < 10001):
    if (primes[i] == 1):
        number_of_primes += 1
        for j in range(2*i,n,i):
            primes[j] = 0
    i += 1

# length of max sequence and the corresponding coefficients

max_length = 0
max_a = 0
max_b = 0

# loop for the coefficients
# supposing that a sequence with maximal length is longer than 80, I set k to 80*80+80*a+b and tested whether the equation with 
# the current coefficients gives a prime at n = 80
# with this settings I found a solution with the length of 70, where a = -59, b = 911. 
# based on this solution with setting k to 70*70+70*a+b I found a longer solution that appeared to be the longest one. 

for a in range(-999,1000):
    for b in range(-1000,1001):
        k = 70*70+70*a+b
        if (0 < k): 
            if (primes[k] == 1): 
                n = 0
                length = 0
                end = False
                while (end == False):
                    k = n*n+n*a+b
                    if (k <= 1):
                        end = True
                    else: 
                        if (primes[k] == 1):
                            length += 1
                        else: end = True
                    n = n + 1
                if (max_length < length):
                    max_length = length 
                    max_a = a
                    max_b = b
                    last_prime_at = n - 2
                    print("Better found: ", n-2, max_length, max_a, max_b)

for i in range(72):
    print(primes[i*i-61*i+971])
    
print(-61*971)