# variables: a reusable container for storing a value/data
#            a variable behaves as if it was the value it contains   
#            3 methods to use it with print statement = STRING CONCATINATION, SEPARATE ARGUMENTS, F-STRING

# data types: 
# sssbbnnm - string, sequence(list, tuple, range), set types,  boolean, binary(bytes, bytearray), numeric(int, float, complex, number), none, mapping type(dict)
# most commone are: integer, float, string, boolean


age = 24
players = 11
quantity = 2

print("you are " + str(age) + "years old- string concatination")
print("you are", age, "years old- here using 3 separate arguments")
print(f"you are {age} years old- this f-string is mostly used")

# Integers:     
print(f"You are {age} years old")
print(f"There are {players} players online")
print(f"You would like to buy {quantity} items")

# Float:
gpa = 3.2
distance = 2.9
price = 10.99

print(f"Your gpa is {gpa}")
print(f"You ran {distance}Km")
print(f"The price is ${price}")

# Strings:
name = "Kim"
food = "Burger"
email = 'kim2411@gmail.com'

print(f"{name} gpa is {gpa}")
print(f"You ate {food}")
print(f"The mail Id is {email}")

# Boolean: typically we use them with if statements and in conditions
online = True

print(f"{name} is online? {online}")

# For multiple values
x, y, z = 1, 2, 3
# x = y = z = 4

print(x)
print(y)
print(z)