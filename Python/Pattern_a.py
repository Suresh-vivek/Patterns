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