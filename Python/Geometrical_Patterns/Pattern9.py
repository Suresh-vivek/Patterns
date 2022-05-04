"""
pattern is:
         
         *
        * *
       * * *
      * * * *

      n = 4

"""

print("Enter the number of Rows")
n = int(input())

if n >=2:
    print("Here is the Pattern")
    for i in range(1,n+1):
        s = 0 # s represent spaces
        while s < n - i:
            print(" ",end=" ")
            s+=1
        for j in range(1,i+1):
            print("* ",end="  ")
        print("\n")

else:
    print("Pattern not Possible")
        