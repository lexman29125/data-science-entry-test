def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """
    # Check if both x and y are numeric
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        return -1

    # Swap values using arithmetic operations (no third variable)
    x = x + y
    y = x - y
    x = x - y

    print("Swapped values:", x, y)

# Task 2: Invoke the function with given scenarios

# Scenario 1: Non-numeric input
result1 = swap("Apple", 10)
if result1 == -1:
    print("Scenario 1: Invalid input, result =", result1)

# Scenario 2: Numeric input
print("Scenario 2:")
swap(9, 17)
