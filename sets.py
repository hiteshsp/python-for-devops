# Sets are unordered collections and contain unique values

"""
Set operations
1. Add
2. Remove
3. Union
4. Intersection
5. Difference
6. Subset/Superset
"""

"""
empty set is created as follows

set1 = set()

collection = {} is a empty dict
"""
set_of_cars = {"skoda", "vw", "ford"}
indian_set_of_cars = {"tata", "mahindra", "maruti"}

print(set_of_cars)
print(indian_set_of_cars)

set_of_cars.add("volvo")
print(set_of_cars)

set_of_cars.add("suzuki")
indian_set_of_cars.add("suzuki")

set_of_cars.remove("ford")
print(set_of_cars)

all_cars = set_of_cars.union(indian_set_of_cars)
print(all_cars)

common_set = set_of_cars.intersection(indian_set_of_cars)

print(common_set)

diff_set = set_of_cars.difference(indian_set_of_cars)
print(diff_set)
print(set_of_cars - indian_set_of_cars)