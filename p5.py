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

print(number_of_primes, ", ",i-1)
    
            