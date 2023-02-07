#Arithmetic Operators
print(10 + 3) #addition
print(10 - 3)  #subtraction
print(10 * 3)  #multiplication
print(10 / 3)  #division with "float" result
print(10 // 3) #gives the value of 10 divided by 3 as an integer or whole number, division with "integer" result
print(10 % 3)  #dividion or modulus: gets the remainder value of the divison
print(10 ** 3) #Exponent: raised to the power
x = 10
x = x + 3
print(x)
x += 3  #the same as "x = x + 3" reffered to as augmented assignment operator
print(x)
x -= 3
print(x)
x *= 3
print(x)

#Operator Precedence
x = 10 + 3 * 2 #Python follows maths principles
print(x)
x = (10 + 3) * 2
print(x)

#Comparison Operators: used to compare values
x = 3 > 2 #boolean variable, greater than
print(x)
x = 3 >= 2 #greater than or equal to
print(x)
x = 3 < 2 #less than
print(x)
x = 3 <= 2 #less than or equal to
print(x)
x = 3 == 2 #equal to
print(x)
x = 3 != 2 #not equal to
print(x)

print("Logical Operators")
#Logical Operators
print("And Operator")
price = 25
print(price > 10 and price < 30)  #And operator &&
print("Or Operator")
price = 5
print(price > 10 or price < 30) #Or operator ||
print("Not Operator")
price = 5
print(not price > 10) #Not operator !