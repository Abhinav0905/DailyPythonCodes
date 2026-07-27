def count_word_frequency(text):
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
