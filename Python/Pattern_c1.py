"""
Patetrn

1 2 3 4
1 2 3 4
1 2 3 4
1 2 3 4

n = 4

"""

print("Enter the number of rows")
n=int(input())

print("Here is the pattern")

for i in range(1,n+1):
    for j in range(1,n+1):
        print(j,end=" ")
    print("\n")
