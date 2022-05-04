"""
Pattern

               *
             * *
           * * *
         * * * *

n = 4
"""
# minimum value of n = 2

print("Enter the number of rows")
n = int(input())

if n >= 2:
  for i in range(1,n+1):
    s= 0  # s represent spaces
    while s < n - i:
      print(" ",end=" ")
      s+=1

    for j in range(1,i+1):
      print("*",end=" ")
    
    print("\n")

else:
  print("Pattern Not Possible")
    
