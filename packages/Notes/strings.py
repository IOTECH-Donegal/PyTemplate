"""
Strings
By: JOR
Initial: 03JUN22
1. We can use either double or single quotes for strings, standardize!
2. Strings are ordered sequences

"""
print("*** Escape sequences ***")
print("The backslash character is an escape, the character following in a special character")
print("I can insert tabs \tin a \tsentence.")
print("I can break up a line \n by inserting a CR or LF character, or use it to create a blank line. \n")

print("*** Quote marks ***")
print('You can use single quotes for strings')
print("You can also use double quotes")
print("You can use double quotes if you need a single quote in the string.")
print("For example, if you want to print a word like can't \n")

print("*** Print Formatting - Two Methods ***")
print("Method 1")
c = "chips"
b = "beans"
print("You can order fish and {0} with {1}.".format(c, b))
print("Or you can order fish and {r} as {s}.".format(r="rice", s="sushi"))
print("If you have a big floating point number like {r}".format(r=100/9876))
print("you can use float formatting {r:1.5f}".format(r=100/9876))
print("This is in the form VALUE:WIDTH.Precision")
print("you can really mangle presentation using width {r:10.5f}".format(r=100/9876))
print("Method 2")
ver = 3.6
print(f"From Python {ver}, you can also use f strings.\n")
print()
print("There are many other ways to print in particular formats, feel free to find some!")

exit()

print("*** Indexing ***")
test_string = "Hello World!"
position = 4
char = test_string[position]
print(f"I can extract the character '{char}' at position {position} from the string '{test_string}'")
print("Counting starts from position zero.")
print(f"I can get the length of '{test_string}' using the len function, it's equal to {len(test_string)} \n")

print("*** Reverse Indexing ***")
print("I can also identify characters from the end of a string, regardless of the string length")
position = -4
char = test_string[position]
print(f"I can extract the character '{char}' at position {position} from the end of string '{test_string}' \n")

print("*** Slicing ***")
print("You can extract a subsection from START to STOP with a JUMP")
big_string1 = "abcdefghijklmnopqrstuvwxyz"
print(f"I can extract from the 10th character to the end: {big_string1[10:]}")
print(f"I can extract from the beginning to character 12: {big_string1[:12]} not including the 12th character")
print(f"I can extract a subset from 10th to 20th character: {big_string1[10:20]}")
print(f"I can use a step size of 3 to get every third character: {big_string1[::3]}")
print(f"I can combine all from 10th to 20th step 3: {big_string1[10:20:3]}")
print(f"Or reverse a string: {big_string1[::-1]}")

print("*** Immutability ***")
print("You cannot change a letter of a string, you need to create a new string")
print()
print("*** Concatenation ***")
a = "Hello"
b = "World"
print(a + " " + b + ", what about ya?")
print(f"I'm sleeping! {'z' * 10}")
print(f"Adding 2+3: {2+3}")
print(f"Badly adding strings 2+3: {'2'+'3'}")

print("*** Methods ***")
print("Define the string first")
big_string1 = "abcdefghijklmnopqrstuvwxyz"
big_string2 = big_string1.upper()
print(f"String 1: {big_string1}")
print(f"String 2: {big_string2}")
print(f"String 2 using the lower method: {big_string2.lower()}")
print(f"I can split the string based on any character: {big_string1.split('m')}")









