"""
Pattern is:

*       *
*       * 
* * * * *
        *
        *

n = 5
"""

# Here minimum value of n should be 5

print("enter the number of rows")
n=int(input())

if n%2 !=0:
    if n >= 5:
        # for upper portion
        for i in range(1,int(n/2 +2)):
            for j in range(1,n+1):
                # int() is used to convert float values to nearest integer value
                if j == 1 or j == n or i == int(n/2 + 1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print("\n")
        
        # for lower portion
        for i in range(1,int(n/2 +1)):
            for j in range(1,n+1):
                if j == n:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print("\n")
    
    else:
        print("Pattern Not Possible")

else:
        print("Pattern Not Possible")

