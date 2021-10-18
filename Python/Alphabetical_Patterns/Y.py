"""
*       *
  *   *
    *
    *
    *

n = 5
"""

# Minimum value of n = 3

print("Enter the number of Rows")
n = int(input())

if n >= 3:
    # for even values
    if n%2 == 0:
        for i in range(1,int(n/2+1)):
            for j in range(1,int(n/2+1)):

                if i == j:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            for j in range(1,int(n/2 + 1)):
                if j == int(n/2) - i:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print("\n")

        for i in range(1,int(n/2 + 1)):
            for j in range(1,int(n +1)):
                if j == int(n/2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print("\n")

    else:
        # for odd values
        for i in range(1, int(n/2 +2)):
            for j in range(1, int(n/2 + 2)):
                if i == j:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            for j in range(1, int(n/2 + 2)):
                if j == int(n/2 + 1) -i:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print("\n")

        for i in range(1,int(n/2 +1)):
            for j in range(1, int(n + 1)):
                if j == int(n/2+1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print("\n")
        

            

    
    
else:
    print("Pattern Not Possible")