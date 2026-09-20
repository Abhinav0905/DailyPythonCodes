def find_max_min(numbers):
    """Find maximum and minimum values in a list"""
    # Check if list is empty
    if not numbers:
        return None, None
    
    # Initialize max and min with the first element
    max_val = numbers[0]
    min_val = numbers[0]
    
    # Iterate through the list to find max and min
    for num in numbers:
        # Update max if current number is greater
        if num > max_val:
            max_val = num
        # Update min if current number is smaller
        if num < min_val:
            min_val = num
    
    # Return both values as a tuple
    return max_val, min_val

# Main execution
if __name__ == "__main__":
    # Sample list of numbers
    numbers = [45, 12, 67, 23, 89, 34, 56]
    
    # Find maximum and minimum
    max_num, min_num = find_max_min(numbers)
    print(f"List: {numbers}")
    print(f"Maximum: {max_num}")
    print(f"Minimum: {min_num}")
