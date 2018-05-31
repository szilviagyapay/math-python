import math

prime_candidate = 3 # divisor of n
n= 486874
current = prime_candidate

while prime_candidate < math.ceil(math.sqrt(n)):
    if n%prime_candidate == 0:
        if current < prime_candidate:
            current = prime_candidate
        n = n/prime_candidate
        print("cand: ", prime_candidate)
        prime_candidate = 3
    else:
        prime_candidate += 1

print("Prime: ", current)

