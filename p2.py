a1 = 1
a2 = 2
current = 3
sum = 2

while current < 4000000:
    print("The next Fibonacci number is: ", current)
    if current%2 == 0:
      print("The next even Fibonacci number is: ", current)
      sum = sum + current
      print("Current sum is: ", sum)
    a1 = a2
    a2 = current
    current = a1 + a2
print("The sum is: ", sum)
