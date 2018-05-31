#primes[i] = i if i is a prime number and 0 otherwise
primes = []
sum_of_primes = 0
number_of_primes = 0
n=2000000


#set primes[i] = i
for i in range(n+2):
  primes.append(i);

#put 0 to all even number
primes[0] = 0
primes[1] = 0
i=2
for k in range(2,int(n/2)+1):
    primes[2*k]=0
sum_of_primes = 2
number_of_primes = 1
i=3
while i < n+1:
    if primes[i] != 0:
        # i is a prime
#        print "A prime number is found: %d" % primes[i]
        sum_of_primes = sum_of_primes + i
        number_of_primes = number_of_primes + 1
        j = i + i

        #find all multiple of i and set the prime flag to 0
        while j <= n:
            primes[j]=0
            j = j+i
    i = i + 2

print("Sum of the primes below ", n, ": ", sum_of_primes)
