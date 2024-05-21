# age=int(input("enter your age"))
# print("your age is", age)

# # **here indentation is very imp if we dont leave space before print in if loop its not considerd as part of loop.
# if(age>=18) :
#     print("the user can drive the car")
#     print("yes")
# else:
#     print("you are underage")
#     print("no") #this is inside the loop
# print("yay!")  #this is outside the loop so always printed  

# if we want many if else loops
price=100
budget=int(input("enter your budget"))
if(budget-price>100):
    print("you can buy apples")

elif(budget-price<50):
    print("you can buy chips")

else:
    print("you cannot buy anything")    

# nested if else
num =int(input("enter the number: "))
if (num < 0):
     print( "Number is negative.")
elif(num > 0):
    if (num <= 10):
        print( "Number is between 1-10")
    elif (num > 10 and num <= 20):
        print( "Number is between 11-20" )
    else:
       print( "Number is greater than 20")
else:
  print( "Number is zero")