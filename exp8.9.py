def simple_intrest(p,t,r):
    return(p*t*r)/100

p=int(input("enter the value of principal:"))
t=int(input("enter the value of time required:"))
r=int(input("enter the rate if intrest required:"))
si=(p*t*r)/100
print("simple intrest=", si)