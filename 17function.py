a=5
b=7
geometricmean=(a*b)/(a+b)
print(geometricmean)

a=9
b=3
geometricmean=(a*b)/(a+b)
print(geometricmean)

# when we have some operation it will make the code long so as to avoid we will use functions

def CalculateGmean(a,b):   #calculategmean is the functino name. a, b are the arguments
    mean=(a*b)/(a+b)
    print(mean)
# like if we want if else and some text d=then we can make function rsther then doing individually
def Greaterthen(a,b):  #and we can simple add this functino below
    if(a>b):
        print("a is greater then b ")
    else:
        print("a is smaller or equal to b")  

a=int(input("enter the number "))
b=int(input("enter the number"))
Greaterthen(a,b)
CalculateGmean(a,b)

c=5
d=7
Greaterthen(c,d)
CalculateGmean(c,d)
# inspite of this we culd also write : calculategmean(4,7)
CalculateGmean(67,89)

# if want to make a function but want to add body down later we use pass
def issmaller(a,b):
    pass

# types of function: bulit in and userdefiend
# built in - min() max() sum() type() dict() list() print() tuple()

