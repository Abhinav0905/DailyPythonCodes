# Example 1: Squares of numbers
def generate_squares(n):
    """Generate squares of numbers from 1 to n using list comprehension"""
    # List comprehension: [expression for item in iterable]
    squares = [x**2 for x in range(1, n + 1)]
    return squares

# Example 2: Filter even numbers
def filter_even_numbers(numbers):
    """Filter even numbers from a list"""
    # List comprehension with condition
    # [expression for item in iterable if condition]
    evens = [num for num in numbers if num % 2 == 0]
    return evens

# Example 3: String manipulation
def uppercase_words(words):
    """Convert all words to uppercase"""
    # Apply string method to each element
    uppercase = [word.upper() for word in words]
    return uppercase

# Main execution
if __name__ == "__main__":
    # Test squares generation
    squares = generate_squares(10)
    print(f"Squares of 1-10: {squares}")
    
    # Test even number filtering
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    evens = filter_even_numbers(numbers)
    print(f"\nEven numbers: {evens}")
    
    # Test string manipulation
    words = ["hello", "world", "python"]
    upper_words = uppercase_words(words)
    print(f"\nUppercase words: {upper_words}")
