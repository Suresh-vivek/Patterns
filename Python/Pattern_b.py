"""
Patetrn

1 
2 3 2
3 4 5 4 3
4 5 6 7 6 5 4

n = 4

"""

print("Enter the number of rows")
n=int(input())

i=1

print("Here is the Pattern")

while i <=n:
    k = i
    j=1
    while j<=i:
        print(k,end=" ")
        k+=1
        j+=1
    
    k=k-2

    j=1
    while j<i:
        print(k,end=" ")
        k-=1
        j+=1
    print("\n")
    i=i+1