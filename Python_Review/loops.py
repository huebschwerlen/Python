var = "hello"
print(var[0])

for char in var: # iterable are strings, lists, sets, tuples and more
    print(char)
    

my_list = [22, 33, 44, 55, 666, 7]

for x in my_list:
    print(x ** 2) #** mean to the power of ^
    
    
    
    
user_wants_number = True
while user_wants_number == True:
    print(10)
    user_wants_number = False



user_wants_number = True
while user_wants_number == True:
    print(10)
    
    user_input = input("Should we print again? (y/n)")
    if user_input == 'n':
        user_wants_number = False