m = int(input("Enter the starting number (m): "))
n = int(input("Enter the ending number (n): "))
if m > n:
    m, n = n, m

print("Prime numbers between", m, "and", n, "are:")

for num in range(m, n + 1):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num, end=" ")
