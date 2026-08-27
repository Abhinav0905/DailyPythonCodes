def fibonacci(n):
    """Generate Fibonacci sequence up to n terms"""
    # Initialize the first two Fibonacci numbers
    a, b = 0, 1
    # Create an empty list to store the sequence
    fibonacci_sequence = []
    
    # Loop to generate n Fibonacci numbers
    for _ in range(n):
        # Append the current number to the sequence
        fibonacci_sequence.append(a)
        # Calculate the next Fibonacci number
        a, b = b, a + b
    
    # Return the complete sequence
    return fibonacci_sequence

# Main execution
if __name__ == "__main__":
    # Set the number of terms to generate
    terms = 10
    # Generate and display the Fibonacci sequence
    result = fibonacci(terms)
    print(f"First {terms} Fibonacci numbers: {result}")
