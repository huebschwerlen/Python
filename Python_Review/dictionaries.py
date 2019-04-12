my_set = {1, 2, 4}

my_dict = {'name': 'sam', 'age': 90, 'grades': [12, 34, 90] }

another_dict = {1: 15, 2: 76, 3: 50}


lottery_player = {
    'name': 'sam',
    'numbers': (12, 45, 67, 88)  #values can be list, sets, tuples, dicts
}

print(sum(lottery_player['numbers']))
lottery_player['name'] = 'Jon'


universities = [               #list of two dicts
    {
        'name': 'oxford',
        'location': 'UK'
    },
    {
        'name': 'MIT',
        'location': 'US'
    }
    
]


another_dict_in_dict = {
    'key': {
        'name': 'jose'
    },
    
}



# Create a variable called student, with a dictionary.
# The dictionary must contain three keys: 'name', 'school', and 'grades'.
# The values for each must be 'Jose', 'Computing', and a tuple with the values 66, 77, and 88.
student = {
    'name': 'Jose',
    'school': 'Computing',
    'grades': (66, 77, 88)
} #could all be one line too

# Assume the argument, data, is a dictionary.
# Modify the grades variable so it accesses the 'grades' key of the data dictionary.
def average_grade(data):
    grades = data['grades'] #change this
    return sum(grades) / len(grades)


# Implement the function below
# Given a list of students (a list of dictionaries), calculate the average grade received on an exam, for the entire class
# You must add all the grades of all the students together
# You must also count how many grades there are in total in the entire list
def average_grade_all_students(student_list):
    total = 0
    count = 0
    for student in student_list:
        # Implement here
#       total = total + sum(student['grades'])
        total += sum(student['grades'])
        count = count + len(student['grades'])

    return total / count