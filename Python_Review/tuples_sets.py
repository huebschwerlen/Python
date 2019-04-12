#bad example of averaging grades
#grade_one = 67
#grade_two = 80
#grade_three = 90
#
#print((grade_one + grade_two + grade_three) / 3)


#lists are most flexible as they are mutable, extendable, and can have duplicates
grades_list = [77, 50, 60, 90, 90, 80, 55]
print(grades_list)

grades_list.append(69)

grades_list[0] = 33

print(sum(grades_list) / len(grades_list))

print(grades_list[0]) #prints index

print(grades_list)



#tuple, only difference is it's immutable
grades_tuple = (22, 44, 55, 66, 66, 77, 88, 99)
print (grades_tuple)
#grades_tuple.append(90) - - can't do it, cause it's immutable
#grades_tuple[0] = 59 - - also no no
#work around
grades_tuple = grades_tuple + (200,) #needs the comma with one element to be a tuple
print (grades_tuple)




#sets are unique and unordered - hashing
grades_set = {22, 33, 44, 55, 66, 77, 88, 99, 99, 99}
print(grades_set) #could print or traverse in different order each time - - will also remove duplicates, cause unique
#grades_set[0] = 500 - - no no cause unordered 
grades_set.add(500)
print(grades_set)


#advanced set operations
set_one = {1, 2, 3, 4, 5}
set_two = [1, 3, 5, 7, 9, 11]

print(set_one.intersection(set_two)) #.intersetion finds and prints common variables between sets

print(set_one.union(set_two)) #.union merges the sets together, dropping dupllicates, cause unique

print({1, 2, 3, 4}.difference({1, 2}))#will print values not found in both sets
