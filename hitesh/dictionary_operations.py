dictionary_one = {}
dictionary_two = dict()

employee_dict = {
    "name": "Hitesh",
    "city": "Hyderabad",
    "age": 26
}


# Accessing values of a 'dict'
print(employee_dict["age"])
print(employee_dict.get("age"))

# Add/update entries of a 'dict'
employee_dict["salary"] = 20
employee_dict.update({"salary": 20000})

print(employee_dict.keys())
print(employee_dict.values())
print(employee_dict.items())