#WAP to enter hight of user in feets ans converts it into inches and cetimeter


#Height = int(input("Enter Height: "))
Height_ft = int(input("Enter Height in Feet: "))
Height_inch = int(input("Enter Height in Inches: "))

Height_inch= Height_inch + (Height_ft * 12)
Height_cm = int(Height_inch) * 2.54

print("Height in inch:",Height_inch)
print("Height in centimeter:",Height_cm)