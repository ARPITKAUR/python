x=int(input("enter the value of x"))
# x is the variable
match x:
    # if x is 0
    case 0:
        print("the no is zero")
    case 4:
        print("the number matches")
    #for default we use _ 
    
    # case _:
    #     print("x>4")

# ******* we dont need to use break in python.

#if we want to use if in default we will:
    case _ if x!=50:
        print("the no is not equal to 50") 
    case _ if x<50:
        print("the no is to 50")
    case _ :
        print("end")     
