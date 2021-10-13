print("Enter the number of rows")
n=int(input())

print("Here is the pattern")

for i in range(1,n+1):
    for j in range(i,n+1):
        print(j,end=" ")
        j+=1
    
    print("\n")


