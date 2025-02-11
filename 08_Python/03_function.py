# def hello_world():
#     print("hello world")

# hello_world()

# def hello_world(message):
#     print(message)

# hello_world("This is message i do passing parameter")

# def hello_world(nums):
#     sum=0
#     for i in nums:
#         sum+=i
#     print(sum)

# hello_world([1, 2, 3, 4, 5])


##----------Check NO is prime by using function-------------------#
# def check_prime(num):
#     for i in range(2, num//2):
#         if num%i==0:
#               print("not prime")
#               return
#     print("prime")

# check_prime(9)

##----written first repeating number in a list

# def first_repeating_num(nums):
#     store = set()
#     for i in nums:
#         if i in store:
#             return i
#         store.add(i)

# print(first_repeating_num([1, 2, 2, 2, 3, 4, 5]))


def first_repeating_num(*args):
    store = set()
    for i in args[0]:
        if i in store:
            return i
        store.add(i)

print(first_repeating_num([1, 2, 2, 2, 3, 4, 5]))




