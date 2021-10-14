"""
Patetrn

* * * * *
*       *
*       *
*       *
* * * * *

n = 5

"""

# for this pattern minimum vaue of n should be 3

print("Enter the number of rows")
n=int(input())

print("Here is the pattern")


# here i represnt rows, j represent columns
if n>=3:
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i==1 or i==n or j==1 or j==n:
                print("*",end=" ")
            else:
                print(" ",end=" ")
             
        print("\n")

else:
    print("pattern Not possible")
            

                
             
            
            
    