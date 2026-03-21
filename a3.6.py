#wap to remaove all the duplicates from a giver string
x=input("enter the string")
result=" "
for char in x:
    if char not in result:
        result=result+char
        print(result)