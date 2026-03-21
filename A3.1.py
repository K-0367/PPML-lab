#wap to print the twin prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
limit = int(input("Enter the limit: "))

print("Twin primes up to", limit, ":")
for i in range(2, limit-1):
    if is_prime(i) and is_prime(i+2):
        print("(", i, ",", i+2, ")")