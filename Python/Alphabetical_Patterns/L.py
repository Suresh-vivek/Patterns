"""
Pattern

*     
*   
* 
* 
*   
* * * * * *

n = 6


"""

# Here minimum value of n should be 3

print("Enter the number of rows")
n= int(input())

if n>=3:
    print("Here is the pattern")
    
    for i in range(1,n+1):
        for j in range(1,n+1):
            if j==1 or i==n:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print("\n")

else:
    print("pattern Not Possible")