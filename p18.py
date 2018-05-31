sum_of_digits_to_4 = 0
sum_of_numbers = 0

for n in range(0,32806):
    sum_of_digits_to_4 = 0
    for j in range(len(str(n))):
        sum_of_digits_to_4 += math.pow(int(str(n)[j]),4)
    if (n == sum_of_digits_to_4):
        sum_of_numbers += n 
        print("n = ", n)
print("sum_of_numbers = ", sum_of_numbers)        
  
sum_of_digits_to_5 = 0
sum_of_numbers = 0

# there are no 2 or 3 digit numbers that would satisfy the equation: n = sum(digit_of_n^^5)
# there are no such 4 digit number bigger than 5555
# there are no such number with more than 6 digits

#four-digit numbers
for n in range(1000,5556):
    sum_of_digits_to_5 = 0
    for j in range(4):
        sum_of_digits_to_5 += math.pow(int(str(n)[j]),5)
    if (n == sum_of_digits_to_5):
        sum_of_numbers += n 
        print("n = ", n)

#five-digit numbers
for n in range(10000,100000):
    sum_of_digits_to_5 = 0
    for j in range(5):
        sum_of_digits_to_5 += math.pow(int(str(n)[j]),5)
    if (n == sum_of_digits_to_5):
        sum_of_numbers += n 
        print("n = ", n)

#six-digit numbers
for n in range(100000,1000000):
    sum_of_digits_to_5 = 0
    for j in range(6):
        sum_of_digits_to_5 += math.pow(int(str(n)[j]),5)
    if (n == sum_of_digits_to_5):
        sum_of_numbers += n 
        print("n = ", n)

print("sum_of_numbers = ", sum_of_numbers) 