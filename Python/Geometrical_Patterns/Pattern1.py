"""
Patetrn

ROW1 COLUMN1    ROW1 COLUMN2   ROW1 COLUMN3
ROW2 COLUMN1    ROW2 COLUMN2   ROW2 COLUMN3
ROW3 COLUMN1    ROW3 COLUMN2   ROW3 COLUMN3


Here r=3 (Number of rows)
     c=3 (Number of columns)

"""

print("Enter the number of Rows:-")
r= int(input())
print("\n")
print("Enter the number of Columns")
c= int(input())

print("Here is the Pattern")

for i in range(1,r+1):
    for j in range(1,c+1):
        print("Row",i,"Column",j,end="   ")
    print("\n")