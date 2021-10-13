print("Enter the number of rows")
n=int(input())

print("Here is the pattern")

for i in range(1,n+1):
    j=i
    k=1
    while k<=i:
        print(j,end=" ")
        j-=1
        k+=1
    print("\n")
