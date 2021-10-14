"""
Patetrn

1
0 1
0 1 0
1 0 1 0
1 0 1 0 1

n = 5

"""

print("Enter the number of rows")
n=int(input())

print("Here is the Pattern")
row,val=1,1
print("Here is the Pattern")

while row <= n:
    col=1
    while col <= row:
        print(val%2,end=" ")
        val+=1
        col+=1
    
    print("\n")
    row+=1