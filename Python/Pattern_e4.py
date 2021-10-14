"""
Patetrn

D C B A
C B A
B A
A
n = 4

"""
# ASCII value of A=65, B=66 and so on
# chr() function is used to convert ASCII values to character

print("Enter the number of rows")
n=int(input())

print("Here is the pattern")


i=n
while i>=1:
    j=i
    while j>=1:
        print(chr(j+64),end=" ")
        j-=1
    print("\n")
    i-=1