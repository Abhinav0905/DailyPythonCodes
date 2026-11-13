def merge_dictionaries(dict1, dict2):
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
    print(f"\nInverted dictionary: {inverted}")
    
    # Test dictionary filtering
    scores = {"Alice": 85, "Bob": 72, "Charlie": 90, "David": 65}
    filtered = filter_dictionary(scores, 75)
    print(f"\nScores >= 75: {filtered}")
