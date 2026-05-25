def is_prime(number):
    """Check if a number is prime"""
    # Numbers less than 2 are not prime
    if number < 2:
        return False
    
    # Check for factors from 2 to square root of number
    # This is more efficient than checking all numbers up to n
    for i in range(2, int(number ** 0.5) + 1):
        # If number is divisible by i, it's not prime
        if number % i == 0:
            return False
    
    # If no factors found, number is prime
    return True

def find_primes(limit):
    """Find all prime numbers up to a limit"""
    # Create an empty list to store prime numbers
    primes = []
    
    # Check each number from 2 to limit
    for num in range(2, limit + 1):
        # Add to list if it's prime
        if is_prime(num):
            primes.append(num)
    
    return primes

# Main execution
if __name__ == "__main__":
    # Find all prime numbers up to 50
    limit = 50
    primes = find_primes(limit)
    print(f"Prime numbers up to {limit}: {primes}")
