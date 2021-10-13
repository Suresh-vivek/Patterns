# ASCII value of A=65, B=66 and so on
# chr() function is used to convert ASCII values to character


print("Enter the number of rows")
n=int(input())

print("Here is the pattern")

for i in range(1,n+1):
    j=i
    k=1
    while k<=i:
        print(chr(j+64),end=" ")
        j-=1
        k+=1
    print("\n")
