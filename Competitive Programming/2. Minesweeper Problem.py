#Take input from the user for the number of rows and columns in the ground matrix
n_rows = int(input("Enter the number of rows: "))
n_cols = int(input("Enter the number of columns: "))

#Take input from the user for the elements of the ground matrix row by row
print("Enter the elements of the ground matrix:")
ground = []
for i in range(n_rows):
    row = input().split()
    ground.append(row)

#Function to check if there is a mine at location (n, m) in the ground matrix 
def ifMine(n, m):
    if ground[n][m] == "*": 
        return True

#Function to print the current state of the ground matrix   
def printGround(): 
    for i in range(n_rows):
        for j in range(n_cols): 
            print(ground[i][j], end=" ")
        print() 
    print() 
    print()

#Print the initial state of the ground matrix
printGround() 

#For each location in the ground matrix with '0' value, replace it with 0 (integer type)
for i in range(n_rows):
    for j in range(n_cols):
        if ground[i][j] == '0': 
            ground[i][j] = 0
    
#For each location in the ground matrix, check if there is a mine using the 'ifMine(n, m)' function
for i in range(n_rows):
    for j in range(n_cols): 
        if ifMine(i, j):
            if i-1 >=0 and j-1>=0:
                if ground[i-1][j-1] is not ifMine(i-1,j-1): 
                    ground[i-1][j-1] = str(int(ground[i-1][j-1])+1)
            if i-1 >=0 and j>=0:
                if ground[i-1][j] is not ifMine(i-1,j): 
                    ground[i-1][j] = str(int(ground[i-1][j])+1)
            if i-1 >= 0 and j+1<n_cols:
                if ground[i-1][j+1] is not ifMine(i-1,j+1): 
                    ground[i-1][j+1] = str(int(ground[i-1][j+1])+1)
            if j-1 >= 0:
                if ground[i][j-1] is not ifMine(i,j-i): 
                    ground[i][j-1] = str(int(ground[i][j-1])+1)
            if j+1<n_cols:
                if ground[i][j+1] is not ifMine(i,j+1): 
                    ground[i][j+1] = str(int(ground[i][j+1])+1)
            if i+1 < n_rows and j-1 >=0:
                if ground[i+1][j-1] is not ifMine(i+1,j-1): 
                    ground[i+1][j-1] = str(int(ground[i+1][j-1])+1)
            if i+1 < n_rows:
                if ground[i+1][j] is not ifMine(i+1,j): 
                    ground[i+1][j] = str(int(ground[i+1][j])+1)
            if i+1 < n_rows and j+1 < n_cols:
                if ground[i+1][j+1] is not ifMine(i+1,j+1): 
                    ground[i+1][j+1] = str(int(ground[i+1][j+1])+1)
printGround()