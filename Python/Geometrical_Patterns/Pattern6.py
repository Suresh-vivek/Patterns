"""
Pattern is:
* * * *
  * * *
    * *
      *

      n = 4

"""
# minimum value of n = 2

print("Enter the numbe of rows")
n = int(input())

# Here we using matrice method in which i represent rows and j represent columns
if n >= 2:
    for i in range(1, n+1):
        for j in range(1,n+1):
            if i == 1 or j == n or i == j or j > i:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print("\n")

else:
    print("Pattern Not possible")