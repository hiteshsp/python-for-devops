# Tuple is immutable and supports unpacking

tuple1 = (1, 2, 3)

tuple_list = ([1,2,3], 2, 3)

# Modifying a list inside a tuple is possible as List is mutable
tuple_list[0].append(2)

print(tuple_list)

# Unpacking
a, b, c = (20, 30, 40)

print(a,b,c)


"""
Tuples are faster than list as they have no dynamic operations which are supported by lists.
Tuples are hashed into RAM
"""
