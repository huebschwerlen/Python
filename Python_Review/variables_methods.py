string = "hello"
    
print (string)
    
    
#this is a comment


#methods

def print_method(my_param):
    print("hello")
    print("world")
    print(my_param)
    
print_method('I love ya')


def multiply_method(num1, num2):
    return num1 + num2

result = multiply_method(5, 3)
print(result)
print_method(result)

print_method(multiply_method(5, 5))