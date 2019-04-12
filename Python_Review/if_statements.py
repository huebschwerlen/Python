should_continue = True
if should_continue == True:
    print("Hello")
    
sdf = True
if sdf: #will default to true so == above is redundant 
    print("Hello")
    
    
    
known_people = ['jack', 'sally', 'dale', 'mary', 'sam']
person = input('enter the person you know: ')

if person in known_people:
    print(person + ' is in the list')
else:
    print('{} not found'.format(person))
    
#if person not in known_people:
#    print(person + ' not found')
# ^ redundant, clunky and could end up needing to iterate twice




numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Modify the method below to make sure only even numbers are returned.
def even_numbers():
    evens = []
    for number in numbers:
        if number % 2 == 0:
            evens.append(number)
    return evens

print(even_numbers())


# Modify the below method so that "Quit" is returned if the choice parameter is "q".
# Don't remove the existing code
def user_menu(choice):
    if choice == "a":
        return "Add"
    elif choice == "q":
        return "Quit"
    
print(user_menu("a"))








def who_do_you_know():
    people = input("Enter a list of names: ")
    split_list = people.split(",")
    
    people_without_spaces = []
    for person in split_list:
        people_without_spaces.append(person.strip())
    return people_without_spaces


def ask_user():
    user = input("Enter a name: ")
#    split_list = who_do_you_know()
    if user in who_do_you_know():
        print("{} was found in known people.".format(user))
    else:
        print("{} was not found in known people".format(user))
        
ask_user()






txt = "apple#banana#cherry#orange"

# setting the max parameter to 1, will return a list with 2 elements!
x = txt.split("#", 2)

print(x)