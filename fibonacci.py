a,b = 0, 1
even_sum = 0
for x in range(1000):
    if a > 1000:
        break
    print(a, end=" ")
    
    if a % 2 == 0:
        even_sum += a
    
    a, b = b, a + b

print("\nSum of even-valued terms:", even_sum)
