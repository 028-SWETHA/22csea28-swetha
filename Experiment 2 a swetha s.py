#SWAPPING TWO NUMBERS -METHOD 1
a=int(input("enter the first value:"))
b=int(input("enter the second value:"))
print("The values before swapping are",a,b)
a=b
print("The values after swapping are",b,a)


#SWAPPING TWO NUMBERS -METHOD 2
a=59
b=16
print("The values before swapping :",a,b)
a,b=a,b
print("The values after swapping:",a,b)


#SWAPPING TWO NUMBERS -METHOD 3
x=45
y=25
print("The values before swapping are",x,y)
x=x+y
y=x-y
x=x-y
print ("The values after swapping are",x,y)
       

#SWAPPING TWO NUMBERS -METHOD 4
j=58
k=46
print("The values before swapping are",j,k)
j=j^k
k=j^k
j=j^k
print("The values after swapping are",j,k)

#CIRCULATE THE VALUES OF n VARIABLES -METHOD 1
s=int(input("Enter a values in the list:"))
list=[]

for i in range(0,s):
      element=int(input("Enter the value:"))
      list.append(element)
      print("circulating the list")            
for i in range (0,s):
      element_deleted=list. pop(0)
      list.append(element_deleted)
      print("The circulated list after",i+1,"rotation",list)
      
#CIRCULATE THE VALUES OF n VARIABLES -METHOD 2
def circulate(c,n):
 i in range(1,n+1)
 d=c[i:]+c[:i]
print("circulate","=",d)
c=[345,789,235,908,756,324,356]
n=int(input("Enter n:"))
circulate(c,n)

#DISTANCE BETWEEN TWO POINTS
x1=int(input("Enter the value of x1:"))
x2=int(input("Enter the value of x2:"))
y1=int(input("Enter the value of y1:"))
y2=int(input("Enter the value of y2:"))
d1=(x2-x1)**2
d2=(y2-y1)**2
result=(d1+d2)**5
print("Distance between ",(x1,x2),"and",(Y1,y2),"is result")
