# if want to convert to upper case OR VICE VERSA
# STRINGS AR *******immutable****that means cannot change the exisiting string
name="arpit"
print(name)
print(name.upper())
name1="VANSH"
print(name1.lower())

# if want to remove !
name2="roop!!!!!!!"
print(name2.rstrip("!"))

# if want to replace any word
a="hello world"
print(a.replace("world", "arpit"))
# split : used to convert string to a list and separates the words.
print(a.split(" ")) #remenber to give spae bdw ""

# to make 1st letter capital and it also sets the other letters
print(a.capitalize())

# center() allignds the string in centre acc to parametergivrn by user
print(a.center(20))
# count() tells no of time somthing occurs
print(a.count("world"))

# ends with
str="welcome to the python world !!"
print(str.endswith("!!"))
print(str.endswith("to",4,10)) #this means from 4 to 10 index ends with "to"
# find
print(str.find("the"))

# The isalnum() method returns True only it the entire string only consists of A-Z, a-z, 0-9. If any other characters or punctuations are present, then it returns sales
print(str.isalnum()) #not even the spaces otherwise gives false

# isalpha() only alpbts a-z oe A-Z
# islower() lower aplbts
# isprintable() if strng is printable  \n (not printable)

