l=[1,45,11,2,4,6,2]
print(l)
# for adding a no at the end
l.append(7)
print(l)
# for sorting
l.sort()
print(l)
l.sort(reverse=True)
print(l)
# index: for checking the index of element
print(l.index(11))  #it is showing for reverese bcz we printed it up therr

# count : is used to count elements how many time it is there
print(l.count(2))
print(l.count(45))
# copy: for copying the elemets from one list to another but not altering the original one
m=l
m[0]=0
print(m)

# insert
l.insert(1,56)
print(l)
# extend: used to extend the 2nd list in 1st
# l.extend(m)
# print(l)

# concat
# or we can also do : k=l+m then print(k)
print(l+m)
