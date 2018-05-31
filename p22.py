primes = []

n = 1000000
for i in range(0,n):
  primes.append(i);

primes[0] = 0
primes[1] = 0
primes_list = []

for i in range(2,int(n/2)+1):
    for k in range(2,int(n/i)+1):
        if k*i < n:
            primes[k*i]=0

for i in range(100001,n):
    if not primes[i] == 0:
        primes_list.append(i)

primes_placesOfDigits = []
potential_primes = []
char_vec = []
for r in range(0,len(primes_list)):
    i = str(primes_list[r])
    placeOfDigits = []
    numberOfDigits = [0,0,0,0,0,0,0,0,0,0]
    for j in range(0,6):
        numberOfDigits[int(i[j])] += 1
    for k in range(0,10):
        if numberOfDigits[k] >= 3:
                numberOfDigits[k] -= 3
                for j in range(0,6):
                    if int(i[j]) == k:
                        placeOfDigits.append(j)
                primes_placesOfDigits.append(placeOfDigits)
                potential_primes.append(primes_list[r])
                char_vec.append(numberOfDigits)

numberOf = 0

if not primes[121313] == 0:
    numberOf += 1
    print("prime!", 1)
if not primes[222323] == 0:
    numberOf += 1
    print("prime!",2)

#if not primes[92227] == 0:
#    numberOf += 1
if not primes[323333] == 0:
    numberOf += 1
    print("prime!",3)

if not primes[424343] == 0:
    numberOf += 1
    print("prime!",4)

if not primes[525353] == 0:
    numberOf += 1#
    print("prime!",5)

if not primes[626363] == 0:
    numberOf += 1
    print("prime!",6)

if not primes[727373] == 0:
    numberOf += 1
    print("prime!",7)

if not primes[828383] == 0:
    numberOf += 1
    print("prime!",8)

if not primes[929393] == 0:
    numberOf += 1
    print("prime!",9)

print("Number of = ", numberOf)

#print("potential_primes: ", potential_primes)

for r1 in range(0,len(potential_primes)):
    candidate = potential_primes[r1]
    if len(primes_placesOfDigits[r1]) == 3:
        count = 0
        permanent = 0
        prodsum = 0
        for k in range(0,6):
            if k in primes_placesOfDigits[r1]:
                prodsum += 10**(5-k)
            else:
                permanent += int(str(candidate)[k])*10**(5-k)
        for i in range(0,10):
            r2 = i*prodsum + permanent
            if r2 in potential_primes:
                count +=1
        if 7<count:
            print("Prime = ", candidate, " has more than 6 prime chain")
