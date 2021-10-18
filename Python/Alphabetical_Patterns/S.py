"""
Pattern

* * * * *
* 
* * * * *
        *
* * * * *

n = 5
"""

# Minimum value of n = 5 and n sholud be odd

print("Enter the number of rows")
n = int(input())

if n%2 != 0:
    print("Here is the pattern")
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i == 1 or i == n or i == int(n/2 +1):
                print("*",end=" ")
            elif j == 1 and i <= int(n/2):
                print("*",end=" ")
            elif j == n and i > int(n/2):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print("\n")

else:
    print("Pattern Not Possible")
            