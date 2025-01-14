def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return float('inf')
    except TypeError:
        return None

# Example with the uncommon error: trying to divide a string by a number
result = function_with_uncommon_error("hello", 5)
print(result)  # Output: None

# Example with the typical ZeroDivisionError
result = function_with_uncommon_error(10, 0)
print(result) # Output: inf

# Example with no errors
result = function_with_uncommon_error(10, 2)
print(result) # Output: 5.0