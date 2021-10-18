"""
Pattern

*     *
*   *
* *
* *
*   *
*     *

n = 6


"""
# for this figure n should be even and minimum value should be 6

print("Enter the number of rows")
n=int(input())



if n%2==0:
    print("Here is the Pattern")

    # Upper Portion
    for i in range(1,int(n/2+1)):
        print("*",end=" ")
        for j in range(1,int(n/2+1)):
            if i+j== int(n/2+1):
                # to make right diagonal i+j==n/2+1
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print("\n")
    
    # Lower Portion
    for i in range(1,int(n/2+1)):
        print("*",end=" ")
        for j in range(1,int(n/2+1)):
            if j == i:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print("\n")

else:
    print("Pattern Not possible")

    



