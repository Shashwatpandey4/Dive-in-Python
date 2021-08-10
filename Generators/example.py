#using lists
def square_numbers(nums):
    result = []
    for i in nums:
        result.append(i*i)
    return result

nos = square_numbers([1,2,3,4,6])
print(nos)


#using generators
def cube_numbers(nums):
    for c in nums:
        yield (c*c*c)

cube = cube_numbers([1,3,5,8,2])
for value in cube:
    print(value)

#using list comprehension with generators

abc = (x*x*x for x in [1,2,3,4,6])
print(list(abc))