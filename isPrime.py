def print_primes(start, end):
    for num in range(start, end + 1):
        if num > 1:  # 1 is not a prime number
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    break
            else:
                print(num)

# Example usage:
print_primes(10, 50)
