"""
Pattern

                      *
                   *  *
                *  *  *
             *  *  *  *
                *  *  *
                   *  *
                      *

                      n = 4

"""

print("Enter the number of rows")
n = int(input())

print("Here is the Pattern")

# Upper Portion
for i in range(1,n+1):
    s = 0
    while s < n - i:
        print("  ",end="  ")
        s+=1
    for j in range(1,i+1):
        print("* ",end="  ")
    print("\n")

# lower portion
for i in range(1,n):
    s = 1
    while s <= i:
        print("  ",end="  ")
        s+=1
    
    for j in range(1,n-i +1):
        print("* ",end="  ")
    print("\n")


