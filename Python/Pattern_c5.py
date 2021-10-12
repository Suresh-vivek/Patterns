print("Enter the number of rows")
n=int(input())

print("Here is the pattern")

for i in range(1,n+1):
    k=n
    for j in range(1,n+1):
        print(k,end=" ")
        k-=1
    print("\n")
