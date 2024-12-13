num1= float(input("enter a number: "))
num2= float(input("enter a number: "))
num3= float(input("enter a number: "))
num4= float(input("enter a number: "))
num5= float(input("enter a number: "))

nums= [num1,num2,num3,num4,num5]
greatest= nums[0]

for num in nums[1:]:
    if num>greatest:
        greatest=num

print("the greatest is: ", greatest)