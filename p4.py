sum = 0
sqrts_sum = 0
n = 100

for k in range(1,n+1):
  sum = sum + k
  sqrts_sum = sqrts_sum + k * k
print("Sqrts_sum - sqrt(sum) for n =", n, " : d", sum*sum-sqrts_sum)
