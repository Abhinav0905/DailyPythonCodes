def count_lines_words_chars(text):
    """Count lines, words, and characters in text"""
    # Split text into lines
    lines = text.split('\n')
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
    print(f"\nLongest word: {longest}")
