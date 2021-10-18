"""
Pattern

   * * * * *
       *
       *
       *
   * * *     
           
           

   n = 5

"""

# for a perfect figure value of n should be odd & greater than 5

print("enter the number of rows")
n=int(input())



if n%2 != 0:
    if n>=5:
        for i in range(1,n):
            for j in range(1,n+1):
                if i==1 or j==int(n/2 +1):
                    # int() is used to convert float values to nearest integer value

                    print("*", end=" ")

                else:
                    print(" ",end=" ")
        
            print("\n")
        
        for x in range(int(n/2 +1)):
            print("*",end=" ")
        print("\n")
        # This loop will print last line ,this loop will make figure accurate.
        

else:
    print("Pattern Not Possible")