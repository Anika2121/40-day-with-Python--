def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_and_list_primes(n):
    primes = []
    for i in range(2, n):
        if is_prime(i):
            primes.append(i)
    print(f"Output: {len(primes)} ({','.join(map(str, primes))})")


n = int(input("Enter a number: "))
count_and_list_primes(n)
