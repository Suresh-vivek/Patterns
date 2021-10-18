"""
Pattern

* * * * *
*   *   *
*   *   *
*       *
*       *

n = 5

"""
# Here n should be ann odd value with minimum of 5

print("Enter the number of rows")
n= int(input())

if n%2 !=0:
    print("Here is the pattern")
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i == 1:
                print("*",end=" ")
            elif j == 1 or j == n:
                print("*",end=" ")
            elif j == int(n/2 +1) and i <= int(n/2+ 1):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        
        print("\n")

else:
    print("Pattern Not Possible")
