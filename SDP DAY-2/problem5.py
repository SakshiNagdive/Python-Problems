#WAP to find armstrong number

num = int(input("Enter a number: "))
sum = 0
x = num
while x > 0:
   temp = x % 10
   sum =sum + temp ** 3
   x = x//10

if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")