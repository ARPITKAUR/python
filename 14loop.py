# if we want to combine 2 lists
# use zip()
fruit=["apple","mango"]
color=["red","yellow"]

for fruit,color in zip(fruit,color):
    print(fruit ,"is" ,color)


number=((1,3), (3,5))
# for i in fruit2:
#     print(i) 
  
# if dont want brackets and , we use:
for a,b in number:
    print(a,b)

