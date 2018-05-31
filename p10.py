import numpy as np

m = 3

r = [[0 for x in range(m+1)] for y in range(m+1)]

i=0
for k in range(m+1):
    r[i][k] = 1

j=0
for k in range(m+1):
    r[k][j] = 1

for k in range(m+1):
    for l in range(m+1):
        if (0<k) and (0<l):
            r[k][l]=r[k-1][l]+r[k][l-1]

#print "Number of routes = %d" % r[m][m]

x = np.array([[1,2],[3,4],[5,6]])
y = np.array([[1,2],[3,4],[5,6]])
z = x * y

print (x.T)
print (y)
print (z)

new_x = new_x.reshape((1, -1))

print(x)
