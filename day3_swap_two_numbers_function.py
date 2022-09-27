# logic to swap two number
#swap function
def swap(num1,num2):
  temp=num1
  num1=num2
  num2=temp
  print("After swaping \nnum1= "+num1 +"\n"+ "num2= "+num2)

num1=input("Please enter first number: ")
num2=input("Please enter second number: ")
print("Before swaping \nnum1= "+num1 +"\n"+ "num2= "+num2)
swap(num1,num2)
