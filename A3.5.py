#wap to print even length words in the string
x=input("enter a string")
x=x.split()
for i in x:
    if len(i)%2==0:
        print(i)