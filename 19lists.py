# array can only store one data type say int, but List can store multiple data types at one time. and we can changes in lists
# and array needs to be imported but lists are in built  like: import array as arr
l=[1,3,7,8, "hey", True]
print(l)
print(type(l))
print(l[0])
print(l[1])
print(l[2])
print(l[3])
print(l[4])
print(l[5])
# negative index
print(l[-3])
print(l[len(l)-3])
print(l[6-3])
# if we want to find any element
if 7 in l:
    print("yes")
else:
    print("no")

if "arpit" in l:
    print("yes")
else:
    print("no")  
#we can also check string
if "ey" in "hey":
    print("yes its there")

#printing list
print(l[2:5])          
print(l[0:6:2])    #this means will jump to one alter element

# list comprehension :used to creating new lists from other iterables like list tuples dict etc.
list=[i*2 for i in range(10)]
print(list)
# we can also use if in this :
list=[i*2 for i in range(10) if i%2==0]
print(list)