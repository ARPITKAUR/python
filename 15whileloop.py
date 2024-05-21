# while loop:
# first declare/ define the variable
i=0
while(i<5):
    print(i+1)
    i=i+1

#if we want to print the no till the condition again and again
i=int(input("enter the number: "))
while(i<=10):
    i=int(input("enter the number: ")) #we use this so that user can take input again n again
    print(i)    
print("the work is done. ")    

# decrementing while loop: ulta chlna
count =5
while(count>0):   #we will check if cnndtn true that the no is >0 then move to next no.
    print(count)
    count=count-1 #if we write + then it will go in infinte loop
else:
    print("now i am in else ")
    
#do while loop*********
#we dont use in python but the difference is that on do while first the work is done thne condition is checked and printed

#emulate (do while) loop:
i=0
while True:
    print(i)
    i=i+1
    if(i%100==0):
        break
    
