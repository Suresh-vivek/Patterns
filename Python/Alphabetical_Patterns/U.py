"""
Pattern

   *       *
   *       *
   *       *
   *       *
   * * * * *
   n = 5

"""

# Here minimum value of n should be 3

print("enter the number of rows")
n=int(input())



if n>=3:
    print("here is the Pattern")
    for i in range(1,n+1):
        for j in range(1,n+1):
            if j==1 or j==n or  i==n:
                # int() is used to convert float values to nearest integer value
                print("*",end=" ")
            else:
                print(" ",end=" ")
        
        print("\n")

else:
    print("Pattern NOT possible")
    
        