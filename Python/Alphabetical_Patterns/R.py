"""
Pattern

* * * *   
*     *         
*     *      
* * * * 
*
* *
*   *

n = 7
"""

# for this pattern value of n sholud be odd with minimum of 5

print("Enter the number of rows")
n = int(input())


if n%2 != 0:
    # Upper portion
    for i in range(1,int(n/2 + 2)):
        for j in range(1, int(n/2 + 2)):
            if i == 1 or j == 1 or i == int(n/2 + 1) or j == int(n/2 + 1):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print("\n")

    # Lower Portion
    for i in range(1,int(n/2 + 1)):
        for j in range(1, int(n/2 + 1)):
            if j == 1 or i == j:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print("\n")

else:
    print("Pattern Not Possible")



