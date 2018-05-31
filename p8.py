#primes[i] = i if i is a prime number and 0 otherwise
primes = [2, 3, 5, 7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,
73,79,83,89,97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149,
151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229,
233, 239, 241, 251, 257, 263, 269, 271, 277, 281,
283, 293, 307, 311, 313, 317, 331, 337, 347, 349,
353, 359, 367, 373, 379, 383, 389, 397, 401,
409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,
503,509,521,523,541,547,557,563,569,571,577,587,593,599,
601,607,613,617,619,631,641,643,647,653,659,661,673,677,683,691,
701,709,719,727,733,739,743,751,757,761,769,773,787,797,
809,811,821,823,827,829,839,853,857,859,863,877,881,883,887,
907,911,919,929,937,941,947,953,967,971,977,983,991,997,
1009,1013,1019,1021,1031,1033,1039,1049,1051,1061,1063,1069,1087,1091,1093,
1097,
1103,1109,1117,1123,1129,1151,1153,1163,1171,1181,1187,1193,
1201,1213,1217,1223,1229,1231,1237,1249,1259,1277,1279,1283,1289,1291,1297
]

m=len(primes)
print "Number of primes used: %d" % m
n=7500000

#taking into account at max
#factorization_of_numbers[i][j] = the exponential of factor j in i
factorization_of_numbers = [[0 for x in range(m)] for y in range(n)]

for k in range(n):
    for l in range(m):
        factorization_of_numbers[k][l]=0

for k in range(len(primes)):
    l = 1
    while l < n:
        l = primes[k] * l
        i = l
        # find the multiples of l and increase the exponential of the prime by 1
        while i < n:
            factorization_of_numbers[i][k] = factorization_of_numbers[i][k] + 1
            i = i + l

print "Factorization is done"
number_of_divisors = 1
number_of_divisors2 = 1
tr = 0
tr2 = 0

k = 0
while k < round(n/2):
    print "test %d" % (2*k+1)
    tr = 2*k + 1
    tr2 = 2*k -1
    for l in range(m):
        number_of_divisors = number_of_divisors * (factorization_of_numbers[tr][l] + 1)
        number_of_divisors2 = number_of_divisors2 * (factorization_of_numbers[tr2][l] + 1)
    if 500 < number_of_divisors:
        k = round(n/2)
        print "Triangular number with more than 500 divisors found: %d" % tr
        print "Divisors of %d" % tr
        for j in range(m):
            if 0<factorization_of_numbers[tr][j]:
                print "Exponential of %d in %d: %d" % (primes[j],tr,factorization_of_numbers[tr][j])
    else:
        if 500 < number_of_divisors2:
            k = round(n/2)
            print "Triangular number (-1) with more than 500 divisors found: %d" % tr
            print "Divisors of %d" % tr2
            for j in range(m):
                if 0<factorization_of_numbers[tr2][j]:
                    print "Exponential of %d in %d: %d" % (primes[j],tr2,factorization_of_numbers[tr2][j])
        else:
            k = k+1
            number_of_divisors = 1
            number_of_divisors2 = 1

