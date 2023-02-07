first_name = "John"
last_name = "Smith"
age = 20
is_new = False
print(first_name)
print(last_name)
print(age)
if is_new is True:
    print ("New Patient")
if is_new is False:
    print ("Existing patient")

#Receiving Inputs, variable declaration: variablename = value

name = input("What is your name? ")
print("Hello " + name)

#Type Conversion
birth_year = input("Enter your birth year: ")
age = 2020 - int(birth_year)
print(age)

First = input("First: ") #declaring a variable: assigning a value to a variable
Second = input("Second: ")
Total = float(First) + int(Second)
print("Sum:" + str(Total))

a = input("What is your name? ")
b = input("Hello " + a )
c = input("What year were you born? ")
d = input("What is your name? ")
e = input("Hello " + d )
f = input("What year were you born? ")
b_age = 2023 - int(c)
d_age = 2023 - int(f)
sum = b_age + d_age
print("Your total age is:" + str(sum))