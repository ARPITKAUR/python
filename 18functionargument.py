def average(a,b):
    print("average of two no is", (a+b)/2)
average(1,3)    

# 1. default arguments : -----when we declare values in function with argumnet only 
def average(c= 4, d= 5):
    print("average of two no is",(c+d)/2)
average()   #if we write value here then it will ignore upper one and use these one

def name(fname , myname="arpit" , yname="vansh"):
    print('hello', fname, myname, yname)
name("yash")     #this emans it will by default consider this for 1st argument that is fname

# 2.required arguments --------: which are compulsory to give like a, b atleast give value wither uper or niche
# 3.Variable-length arguments:---- somotimes we may nood to pass more aruments than thosa defined in the actual function. This can be done using variable-length arguments.
# type is ++++++++    tuple   ++++++++++
def avg(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    print("the average of the numbers is ", sum/len(numbers))    
avg(4,5,6)


# 4. keyword arbitarary argument: we use **
# means jisko jo nam denge uska vhi print hoga
# type is !!!!!!!!!! DICT **************
def names1(**name):
    print("hello, ", name["fname"], name["yname"], name["lname"])
names1(fname="appi", yname="vansh", lname="vroski")    