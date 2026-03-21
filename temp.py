celsius_list = [0, 10, -9, 30, 40]
fahrenheit_list = []
for c in celsius_list:
    f = (c * 9/5) + 32
    fahrenheit_list.append(f)

print("Celsius List:", celsius_list)
print("Fahrenheit List:", fahrenheit_list)
