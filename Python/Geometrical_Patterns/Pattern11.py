"""
Pattern

               *
              *  * 
             *     *
            *  *  *  *

n = 4
"""
# minimum value of n = 2

print("Enter the number of rows")
n = int(input())

if n >=3:
    print("Here is the Pattern")
    for i in range(1,n+1):
        s = 0
        while s < n - i:
            print(" ",end=" ")
            s+=1
        for j in range(1,i+1):
            if j == 1 or i == j or i == n:
                print("* ",end="  ")
            
            else:
                print("  ",end="  ")
        print("\n")
else:
    print("Pattern Not Possible")