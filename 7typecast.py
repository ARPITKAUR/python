# typecast mean conversion of one datatype to another datatype
# python supports many function / methods like: int() float(), tuple(), dict() for typecasting
a="1"
b="2"
print(a+b) # int is converted to string
# but if want it to be in string only then:
print(int(a)+int(b))

""" 2 types of typr casting
1.explicit - done by the user
2. implicit- done by the python
"""
string="40"
num=2
intstring= int(string)
sum=num+intstring
print("the addition of 2 nos is",sum)

# implicit example
# in this we get float as ans bcz high priority
f=9.9
d=6    #converted to float
print(f+d)

inp=input("enter you name")
print(inp)