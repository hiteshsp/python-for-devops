import timeit

print(timeit.timeit('x=(1,2,3,4,5)', number=100000000))
print(timeit.timeit('x=[1,2,3,4,5]', number=100000000))