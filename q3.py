def update_dictionary(dct, key, value):
    """
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """
    if not isinstance(dct, dict):
        raise ValueError("First argument must be a dictionary.")

    if key in dct:
        print(f"Original value for key '{key}':", dct[key])
    
    dct[key] = value
    return dct


# Task 2: Invoke the function using the given scenarios

# Scenario 1: Adding a new key-value pair
result1 = update_dictionary({}, "name", "Alice")
print("Scenario 1 result:", result1)

# Scenario 2: Updating an existing key's value
result2 = update_dictionary({"age": 25}, "age", 26)
print("Scenario 2 result:", result2)
