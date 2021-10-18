"""
Pattern is:

* * * * *
      *
    *
  *
* * * * *
 n = 5

"""
# Minimum value of n = 3

print("Enter the number of Rows")
n = int(input())

if n >= 3:
    print("Here is the Pattern")
    for i in range(1,n+1):
        for j in range(1, n+1):
            if i == 1 or i == n or i+j == n+1:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print("\n")
    
else:
    print("Pattern Not Possible")