"""
Patetrn

D
D C 
D C B
D C B A
n = 4

"""
# ASCII value of A=65, B=66 and so on
# chr() function is used to convert ASCII values to character

print("Enter the number of rows")
n=int(input())

print("Here is the pattern")

i=n
while i>=1:
    j=n
    while j>=i:
        print(chr(j+64),end=" ")
        j-=1
    print("\n")
    i-=1