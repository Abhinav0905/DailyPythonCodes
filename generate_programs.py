"""
Automated Python Program Generator
This script generates 5 unique Python programs daily with inline comments.
"""

import os
from datetime import datetime
import random

# List of program topics and templates
PROGRAM_TEMPLATES = [
    {
        "name": "fibonacci_generator",
        "code": '''def fibonacci(n):
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
'''
    },
    {
        "name": "palindrome_checker",
        "code": '''def is_palindrome(text):
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
'''
    },
    {
        "name": "prime_numbers",
        "code": '''def is_prime(number):
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
'''
    },
    {
        "name": "word_frequency_counter",
        "code": '''def count_word_frequency(text):
    """Count the frequency of each word in a text"""
    # Convert text to lowercase and split into words
    words = text.lower().split()
    
    # Create an empty dictionary to store word counts
    frequency = {}
    
    # Iterate through each word
    for word in words:
        # Remove common punctuation marks from the word
        word = word.strip('.,!?;:"')
        
        # Increment the count for this word
        # get() returns 0 if word not in dictionary yet
        frequency[word] = frequency.get(word, 0) + 1
    
    # Return the frequency dictionary
    return frequency

# Main execution
if __name__ == "__main__":
    # Sample text for analysis
    sample_text = "Python is great. Python is powerful. Python is versatile."
    
    # Get word frequencies
    word_freq = count_word_frequency(sample_text)
    
    # Display results sorted by frequency (descending)
    print("Word Frequency Count:")
    for word, count in sorted(word_freq.items(), key=lambda x: x[1], reverse=True):
        print(f"{word}: {count}")
'''
    },
    {
        "name": "temperature_converter",
        "code": '''def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    # Apply the conversion formula: F = (C × 9/5) + 32
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    # Apply the conversion formula: C = (F - 32) × 5/9
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def celsius_to_kelvin(celsius):
    """Convert Celsius to Kelvin"""
    # Apply the conversion formula: K = C + 273.15
    kelvin = celsius + 273.15
    return kelvin

# Main execution
if __name__ == "__main__":
    # Test temperature in Celsius
    temp_c = 25
    
    # Convert to different scales
    temp_f = celsius_to_fahrenheit(temp_c)
    temp_k = celsius_to_kelvin(temp_c)
    
    # Display the results
    print(f"{temp_c}°C = {temp_f}°F = {temp_k}K")
'''
    },
    {
        "name": "list_operations",
        "code": '''def find_max_min(numbers):
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
'''
    },
    {
        "name": "string_reverser",
        "code": '''def reverse_string(text):
    """Reverse a string using different methods"""
    # Method 1: Using slicing (most Pythonic way)
    reversed_text = text[::-1]
    return reversed_text

def reverse_words(sentence):
    """Reverse the order of words in a sentence"""
    # Split the sentence into words
    words = sentence.split()
    
    # Reverse the list of words
    words.reverse()
    
    # Join the words back into a sentence
    reversed_sentence = ' '.join(words)
    return reversed_sentence

# Main execution
if __name__ == "__main__":
    # Test string reversal
    original = "Hello World"
    reversed_str = reverse_string(original)
    print(f"Original: {original}")
    print(f"Reversed: {reversed_str}")
    
    # Test word order reversal
    sentence = "Python is an amazing language"
    reversed_words_str = reverse_words(sentence)
    print(f"\\nOriginal sentence: {sentence}")
    print(f"Reversed words: {reversed_words_str}")
'''
    },
    {
        "name": "factorial_calculator",
        "code": '''def factorial_iterative(n):
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
'''
    },
    {
        "name": "list_comprehension_examples",
        "code": '''# Example 1: Squares of numbers
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
    print(f"\\nEven numbers: {evens}")
    
    # Test string manipulation
    words = ["hello", "world", "python"]
    upper_words = uppercase_words(words)
    print(f"\\nUppercase words: {upper_words}")
'''
    },
    {
        "name": "dictionary_operations",
        "code": '''def merge_dictionaries(dict1, dict2):
    """Merge two dictionaries"""
    # Create a copy of the first dictionary
    merged = dict1.copy()
    
    # Update with values from second dictionary
    # If keys overlap, dict2 values take precedence
    merged.update(dict2)
    
    return merged

def invert_dictionary(original_dict):
    """Swap keys and values in a dictionary"""
    # Create new dictionary with swapped key-value pairs
    # Using dictionary comprehension
    inverted = {value: key for key, value in original_dict.items()}
    return inverted

def filter_dictionary(dictionary, min_value):
    """Filter dictionary items based on value threshold"""
    # Keep only items where value is >= min_value
    filtered = {k: v for k, v in dictionary.items() if v >= min_value}
    return filtered

# Main execution
if __name__ == "__main__":
    # Test dictionary merging
    dict1 = {"a": 1, "b": 2}
    dict2 = {"c": 3, "d": 4}
    merged = merge_dictionaries(dict1, dict2)
    print(f"Merged dictionary: {merged}")
    
    # Test dictionary inversion
    grades = {"Alice": "A", "Bob": "B", "Charlie": "A"}
    inverted = invert_dictionary(grades)
    print(f"\\nInverted dictionary: {inverted}")
    
    # Test dictionary filtering
    scores = {"Alice": 85, "Bob": 72, "Charlie": 90, "David": 65}
    filtered = filter_dictionary(scores, 75)
    print(f"\\nScores >= 75: {filtered}")
'''
    },
    {
        "name": "file_statistics",
        "code": '''def count_lines_words_chars(text):
    """Count lines, words, and characters in text"""
    # Split text into lines
    lines = text.split('\\n')
    line_count = len(lines)
    
    # Split text into words
    words = text.split()
    word_count = len(words)
    
    # Count all characters including spaces
    char_count = len(text)
    
    # Return statistics as a dictionary
    return {
        'lines': line_count,
        'words': word_count,
        'characters': char_count
    }

def find_longest_word(text):
    """Find the longest word in text"""
    # Split text into words and remove punctuation
    words = text.split()
    
    # Initialize variables to track longest word
    longest = ""
    
    # Iterate through words to find the longest
    for word in words:
        # Remove punctuation for accurate length comparison
        clean_word = word.strip('.,!?;:"')
        # Update longest if current word is longer
        if len(clean_word) > len(longest):
            longest = clean_word
    
    return longest

# Main execution
if __name__ == "__main__":
    # Sample text for analysis
    sample_text = """Python is a high-level programming language.
It is widely used for web development, data science, and automation.
Python's syntax is clean and readable."""
    
    # Get text statistics
    stats = count_lines_words_chars(sample_text)
    print("Text Statistics:")
    print(f"Lines: {stats['lines']}")
    print(f"Words: {stats['words']}")
    print(f"Characters: {stats['characters']}")
    
    # Find longest word
    longest = find_longest_word(sample_text)
    print(f"\\nLongest word: {longest}")
'''
    },
    {
        "name": "sorting_algorithms",
        "code": '''def bubble_sort(arr):
    """Sort an array using bubble sort algorithm"""
    # Create a copy to avoid modifying original array
    array = arr.copy()
    n = len(array)
    
    # Outer loop for number of passes
    for i in range(n):
        # Flag to optimize by detecting if array is already sorted
        swapped = False
        
        # Inner loop for comparisons
        # -i-1 because largest elements bubble to the end
        for j in range(0, n - i - 1):
            # Compare adjacent elements
            if array[j] > array[j + 1]:
                # Swap if they're in wrong order
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        
        # If no swaps occurred, array is sorted
        if not swapped:
            break
    
    return array

def selection_sort(arr):
    """Sort an array using selection sort algorithm"""
    # Create a copy to avoid modifying original array
    array = arr.copy()
    n = len(array)
    
    # Iterate through the array
    for i in range(n):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i + 1, n):
            # Update min_idx if smaller element found
            if array[j] < array[min_idx]:
                min_idx = j
        
        # Swap the found minimum with the first element
        array[i], array[min_idx] = array[min_idx], array[i]
    
    return array

# Main execution
if __name__ == "__main__":
    # Unsorted array for testing
    numbers = [64, 34, 25, 12, 22, 11, 90]
    
    print(f"Original array: {numbers}")
    
    # Test bubble sort
    sorted_bubble = bubble_sort(numbers)
    print(f"Bubble sort result: {sorted_bubble}")
    
    # Test selection sort
    sorted_selection = selection_sort(numbers)
    print(f"Selection sort result: {sorted_selection}")
'''
    },
    {
        "name": "number_guessing_game",
        "code": '''import random

def play_number_guessing_game():
    """Simple number guessing game"""
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    # Initialize attempt counter
    attempts = 0
    max_attempts = 10
    
    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between 1 and 100")
    print(f"You have {max_attempts} attempts to guess it.\\n")
    
    # Game loop
    while attempts < max_attempts:
        # Simulate user input for demonstration
        # In real game, you'd use: guess = int(input("Enter your guess: "))
        guess = random.randint(1, 100)
        attempts += 1
        
        print(f"Attempt {attempts}: Guessed {guess}")
        
        # Check if guess is correct
        if guess == secret_number:
            print(f"Congratulations! You won in {attempts} attempts!")
            return True
        # Provide hints
        elif guess < secret_number:
            print("Too low! Try a higher number.\\n")
        else:
            print("Too high! Try a lower number.\\n")
    
    # If max attempts reached
    print(f"Game Over! The number was {secret_number}")
    return False

# Main execution
if __name__ == "__main__":
    # Play the game
    play_number_guessing_game()
'''
    },
    {
        "name": "class_student_management",
        "code": '''class Student:
    """Represents a student with their information and grades"""
    
    def __init__(self, name, student_id):
        """Initialize student with name and ID"""
        # Store student's basic information
        self.name = name
        self.student_id = student_id
        # Initialize empty list for grades
        self.grades = []
    
    def add_grade(self, grade):
        """Add a grade to the student's record"""
        # Validate grade is between 0 and 100
        if 0 <= grade <= 100:
            self.grades.append(grade)
            return True
        return False
    
    def calculate_average(self):
        """Calculate the average of all grades"""
        # Check if student has any grades
        if not self.grades:
            return 0
        
        # Calculate and return average
        return sum(self.grades) / len(self.grades)
    
    def get_letter_grade(self):
        """Convert average to letter grade"""
        # Get numerical average
        avg = self.calculate_average()
        
        # Determine letter grade based on average
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        elif avg >= 60:
            return 'D'
        else:
            return 'F'
    
    def display_info(self):
        """Display student information"""
        avg = self.calculate_average()
        letter = self.get_letter_grade()
        print(f"Student: {self.name} (ID: {self.student_id})")
        print(f"Grades: {self.grades}")
        print(f"Average: {avg:.2f} (Letter Grade: {letter})")

# Main execution
if __name__ == "__main__":
    # Create a student object
    student = Student("John Doe", "S001")
    
    # Add some grades
    student.add_grade(85)
    student.add_grade(92)
    student.add_grade(78)
    student.add_grade(88)
    
    # Display student information
    student.display_info()
'''
    },
    {
        "name": "binary_search",
        "code": '''def binary_search(arr, target):
    """Search for target in sorted array using binary search"""
    # Initialize left and right pointers
    left = 0
    right = len(arr) - 1
    
    # Continue searching while search space is valid
    while left <= right:
        # Calculate middle index (avoiding overflow)
        mid = left + (right - left) // 2
        
        # Check if target is at middle
        if arr[mid] == target:
            return mid  # Return index where target was found
        
        # If target is greater, ignore left half
        elif arr[mid] < target:
            left = mid + 1
        
        # If target is smaller, ignore right half
        else:
            right = mid - 1
    
    # Target not found in array
    return -1

def binary_search_recursive(arr, target, left, right):
    """Recursive implementation of binary search"""
    # Base case: search space is empty
    if left > right:
        return -1
    
    # Calculate middle index
    mid = left + (right - left) // 2
    
    # Check if target found at middle
    if arr[mid] == target:
        return mid
    
    # Recursively search in left or right half
    elif arr[mid] < target:
        # Search in right half
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        # Search in left half
        return binary_search_recursive(arr, target, left, mid - 1)

# Main execution
if __name__ == "__main__":
    # Sorted array for binary search
    sorted_array = [2, 5, 8, 12, 16, 23, 38, 45, 56, 67, 78]
    target = 23
    
    # Test iterative binary search
    result = binary_search(sorted_array, target)
    if result != -1:
        print(f"Element {target} found at index {result}")
    else:
        print(f"Element {target} not found")
    
    # Test recursive binary search
    result_rec = binary_search_recursive(sorted_array, target, 0, len(sorted_array) - 1)
    print(f"Recursive search result: index {result_rec}")
'''
    }
]


