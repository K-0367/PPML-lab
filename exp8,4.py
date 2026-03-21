def factorial(n):
    if n < 0:
        return None 
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
fact1 = factorial(num1)
fact2 = factorial(num2)

if fact1 is None:
    print(f"Factorial is not defined for {num1}")
else:
    print(f"Factorial of {num1} is: {fact1}")

if fact2 is None:
    print(f"Factorial is not defined for {num2}")
else:
    print(f"Factorial of {num2} is: {fact2}")
