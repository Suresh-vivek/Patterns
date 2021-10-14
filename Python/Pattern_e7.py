"""
Patetrn

* 
* *
*   *
*     *
* * * * *

n = 5

"""

# for this pattern minimum vaue of n should be 2

print("Enter the number of rows")
n=int(input())

print("Here is the pattern")



# here i represnt rows, j represent columns
if n>=2:
    for i in range(1,n+1):
        for j in range(1,n+1):
            if j==1 or i==n or i==j:
                print("*",end=" ")
            else:
                print(" ",end=" ")
             
        print("\n")

else:
    print("pattern Not possible")
            

                
             
            
            
    