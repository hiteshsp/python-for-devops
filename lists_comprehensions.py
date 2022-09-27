list_of_numbers = []
for i in range(0, 10):
    list_of_numbers.append(i)
print(list_of_numbers)

list_comprehension = [ i for i in range(0, 10) ]

"""
Multi level list comprehensions
Hacker Rank: List Comprehension
"""
x = int(input("Enter a value for x: "))
y = int(input("Enter a value for y: "))
z = int(input("Enter a value for z: "))
n = int(input("Enter the value of n: "))

final_list_comprehension = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i + j + k != n]

print(final_list_comprehension)