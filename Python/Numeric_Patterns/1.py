
"""
Pattern is:

* * *
    *
    *
    *
* * * * *

n = 5
"""

# minimum value of n = 3 an it should be odd
print("Enter the number of Rows")
n = int(input())

if n%2 != 0:
    if n >=3:
        for i in range(1, n+1):
            for j in range(1 , n+1):
                if i ==1 and j <= int(n/2 + 1):
                    print("*",end=" ")
                elif j == int(n/2 + 1) or i == n:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print("\n")
    
    else:
        print("Pattern not Possible")

else:
        print("Pattern not Possible")

