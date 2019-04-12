my_list = [0, 1, 2, 3, 4]


an_equal_list = [x for x in range(5)] #[0, 1, 2, 3, 4]
print(an_equal_list)


another_list = [range(5)]
print(another_list)


multiply_list = [x * 3 for x in range(5)]
print(multiply_list)


print(8 % 3)# 2 is the remainder  - - 8/3 == 6r2

print([n for n in range(20) if n % 2 == 0]) # print even numbers in range
print([n for n in range(20) if n % 2 == 1]) # print odd numbers in range


people = [" TOm", "SaM   ", "AliSSa", "ANNA", "  cAesar"]
normalize_people = [person.strip().lower() for person in people]
print(normalize_people)





def who_do_you_know():
    people = input("Enter a list of names: ")
#    split_list = people.split(",")
    normalize_people = [person.strip().lower() for person in people.split(",")] #could keep taking this further but even this is a tab unreadable and not advisable
#    people_without_spaces = []
#    for person in split_list:
#        people_without_spaces.append(person.strip())
    return normalize_people


def ask_user():
    user = input("Enter a name: ")
#    split_list = who_do_you_know()
    if user in who_do_you_know():
        print("{} was found in known people.".format(user))
    else:
        print("{} was not found in known people".format(user))
        
ask_user()