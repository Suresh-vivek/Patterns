"""
Pattern

*           *
  *       *
    *   *
      *
    *   *
  *       *
*           *

n = 7
              
"""

# minimum value of n = 3

print("Enter the number of rows")
n = int(input())

if n >= 3:
    # for odd values
    if n%2 !=0:
        for i in range(1,n+1):
            for j in range(1,n+1):
                if i == j or i + j == n+1:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print("\n")

    
    # for even values
    else:
        for i in range(1,int(n/2+1)):
            for j in range(1,int(n/2+1)):
              if i == j:
                print("*",end=" ")
              else:
                print(" ",end=" ")
            
            for j in range(1,int(n/2 + 1)):
              if j ==  int(n/2) - i +1:
                print("*",end=" ")
              else:
                print(" ",end=" ")
            print("\n")
        
        for i in range(1, int(n/2+1)):
          for j in range(1, int(n/2+1)):
            if j == int(n/2) - i + 1:
              print("*",end=" ")
            else:
              print(" ",end=" ")
            
          for j in range(1, int(n/2 + 1)):
            if i == j:
              print("*",end=" ")
            else:
              print(" ",end=" ")
          print("\n")

else:
  print("Pattern not possible")

          
          



              
                

    
    
    
