"""
Patetrn

* * * *
* * * *
* * * *
* * * *
n = 4

"""
print("Enter the number of rows")
n=int(input())

print("Here is the pattern")

for i in range(1, n+1):
    for j in range(1,n+1):
        print("*",end=" ")
    
    print("\n")