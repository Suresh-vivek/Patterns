"""
Patetrn

1 
1 2 
1 2 3
1 2 3 4
n = 4

"""
print("Enter the number of rows")
n=int(input())

print("Here is the pattern")


for i in range(1,n+1):
    j=1
    while j<=i:
        print(j,end=" ")
        j+=1

    print("\n")

    