#Strings
course = 'Python for Beginners'
print(course.upper())
print(course.lower())
print(course.count('e'))   #finding the number of e in python for beginners
print(course.find('o'))   #finds the first occurence position of o, o is in the 4th position, numbering is 0,1,2,3,4..
print(course.replace('for','4'))
print(course.replace('Beginners','Experts'))
#Strings are imutable i.e. they cannot be changed but can only modify its form
print(course)  #after all the functions used, te string course stil remains the same
print(course.find('Python'))
print('Python' in course)

place = course.find('for')
print(place)