"""
Pattern

* * * * *
*       *
* * * * *
* 
*

n = 5

"""

# here n should be n odd value with minimum of 5

print("Enter the number of rows")
n= int(input())

if n%2 != 0:
    print("Here is the pattern")
    for i in range(1,n+1):
        for j in range(1,n+1):
            if j==1 or i==1 or i== int(n/2+1):
                print("*",end=" ")
            elif j ==n and i<= n/2:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print("\n")

else:
    print("Pattern Not Possible")