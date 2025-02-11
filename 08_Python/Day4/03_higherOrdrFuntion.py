def Sum_number(x):
    return sum(x)


def higher_OrderFunction(f, lst):
    var = f(lst)
    return var

result = higher_OrderFunction(Sum_number,[1, 2, 3, 4, 5])
print(result)
