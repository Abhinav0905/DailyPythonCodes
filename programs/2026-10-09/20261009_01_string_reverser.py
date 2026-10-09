def reverse_string(text):
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
    print(f"\nOriginal sentence: {sentence}")
    print(f"Reversed words: {reversed_words_str}")
