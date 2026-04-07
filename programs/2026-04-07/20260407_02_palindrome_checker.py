def is_palindrome(text):
    """Check if a string is a palindrome"""
    # Remove spaces and convert to lowercase for accurate comparison
    cleaned_text = text.replace(" ", "").lower()
    
    # Compare the string with its reverse
    # [::-1] creates a reversed copy of the string
    return cleaned_text == cleaned_text[::-1]

# Main execution
if __name__ == "__main__":
    # Test strings for palindrome checking
    test_strings = ["racecar", "hello", "A man a plan a canal Panama"]
    
    # Check each string and print the result
    for string in test_strings:
        # Call the palindrome checker function
        result = is_palindrome(string)
        print(f"'{string}' is palindrome: {result}")
