"""
Pattern
   * * * * * *
   *         *
   *         *
   *     *   * 
   *       * *
   * * * * * *
   n = 6

"""

# Here minimum value of n should be 6 and even

print("enter the number of rows")
n=int(input())



if n%2==0:
    print("here is the Pattern")
    for i in range(1,n+1):
        for j in range(1,n+1):
            if j==1 or j==n or i==1 or i==n:
                
                print("*",end=" ")
            elif i == j and i> n/2:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        
        print("\n")

else:
    print("Pattern NOT possible")
    
        