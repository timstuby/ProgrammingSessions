#Dictionaries

'''
Dictionaries are a more general type of list. While in a list indices are integers, in a dictionary
they can be almost any immutable object. In the case of dictionaries, the index is called a 'key'. Like indices,
"keys" need to be unique and each key maps to a value. Dictionaries are mutable.
Dictionaries are created with {}
'''

my_dict = {0:"Hello", 1:"World", 2: "Python", 3:"Programming"}
print(my_dict[0])

my_dict2 = {"Hello":0, "World":1, "Python":2, "Programming":3, "Language": 4}
print(my_dict2["Hello"])

# Add elem to dict
my_dict[5] = "New"
print(my_dict)

# Change existing elem
my_dict[0] = "Hi"
print(my_dict)

my_dict[1] = ["this", "can", "be", "a", "list"]
print(my_dict)

# How to use the get method
## Returns the key of item specified in the dictionary.
print(my_dict.get(0))
print(my_dict.get(6))
print(my_dict.get(6, "Not found"))

# Use of keys and value methods
print(my_dict.keys())
print(my_dict.values())

# Use of items method
print(my_dict.items())

for key, value in my_dict.items():
    print(f"key: {key}, value: {value}")