"""
Pattern is:

        1
      1 2
    1 2 3
  1 2 3 4

  n = 4
"""


print("Enter the number of rows")
n = int(input())
print("Here is the Pattern")

for i in range(1,n+1):
    s = 0
    while s < n -i:
        print(" ",end=" ")
        s+=1
    for j in range(1,i+1):
        print(j,end=" ")
    print("\n")
    
