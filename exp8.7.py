def prime(n):
    count = 1
    for i in range(2, n):
        if n % i == 0:
            count += 1
    
    if(count != 1):
        return "Not prime"
    else:
        return "prime"

n = int(input("Enter a number"))
print(prime(n))