with open("problem_11_input.txt") as f:
    content = f.readlines()
grid = []
for i in range(len(content)): 
    s = content[i]
    gr = s.split(" ")
    next_item = []
    for j in range(20):
        next_item.append(int(gr[j]))
    grid.append(next_item)
    
max_prod = grid[0][0]*grid[0][1]*grid[0][2]*grid[0][3]
max_i = 0
max_j = 0
mod = "right"

# right diag down
for i in range(17):
    for j in range(17):
        k = grid[i][j]*grid[i+1][j+1]*grid[i+2][j+2]*grid[i+3][j+3]
        if (max_prod < k):
            max_prod = k
            max_i = i 
            max_j = j
            mod = "right diag"
            
            
print(max_prod, ", ", max_i, ", ", max_j, ", ", mod)


# right
for i in range(20):
    for j in range(17):
        k = grid[i][j]*grid[i][j+1]*grid[i][j+2]*grid[i][j+3]
        if (max_prod < k):
            max_prod = k
            max_i = i 
            max_j = j
            mod = "right"

print("Current best: ", max_prod, ", ", max_i, ", ", max_j, ", ", mod)
        
# down
for i in range(17):
    for j in range(20):
        k = grid[i][j]*grid[i+1][j]*grid[i+2][j]*grid[i+3][j]
        if (max_prod < k):
            max_prod = k
            max_i = i 
            max_j = j
            mod = "down"

print("Current best: ", max_prod, ", ", max_i, ", ", max_j, ", ", mod)
            
# left diag down
for i in range(17):
    for j in range(17):
        k = grid[19-i][j]*grid[19-i-1][j+1]*grid[19-i-2][j+2]*grid[19-i-3][j+3]
        if (max_prod < k):
            max_prod = k
            max_i = i 
            max_j = j
            mod = "left diag"

print("Current best: ", max_prod, ", ", max_i, ", ", max_j, ", ", mod)

