# typecasting = the process of converting a value of one data type to another data type
#               2 ways to do it: Explicitly vs Impicitly  

# Explicit typecasting:

name = "Kim"
age = 18
gpa = 3.9
student = True

print(f" {name} is type of type(name)")#if name would be empty then it'll show false
name = bool(name)
print(f" {name} is type of type(name)")#typecasting doesnt work with f-string 

print(f" {age} is type(age)")
age = float(age)
print(f" {age} is ", type(age))


# Implicit typecasting: automatically convert into another data type if we perform any specific operations such as: arithmatic operations
x = 2
y = 2.0
x = x/y

print(x)

