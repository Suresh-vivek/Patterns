print("Enter the number of rows")
n=int(input())

print("Here is the pattern")

i=n
while i>=1:
    j=n
    while j>=i:
        print(j,end=" ")
        j-=1
    print("\n")
    i-=1