"""
Patetrn

1 
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4 5
1 2 3 4
1 2 3
1 2 
1

n = 5
"""
print("Enter the number of rows")
n=int(input())

print("Here is the Pattern")

for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    
    print("\n")

i=n
while i>=1:
    for j in range(1,i+1):
        print(j,end=" ")

    i-=1    
    print("\n")
