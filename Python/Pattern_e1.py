
"""
Patetrn

A B C D
B C D
C D
D
n = 4

"""
# ASCII value of A=65, B=66 and so on
# chr() function is used to convert ASCII values to character

print("Enter the number of rows")
n=int(input())

print("Here is the pattern")

for i in range(1,n+1):
    for j in range(i,n+1):
        print(chr(j+64),end=" ")
        j+=1
    
    print("\n")


