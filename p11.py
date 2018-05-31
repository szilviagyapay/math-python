month = [31,28,31,30,31,30,31,31,30,31,30,31]
#Tuesday = k==2, 1901.01.01 = Tuesday
k = 2
count = 0
for i in range(1, 101):
    for j in range(1,13):
        print(1900+i, ".", j, ".01. is : ", k)
        if k == 0:
            count += 1
        if j!=2:
            k = (k + month[j-1])%7
        elif i%4 == 0:
            k = (k + month[j-1] + 1)%7
print("Count: ",count)
