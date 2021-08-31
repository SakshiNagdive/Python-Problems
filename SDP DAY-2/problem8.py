#Enter five integer number and find min mumber ( using simple if)

num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
num3 = int(input("Enter the third number:"))
num4 = int(input("Enter the fourth number:"))
num5 = int(input("Enter the fifth number:"))

if num1 < num2 and num1 < num3 and num1 < num4 and num1 < num5:
    print("Minimum number :" , num1)

elif num2 < num1 and num2 < num3 and num2 < num4 and num2 < num5:
    print("Minimum number :" , num2)

elif num3 < num1 and num3 < 2 and num3 < num4 and num3 < num5:
    print("Minimum number :" , num3)

elif num4 < num1 and num4 < num2 and num4 < num3 and num2 < num5:
    print("Minimum number :" , num4)

else:
    print("Minimum number : ", num5)