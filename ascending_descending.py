list=[]
n=int(input("enter the number of inputs:"))

for i in range(n):
    numbers=int(input("enter the numbers:"))
    list.append(numbers)
    
print("the original list:",list)
flag=0
if(list==sorted(list)):
  flag=1
  
if(flag==1):
   print("list is sorted")

else:
    print("list is not sorted")