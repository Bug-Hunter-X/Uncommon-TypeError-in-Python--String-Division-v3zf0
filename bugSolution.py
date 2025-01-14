def improved_function(a, b):
    if not isinstance(a,(int, float)) or not isinstance(b,(int, float)):
        return "Error: Inputs must be numbers"
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return float('inf') 

# Example with the improved function
result = improved_function("hello", 5)
print(result)  # Output: Error: Inputs must be numbers

result = improved_function(10, 0)
print(result)  # Output: inf

result = improved_function(10, 2)
print(result) # Output: 5.0