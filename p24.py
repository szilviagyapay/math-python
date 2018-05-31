n = 1000000

sum_of_divisors = []
visited = []

for i in range(0,n):
    sum_of_divisors.append(1)
    visited.append(0)

sum_of_divisors[0] = 0
sum_of_divisors[1] = 0

for i in range(2,int(n/2)):
  j = 2*i
  while j < n:
    sum_of_divisors[j] += i
    j += i

current_length = 1
current_min = 2
current_start = 2
best_length = 1
best_min = 2
best_start = 2

visited = []

for i in range(2,n):
    visited = []
    k = i #2
    current_length = 1
    current_min = k
    current_start = i # 2
    while not k in visited:
        visited.append(k)
        k = sum_of_divisors[k] #1
        if(k<n):
            current_length += 1 # 2
            if k < current_min:
                current_min = k     # 1
        else:
            current_length = 1
            current_min = i + 1
            current_start = i + 1
            break
    if (i==k):
        if best_length < current_length:
            print("Better found, end of circle, start, length, min: ",
            current_start, current_length, current_min)
            print("Circle: ", visited)
            best_length = current_length - 1
            best_start = current_start
            best_min = current_min

print(best_start)
print(best_length)
print("best_min = ",best_min)

print(" start: ", best_start)
print("sum = ", sum_of_divisors[best_start])
best_start = sum_of_divisors[best_start]
print("sum = ", sum_of_divisors[best_start])
best_start = sum_of_divisors[best_start]
print("sum = ", sum_of_divisors[best_start])
best_start = sum_of_divisors[best_start]
print("sum = ", sum_of_divisors[best_start])
best_start = sum_of_divisors[best_start]
print("sum = ", sum_of_divisors[best_start])
best_start = sum_of_divisors[best_start]
print("sum = ", sum_of_divisors[best_start])
best_start = sum_of_divisors[best_start]
print("sum = ", sum_of_divisors[best_start])
best_start = sum_of_divisors[best_start]
print("sum = ", sum_of_divisors[best_start])
best_start = sum_of_divisors[best_start]
print("sum = ", sum_of_divisors[best_start])
best_start = sum_of_divisors[best_start]
print("sum = ", sum_of_divisors[best_start])
best_start = sum_of_divisors[best_start]
print("sum = ", sum_of_divisors[best_start])
best_start = sum_of_divisors[best_start]
print("sum = ", sum_of_divisors[best_start])
best_start = sum_of_divisors[best_start]
print("sum = ", sum_of_divisors[best_start])
best_start = sum_of_divisors[best_start]
print("sum = ", sum_of_divisors[best_start])
best_start = sum_of_divisors[best_start]
print("sum = ", sum_of_divisors[best_start])
best_start = sum_of_divisors[best_start]
print("sum = ", sum_of_divisors[best_start])
best_start = sum_of_divisors[best_start]
print("sum = ", sum_of_divisors[best_start])
best_start = sum_of_divisors[best_start]
print("sum = ", sum_of_divisors[best_start])
best_start = sum_of_divisors[best_start]
print("sum = ", sum_of_divisors[best_start])
best_start = sum_of_divisors[best_start]
print("sum = ", sum_of_divisors[best_start])
best_start = sum_of_divisors[best_start]
print("sum = ", sum_of_divisors[best_start])
best_start = sum_of_divisors[best_start]
print("sum = ", sum_of_divisors[best_start])
best_start = sum_of_divisors[best_start]
print("sum = ", sum_of_divisors[best_start])
best_start = sum_of_divisors[best_start]
print("sum = ", sum_of_divisors[best_start])
best_start = sum_of_divisors[best_start]
print("sum = ", sum_of_divisors[best_start])
best_start = sum_of_divisors[best_start]
print("sum = ", sum_of_divisors[best_start])
best_start = sum_of_divisors[best_start]
print("sum = ", sum_of_divisors[best_start])
best_start = sum_of_divisors[best_start]
print("sum = ", sum_of_divisors[best_start])
best_start = sum_of_divisors[best_start]
