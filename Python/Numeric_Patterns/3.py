"""
Pattern

   * * * * *
           *       
   * * * * *
           *
   * * * * *       

   n = 5

"""

# Here minimum value of n should be 5

print("enter the number of rows")
n=int(input())

if n%2 != 0:
    if n>=5:
        print("here is the Pattern")
        for i in range(1,n+1):
            for j in range(1,n+1):
                if i==1 or i==int(n/2 +1) or j==n or i==n:
                # int() is used to convert float values to nearest integer value
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
        
            print("\n")

    else:
        print("Pattern NOT possible")
else:
        print("Pattern NOT possible")

    

    

