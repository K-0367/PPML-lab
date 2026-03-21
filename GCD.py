def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))
result = gcd(gcd(x, y), z)

print("GCD of the three numbers is:", result)