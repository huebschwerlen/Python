def methodception(another):
    return another()

def add_two_numbers():
    return 35 + 77

methodception(add_two_numbers)



###




methodception(lambda: 35 + 77)






my_list = [13, 56, 77, 484]


print(list(filter(lambda x: x != 13, my_list)))  # A lambda function is just a short, one-line function that has no name.

# same as...

print([x for x in my_list if x != 13]) #more pythonic but list comp is more python specific where 'filter' is more widely used in other langs

# same as ....

def not_thirteen(x):
    return x != 13

print(list(filter(not_thirteen, my_list)))

# filter() passes each element of my_list as a parameter to the function.






##




(lambda x: x * 3)(5)

#same as...

def f(x):
    return x * 3

f(5)