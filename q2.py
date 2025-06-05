def find_and_replace(lst, find_val, replace_val):
    """
    Task 1
    - Create a function that searches for all occurrences of a value (find_val) in a given list (lst) and replaces them with another value (replace_val).
    - lst must be a list.
    - Return the modified list.
    """
    if not isinstance(lst, list):
        raise ValueError("Input must be a list.")

    # Replace all occurrences of find_val with replace_val
    for i in range(len(lst)):
        if lst[i] == find_val:
            lst[i] = replace_val

    return lst


# Task 2: Invoke the function using the given scenarios

# Scenario 1
result1 = find_and_replace([1, 2, 3, 4, 2, 2], 2, 5)
print("Scenario 1 result:", result1)

# Scenario 2
result2 = find_and_replace(["apple", "banana", "apple"], "apple", "orange")
print("Scenario 2 result:", result2)
