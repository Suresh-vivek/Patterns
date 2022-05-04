"""
Pattern is :

        * * * *
      *     *
    *     *
  * * * *

  n = 4
""" 
print("Enter the number of Rows")
n = int(input())

if n >=3:
    for i in range(1,n+1):
        s = 0 # s represent spaces
        while s < n - i:
            print(" ",end=" ")
            s+=1
        for j in range(1,n+1):
            if i == 1 or j == 1 or i ==n or j == n:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print("\n")
else:
    print("pattern not possible")