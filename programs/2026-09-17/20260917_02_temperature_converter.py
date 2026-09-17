def celsius_to_fahrenheit(celsius):
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
