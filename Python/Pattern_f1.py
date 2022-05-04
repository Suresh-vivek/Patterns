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
  s = 0 # s represent spaces
  while s < n -i:
    print(" ",end=" ")
    s+=1
  k = i
  for j in range(1,i+1):
    print(k,end=" ")
    k-=1
  print("\n")