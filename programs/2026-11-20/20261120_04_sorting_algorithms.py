def bubble_sort(arr):
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
