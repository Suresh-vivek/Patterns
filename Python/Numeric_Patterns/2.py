"""
Pattern is 

* * * * * * *
            *
            *
* * * * * * *
*
*
* * * * * * *

n = 7
"""

# Minimum vakue of n = 5 and it should be odd

print("enter the number of rows")
n=int(input())

if n >= 5:
    if n%2 != 0:
        for i in range(1,n+1):
            for j in range(1,n+1):
                if i == 1 or i == int(n/2 + 1) or i == n:
                    # int() is used to convert float values to nearest integer value
                    print("*",end=" ")
                elif j == n and i <= int(n/2):
                    print("*",end=" ")
                elif j == 1 and i >= int(n/2 + 1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print("\n")
    
    else:
        print("Pattern not possible")

else:
        print("Pattern not possible")

        
