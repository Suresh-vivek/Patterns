"""
Patetrn

1
2 3
4 5 6 
7 8 9 10

n = 4

"""

print("Enter the number of rows")
n=int(input())

row,val=1,1
print("Here is the Pattern")

while row <= n:
    col=1
    while col <= row:
        print(val,end=" ")
        val+=1
        col+=1
    
    print("\n")
    row+=1