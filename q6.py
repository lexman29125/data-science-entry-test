def find_first_negative(lst):
    """
    Task 1
    - Create a function that finds the first negative number in a list (lst).
    - Return the first negative number if found, otherwise return "No negatives".
    - Use a while loop to implement this.
    """
    if not isinstance(lst, list):
        raise ValueError("Input must be a list.")

    i = 0
    while i < len(lst):
        if lst[i] < 0:
            return lst[i]
        i += 1
    
    return "No negatives"


# Task 2: Invoke the function using the given scenarios

# Scenario 1
result1 = find_first_negative([3, 5, -1, 7, -2, 8])
print("Scenario 1 result:", result1)

# Scenario 2
result2 = find_first_negative([2, 10, 7, 0])
print("Scenario 2 result:", result2)
