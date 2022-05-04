"""
Pattern

*
*  *
*  *  *
*  *  *  * 
*  *  *  *  *
*  *  *  * 
*  *  *
*  * 
*

n = 5
"""

print("Enter the number of rows")
n = int(input())

print("Here is the Pattern")

for i in range(1,n+1):
    for j in range(1,i+ 1):
        print("* ",end="  ")
    print("\n")

i = n-1
while i >= 1:
    for j in range(1,i+1):
        print("* ",end="  ")
    print("\n")
    i-=1
    