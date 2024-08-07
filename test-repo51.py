# Write a Python program to calculate the sum of values in a dictionary.

# Create a dictionary with some key-value pairs
my_dict = {
    'a': 10,
    'b': 20,
    'c': 30,
    'd': 40
}

# Function to calculate the sum of values in a dictionary


def sum_of_values(dictionary):
    # Use the sum function to add up all the values in the dictionary
    return sum(dictionary.values())


# Example usage
total_sum = sum_of_values(my_dict)
print(f"The sum of the values in the dictionary is: {total_sum}")
