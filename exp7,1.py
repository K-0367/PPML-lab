m = int(input("Enter the starting number (m): "))
n = int(input("Enter the ending number (n): "))
if m > n:
    m, n = n, m


num_list = list(range(m, n + 1))

total_sum = sum(num_list)
average = total_sum / len(num_list)
largest = max(num_list)
smallest = min(num_list)
new_list = [x for x in num_list if x != 3]

print("Original List:", num_list)
print("Sum:", total_sum)
print("Average:", average)
print("Largest number:", largest)
print("Smallest number:", smallest)
print("List without 3:", new_list)
                                                                                                                                                  