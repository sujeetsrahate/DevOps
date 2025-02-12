def sum(a, b):
    return a+b

# print(sum(2,4))


mySum = lambda a,b: a+b
# print(mySum(10, 2))

# print((lambda a, b: a+b) (2, 4))

#Example of lambda function in another function

def power(x):
    return lambda n: x**n

print(power(4)(3))