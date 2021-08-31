# WAP LCM , HCF , GCD
num1 = int(input("Enter the Number: "))
num2 = int(input("Enter the another Number: "))

a = num1
b = num2
while b!=0:
    x = b
    b = a%b
    a = x

hcf = a
lcm = int((num1*num2)/hcf)

'''if a > b:
    y = b  
else:  
    y = a  
    for i in range(1, y + 1):  
        if (( a % i == 0) and (b % i == 0 )):  
            gcd = i'''
        
        
print("LCM of two numbers is :" , lcm)
print("HCF of two numbers is:" , hcf)