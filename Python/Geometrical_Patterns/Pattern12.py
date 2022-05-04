"""
Pattern is:

*  *  *  *  *
 *        *
  *     *
   *  *
    *

n = 5
"""

print("Enter the number of Rows")
n = int(input())

if n >= 2:
    print("Here is the Pattern")
    for i in range(1,n+1):
        s = 1
        while s < i:
            print(" ",end=" ")
            s+=1

        for j in range(1,n+2 - i):
            if i == 1 or j == n or i == j:
                print("* ",end="  ")
            else:
                print("  ",end="  ")
        print("\n")
else:
    print("Pattern Not Possible")
    