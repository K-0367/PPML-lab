numbers = []
n = int(input("Enter number of elements: "))
for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

numbers = list(set(numbers))
numbers.sort()
print("List after removing duplicates and sorting:")
print(numbers)
