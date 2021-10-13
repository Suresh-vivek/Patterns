print("Enter the number of rows")
n=int(input())

print("Here is the pattern")

i=n
while i>=1:
    k=n
    for j in range(1,i+1):
        print(k,end=" ")
        j+=1
        k-=1
    print("\n")
    i-=1