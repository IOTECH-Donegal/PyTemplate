"""
Numbers
By: JOR
Initial: 03JUN22

1. Do not start variable names with a number
2. Do not use a built-in keyword as a variable
3. There can be no spaces in a name
4. Do not use symbols except underscore
5. Variable names, use all lower case (PEP8)
6. Global variable names, all CAPITALS

In these examples, I use formatted strings

"""

a = 5
b = 3
print (f"Example calculations using {a} and {b}")

# Calculate within the f string
print(f"Addition (a+b) result is: {a+b} of type {type(a+b)}")
print(f"Subtraction (a-b) result is: {a-b}  f type {type(a-b)}")
print(f"Division (a/b) result is: {a/b} of type {type(a/b)}")

# Calculate, then show the result
value = a%b
print(f"Modulus or remainder (a%b) result is: {value} of type {type(value)}")
value = a*b
print(f"Multiplication (a*b): result is: {value} of type {type(value)}")
value = a**b
print(f"Powers (a**b): result is: {value} of type {type(value)}")

print("*** Parenthesis to define order of calculations ***")
a = 5 + 3 * 5 + 2
b = (5 + 3) * (5 + 2)
print(f"Very different outcomes between {a} and {b}")

print("*** Dynamic data types ***")
message = "Ornithology"
print(f"The variable message is set to {message} with a type of {type(message)}")
message = 214
print(f"The variable message is set to {message} with a type of {type(message)}")

print("*** Calculations using meaningful variable names ***")
net = 10000
vrt = .25
gross = net + (net * vrt)
print(f"From the dealer, the car costs E{net}, however after applying VRT of {vrt}, the final price is {gross}")
print(f"The data types of net is {type(net)}")
print(f"The data types of vrt is {type(vrt)}")
print(f"The calculated result has a data type of {type(gross)}")


