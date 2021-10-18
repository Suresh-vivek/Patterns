"""
Pattern

   * * * * *
   *       
   * 
   *       
   * * * * *

   n = 5

"""

# Here minimum value of n should be 4

print("enter the number of rows")
n=int(input())


if n>=4:
    print("here is the Pattern")
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i==1 or j==1 or i==n:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        
        print("\n")

else:
    print("Pattern NOT possible")
    
        

