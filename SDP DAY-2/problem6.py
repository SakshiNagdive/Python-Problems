#WAP to find palindrom number

num=int(input("Enter number:"))
n = num
rev=0
while(n>0):
    y =n%10
    rev=rev*10+ y
    n=n//10
if(num==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")