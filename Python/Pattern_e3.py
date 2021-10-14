"""
Patetrn

D C B A
D C B
D C 
D
n = 4

"""

# ASCII value of A=65, B=66 and so on
# chr() function is used to convert ASCII values to character

print("Enter the number of rows")
n=int(input())

print("Here is the pattern")

i=n
while i>=1:
    k=n
    for j in range(1,i+1):
        print(chr(k+64),end=" ")
        j+=1
        k-=1
    print("\n")
    i-=1