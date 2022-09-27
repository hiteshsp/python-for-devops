names = ["messi", "ronaldo", "maradona"]

legends = list()

"""
list() and [] creates a list. 

Which is preferred ?
[] faster than list()
"""

print(names)
print(legends)
print(type(names))
print(type(legends))

# Adds an entry
names.append("pele")
print(names)

# Clears a list
names.clear()
print(names)

# Find count of repeating numbers
list_of_numbers = [0,1,2,2,3,4,5,5,6,6,6,7]
print(list_of_numbers.count(9))

# Find count of repeating strings
list_of_names = ["messi", "ronaldo", "messi"]
print(list_of_names.count("messi"))

# Find all the operations which can be performed on list
print(dir(list_of_numbers))

names = ["messi", "ronaldo", "maradona"]
l = list_of_names.extend(names)
print(l)
print(list_of_names)

for item in list_of_names:
    print(item)

for iterator in range(0, len(list_of_names)):
    print(list_of_names[iterator])