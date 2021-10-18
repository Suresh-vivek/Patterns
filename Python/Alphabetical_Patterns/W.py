"""
Pattern
   *       *
   *       *
   *       *
   *   *   *
   *   *   *
   * * * * *
   n = 5

"""

# minimum value n = 3 and it should be odd

print("enter the number of rows")
n=int(input())


if n%2 != 0:
    if n >=3:
        print("Here is the Pattern")
        for i in range(1,n+1):
            for j in range(1,n+1):
                if j == 1 or j == n or i == n:
                    print("*",end=" ")
                elif j == int(n/2 + 1) and i > int(n/2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            
            print("\n")
    
    else:
        print("Pattern Not Possible")

else:
        print("Pattern Not Possible")