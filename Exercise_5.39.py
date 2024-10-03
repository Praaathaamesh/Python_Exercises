# Programs for demonstrating the usage of all the different dictionary methods along with their variations.

# Initialize a dictionary
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
# clear()
print("Before clear():", my_dict)
my_dict.clear()  # Clears all elements from the dictionary
print("After clear():", my_dict)

# Re-initialize the dictionary
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
# copy()
copied_dict = my_dict.copy()
print("\nOriginal dictionary:", my_dict)
print("Copied dictionary:", copied_dict)
# Modifying the copied dictionary
copied_dict["name"] = "Bob"
print("Modified copied dictionary:", copied_dict)
print("Original dictionary after modification:", my_dict)
# fromkeys(keys, value)
keys = ['a', 'b', 'c']
default_value = 0
new_dict = dict.fromkeys(keys, default_value)
print("\nNew dictionary from keys using fromkeys():", new_dict)
# get()
age = my_dict.get("age")
print("\nUsing get() to fetch 'age':", age)
country = my_dict.get("country", "USA")
print("Using get() with default value for 'country':", country)
# items()
items = my_dict.items()  # Get key-value pairs
print("\nDictionary items using items():", list(items))
# keys()
keys = my_dict.keys()  # Get keys
print("Dictionary keys using keys():", list(keys))
# pop()
removed_value = my_dict.pop("age")  # Remove 'age' key
print("\nRemoved value using pop():", removed_value)
print("Dictionary after pop():", my_dict)
# Pop with default value for non-existing key
removed_value = my_dict.pop("country", "Not Found")
print("Trying to pop non-existing key 'country' with default:", removed_value)
# update()
update_dict = {"city": "Los Angeles", "age": 30}
my_dict.update(update_dict)
print("\nDictionary after update():", my_dict)
# Update using key-value pairs
my_dict.update([("name", "Charlie"), ("country", "USA")])
print("Dictionary after updating with key-value pairs:", my_dict)
# values()
values = my_dict.values()  # Get values
print("\nDictionary values using values():", list(values))