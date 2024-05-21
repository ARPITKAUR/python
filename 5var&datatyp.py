#variables contains the data., so these 2 below are diff variables.
# datatype tells the type of value
#****IMP***********IN python everything is OBJECT*************REMEBER like dict , list etc anthing is an object
a=123       #int
c=None
d=True
e=complex(4,7)
print(a)
b="arpit"  #string
print(b)

# we cant concatinate 2 diff datatypes using + directly print(a+b) its wrong    
print("the type of a is ", type(a))
print("the type of b is ", type(b))
print("the type of C is ", type(c))
print("the type of D is ", type(d))
print("the type of e is ", type(e))

# lists: collection of items with different datatypes but is mutable i.e can be modified
# tuples : same as lists but in immutable and csnnot be modifies after crested
list=[5,7,"appi", ["mine","dsa"]]
print(list)
tuple=(("parrot","sparrow"), 23, 78)
print(tuple)
dict={"name":"arpit", "age":20,"canvote":True}
print(dict)
