class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []
        
    def average(self):
        return sum(self.marks) / len(self.marks)
    
#    def friend(self, friend_name):
#        return Student(friend_name, self.school)

    @classmethod
    def friend(cls, origin, friend_name, salary):
        return cls(friend_name, origin.school, salary)
    
        
        
        
        
#anna = Student('Anna', 'Oxford')
#
#friend = anna.friend('Greg')
#print(friend.name)
#print(friend.school)


## 


class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school) #when inheriting need to start by setting up superclass by calling its _init_ method
        self.salary = salary
        


anna = WorkingStudent('Anna', 'Oxford', 20.00)
print(anna.salary)

#friend = anna.friend('Greg')
#print(friend.name)
#print(friend.school)


friend = WorkingStudent.friend(anna, 'Greg', 17.50)
print(friend.name)
print(friend.school)
print(friend.salary)