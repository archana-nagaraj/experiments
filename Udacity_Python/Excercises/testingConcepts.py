def vehicle(number_of_tyres, name, color):
    print(number_of_tyres)
    print(name)
    print(color)

vehicle(4, "Mazda", "blue")



# Trying Lists

courses = ['Math', 'Science', 'CompSci']
print(courses)
print(len(courses))
print(courses[1])
print(courses[-1])
#Lists slicing
print(courses[0:2])
print(courses[:2])
print(courses[2:])
print(courses[1:-1])
# Lists methods
#courses.append('Art')
print(courses)

#courses.insert(0,'Art')
print(courses)

#Lists within a list
courses_2 = ['Zoology', 'Writing']
#courses.insert(0,courses_2)
print(courses)
print(courses[0])

# extend a list
courses_3 = ['Education', 'Photography']
#courses.extend(courses_3)
print(courses)

#remove some items from list
courses.remove('Math')
print(courses)
#popped = courses.pop()
print(courses)
#print(popped)

#reverse a list
courses.reverse()
print(courses)

#sorting a list
courses.sort()
print(courses)