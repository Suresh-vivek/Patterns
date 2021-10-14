"""
Patetrn

4
4 3
4 3 2
4 3 2 1

n = 4

"""
print("Enter the number of rows")
n=int(input())

print("Here is the pattern")


for i in range(1,n+1):
    k=n
    j=1
    while j<=i:
        print(k,end=" ")
        k-=1
        j+=1
    print("\n")