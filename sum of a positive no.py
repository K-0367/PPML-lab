n=int(input("enter a positive number "))
s=0
while n >10:
    digit=n%10
    s+=digit
    n//=10
print("sum of digits")