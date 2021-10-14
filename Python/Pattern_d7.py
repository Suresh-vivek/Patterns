"""
Patetrn

4 3 2 1
3 2 1
2 1
1

n = 4

"""
print("Enter the number of rows")
n=int(input())

print("Here is the pattern")


i=n
while i>=1:
    j=i
    while j>=1:
        print(j,end=" ")
        j-=1
    print("\n")
    i-=1