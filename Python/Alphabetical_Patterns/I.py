"""
Pattern

   * * * * *
       *
       *
       *
   * * * * *    
           
           

   n = 5

"""

# for a perfect figure value of n should be odd & greater than 3

print("enter the number of rows")
n=int(input())



if n%2 != 0:
    if n>=3:
        for i in range(1,n+1):
            for j in range(1,n+1):
                if i==1 or i==n or j==int(n/2 +1):
                    # int() is used to convert float values to nearest integer value
                    print("*", end=" ")
                else:
                    print(" ",end=" ")
            print("\n")

else:
    print("Pattern Not Possible")