def create_daily_directory():
    """Create directory for today's date"""
    # Get current date in YYYY-MM-DD format
    today = datetime.now().strftime("%Y-%m-%d")
    
    # Create directory path
    directory = f"programs/{today}"
    
    # Create directory if it doesn't exist
    os.makedirs(directory, exist_ok=True)
    
    return directory


def generate_daily_programs():
    """Generate 5 unique Python programs for today"""
    # Create today's directory
    directory = create_daily_directory()
    
    # Shuffle templates to get random selection
    shuffled_templates = random.sample(PROGRAM_TEMPLATES, min(5, len(PROGRAM_TEMPLATES)))
    
    # Generate timestamp for file naming
    timestamp = datetime.now().strftime("%Y%m%d")
    
    # Counter for generated files
    generated_files = []
    
    # Generate 5 programs
    for i, template in enumerate(shuffled_templates, 1):
        # Create filename with timestamp and program name
        filename = f"{timestamp}_{i:02d}_{template['name']}.py"
        filepath = os.path.join(directory, filename)
        
        # Write the program to file
        with open(filepath, 'w') as f:
            f.write(template['code'])
        
        # Add to list of generated files
        generated_files.append(filepath)
        print(f"✓ Generated: {filepath}")
    
    return generated_files


def main():
    """Main execution function"""
    print("=" * 60)
    print("Daily Python Program Generator")
    print("=" * 60)
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 60)
    
    # Generate programs
    files = generate_daily_programs()
    
    print("-" * 60)
    print(f"Successfully generated {len(files)} programs!")
    print("=" * 60)


if __name__ == "__main__":
    main()
