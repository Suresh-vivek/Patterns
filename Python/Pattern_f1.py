"""
Patetrn

         1
       2 1
     3 2 1
   4 3 2 1

   n = 4

"""
print("Enter the number of rows")
n=int(input())

print("Here is the Pattern")
for i in range(1,n+1):
    k=n
    while k>=i:
        print(" ",end=" ")
        k-=1

        l=i
    for j in range(1,i+1):
        print(l,end=" ")
        l-=1
    
    print("\n")