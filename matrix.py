# Function to print the required pattern
def printPattern(n):
     
    # arr[][] will store the pattern matrix
    arr = [[0 for x in range(n)]
              for y in range(n)]
    p = 1
 
    # Store the values for upper
    # triangle of the pattern
    for k in range(n):
        x = k
        y = 0
        while (x >= 0):
            arr[x][y] = p
            p += 1
            x = x - 1
            y = y + 1
     
    # Store the values for lower triangle
    # of the pattern
    for k in range(1, n, 1):
        y = k
        x = n - 1
        f = k
        while (x >= f):
            arr[x][y] = p
            p += 1
            x = x - 1
            y = y + 1
     
    # Print the pattern
    for x in range(0, n, 1):
        for y in range(0, n, 1):
            print(arr[x][y], end = " ")
         
        print("\n", end = "")
 
# Driver code
if __name__ == '__main__':
    n = 4
 
    printPattern(n)





