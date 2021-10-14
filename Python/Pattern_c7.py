"""
Patetrn

1 
2 2
3 3 3
4 4 4 4

n = 4

"""
print("Enter the number of rows")
n=int(input())

print("Here is the pattern")


for i in range(1,n+1):
    j=1
    while j<=i:
        print(i,end=" ")
        j+=1

    print("\n")

    