"""
Pattern is:

* * * * *
        *
        *
        *
        *

n = 5
"""

print("enter the number of rows")
n=int(input())

if n >= 3:
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i == 1 or j == n:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        
        print("\n")
    
else:
    print("Pattern Not Possible")