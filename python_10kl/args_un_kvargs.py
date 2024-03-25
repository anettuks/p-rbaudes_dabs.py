# #args
# def add(x, y):
#     return x+y

# print(add(2,3))

# def add(x, y, z):
#     return x+y+z

# print(add(2, 3, 5))



# def add(*numbers):
#     total = 0
#     for num in numbers:
#         total += num
#     return total


# print(add(2, 3))
# print(add(2, 3, 5))
# print(add(2, 3, 5, 7))
# print(add(2, 3, 5, 7, 9))




# # kwargs
# def total_fruits(**kwargs):
#     print(kwargs, type(kwargs))


# total_fruits(banana=5, mango=7, apple=8)




# def total_fruits(**fruits):
#     total = 0
#     for amount in fruits.values():
#         total += amount
#     return total


# print(total_fruits(banana=5, mango=7, apple=8))
# print(total_fruits(banana=5, mango=7, apple=8, oranges=10))
# print(total_fruits(banana=5, mango=7))



def myFunc2(*args):
    return sum(args)
print(myFunc2(3,5,9,7,6,4))
print(myFunc2(3,5,9,7,6,4,15,7))



def videjais(*args):
    return sum(args)/len(args)

vid = videjais(3,4,5)
print("Vidējais ir ", vid)















