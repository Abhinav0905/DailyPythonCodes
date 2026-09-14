def binary_search(arr, target):
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
