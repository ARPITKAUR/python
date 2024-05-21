# for loop can iterate over sequence of iterable object in python
# *******1.iterating a string********
name="vansh"
# syntax
for i in name:
    print(i)
# usinf if in loop
    if(i=="a"):
        print("this is special char")

# EXAMPLE2:
name2="ABHISHEK\n"
for i in name2:
    print(i, end=",")
        
#********2.iterating a list***************
color=["red","green","yellow","blue"]
for i in color:
    print(i)
    # if we want for iteration in this
    for j in i:
        print(j) 

#*******if we want to print many numbers********
# it will print from 0 to 5
for k in range(5):
    print(k) 
#if we want to print from 1 to 5 normaly +1
for k in range(20):
    print(k+1)    

#if we want specifc      it will go till 69
for k in range (55,70):
    print(k)
    
# we have 3 parameter range also (start , stop , step ) i.e with step it will have gap of that numbers
for l in range(0,10,2):    #0 is start point then 10 (till hwere we want to get, 2 (is the gap we want))
    print(l)