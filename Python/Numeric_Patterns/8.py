"""
Pattern is:

* * * * *
*       *
* * * * *
*       *
* * * * *

n = 5
"""

# Minimum value of n = 5 and it should be an odd

print("enter the number of rows")
n=int(input())

if n%2 != 0:
    if n >= 5:
        print("Here is the Pattern")
        for i in range(1,n+1):
            for j in range(1, n+1):
                if i == 1 or i == n or i == int(n/2 + 1) or j == 1 or j == n:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            
            print("\n")
    else:
        print("Pattern Not Possible")

else:
        print("Pattern Not Possible")
