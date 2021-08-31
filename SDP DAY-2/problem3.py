#WAP to calculate fibnocci series 0 1 1 2 3 5 8 13

num = int(input("Enter the Range Number: "))
num1= 0
num2= 1
for n in range(0, num):
    if(n <= 1):
        x = n
        print(x)
    else:
        x = num1 + num2
        num1 = num2
        num2 = x
        print(x)