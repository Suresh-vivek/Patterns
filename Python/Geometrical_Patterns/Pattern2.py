"""
Pattern

A B C D E
B C D E F
C D E F G
D E F G H
E F G H I

n = 5

"""
# ASCII value of A=65, B=66 and so on
# chr() function is used to convert ASCII values to character
# Here maximum value of n could be 13


print("Enter the number of rows")
n= int(input())

if n<=13:
    for i in range(1,n+1):
        k=i
        for j in range(1,n+1):
            print(chr(k+64),end=" ")
            k+=1
        print("\n")
else:
    print("Alphabetical Pattern Not Possible")



