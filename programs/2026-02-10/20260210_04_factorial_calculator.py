def factorial_iterative(n):
    """Calculate factorial using iterative approach"""
    # Check for negative input
    if n < 0:
        return None
    
    # Initialize result to 1
    result = 1
    
    # Multiply all numbers from 1 to n
    for i in range(1, n + 1):
        result *= i
    
    # Return the final factorial value
    return result

def factorial_recursive(n):
    """Calculate factorial using recursive approach"""
    # Base case: factorial of 0 or 1 is 1
    if n <= 1:
        return 1
    
    # Recursive case: n! = n × (n-1)!
    return n * factorial_recursive(n - 1)

# Main execution
if __name__ == "__main__":
    # Test number for factorial calculation
    number = 5
    
    # Calculate using both methods
    result_iter = factorial_iterative(number)
    result_rec = factorial_recursive(number)
    
    # Display results
    print(f"Factorial of {number} (iterative): {result_iter}")
    print(f"Factorial of {number} (recursive): {result_rec}")
